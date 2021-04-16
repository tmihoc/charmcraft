# Copyright 2021 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# For further info, check https://github.com/canonical/charmcraft

"""Module to work with OCI registries."""

import logging
from urllib.request import parse_http_list, parse_keqv_list

import requests

from charmcraft.cmdbase import CommandError

logger = logging.getLogger(__name__)

# some mimetypes
MANIFEST_LISTS = 'application/vnd.docker.distribution.manifest.list.v2+json'
MANIFEST_V2_MIMETYPE = 'application/vnd.docker.distribution.manifest.v2+json'
LAYER_MIMETYPE = 'application/vnd.docker.image.rootfs.diff.tar.gzip'
JSON_RELATED_MIMETYPES = {
    'application/json',
    'application/vnd.docker.distribution.manifest.v1+prettyjws',  # signed manifest
    MANIFEST_LISTS,
    MANIFEST_V2_MIMETYPE,
}


def assert_response_ok(response, expected_status=200):
    """Assert the response is ok."""
    if response.status_code != expected_status:
        if response.headers.get('Content-Type') in JSON_RELATED_MIMETYPES:
            errors = response.json().get('errors')
        else:
            errors = None
        raise CommandError(
            "Wrong status code from server (expected={}, got={}) errors={} headers={}".format(
                expected_status, response.status_code, errors, response.headers))

    if response.headers.get('Content-Type') not in JSON_RELATED_MIMETYPES:
        return

    result = response.json()
    if 'errors' in result:
        raise CommandError("Response with errors from server: {}".format(result['errors']))
    return result


class OCIRegistry:
    """Interface to a generic OCI Registry."""

    def __init__(self, server, organization, image_name):
        self.server = server
        self.orga = organization
        self.name = image_name

        self.auth_token = None
        self.auth_encoded_credentials = None

    def _authenticate(self, auth_info):
        """Get the auth token."""
        headers = {}
        if self.auth_encoded_credentials is not None:
            headers['Authorization'] = 'Basic {}'.format(self.auth_encoded_credentials)

        logger.debug("Authenticating! %s", auth_info)
        url = "{realm}?service={service}&scope={scope}".format_map(auth_info)
        response = requests.get(url, headers=headers)

        result = assert_response_ok(response)
        auth_token = result['token']
        return auth_token

    def _get_url(self, subpath):
        """Build the URL completing the subpath."""
        return "https://{}/v2/{}/{}/{}".format(self.server, self.orga, self.name, subpath)

    def _get_auth_info(self, response):
        """Parse a 401 response and get the needed auth parameters."""
        www_auth = response.headers['Www-Authenticate']
        if not www_auth.startswith("Bearer "):
            raise ValueError("Bearer not found")
        info = parse_keqv_list(parse_http_list(www_auth[7:]))
        return info

    def _hit(self, method, url, headers=None, **kwargs):
        """Hit the specific URL, taking care of the authentication."""
        if headers is None:
            headers = {}
        if self.auth_token is not None:
            headers['Authorization'] = 'Bearer {}'.format(self.auth_token)

        logger.debug("Hitting the registry: %s %s", method, url)
        response = requests.request(method, url, headers=headers, **kwargs)
        if response.status_code == 401:
            # token expired or missing, let's get another one and retry
            try:
                auth_info = self._get_auth_info(response)
            except (ValueError, KeyError) as exc:
                raise CommandError(
                    "Bad 401 response: {}; headers: {!r}".format(exc, response.headers))
            self.auth_token = self._authenticate(auth_info)
            headers['Authorization'] = 'Bearer {}'.format(self.auth_token)
            response = requests.request(method, url, headers=headers, **kwargs)

        return response