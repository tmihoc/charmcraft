manage-resources)=
# How to manage resources

> See first: [`juju` | Charm resource](https://juju.is/docs/juju/charm-resource), [`juju` | Manage resources](https://juju.is/docs/juju/manage-charm-resources)

## Declare a resource

To declare a resource required by your charm, in your charm's `charmcraft.yaml file` specify the `resources` key.

> See more: {ref}`file-charmcraft-yaml-resources`
>
> See next: [`ops` | Manage resources]()


````{tip}
During development, it may be useful to specify the resource at deploy time to facilitate faster testing without the need to publish a new charm/resource in between minor fixes. For example, assuming the resource is a `/tmp/somefile.txt` file, you could pack and the deploy with `juju deploy ... --resource`:

```text
echo "TEST" > /tmp/somefile.txt
charmcraft pack
juju deploy ./my-charm.charm --resource my-resource=/tmp/somefile.txt
```

````

(publish-a-resource)=
## Publish a resource on Charmhub

```{note}
You must have already published the charm. See more: {ref}`publish-a-charm`.

```

To publish a resource on its charm's Charmhub page, run the `charmcraft upload-resource` command followed by the name of the charm, the name of the resource (cf. `charmcraft.yaml`), and `--filepath=<path to file resource>` / `--image=<OCI image>`. For example:

```{note}

The option `--image` must indicate an OCI image's digest, being it in the short or long form (e.g.: `70aa8983ec5c` or `sha256:64aa8983ec5cea7bc143af18829836914fa405184d56dcbdfd9df672ade85249`). When using the "short form" of the digest, the image needs to be present locally so its proper ID (the "long form") can be retrieved.


```


```text
$ charmcraft upload-resource my-super-charm someresource --filepath=/tmp/superdb.bin
Revision 1 created of resource 'someresource' for charm 'my-super-charm'
```

```text
$ charmcraft upload-resource my-super-charm redis-image --image=sha256:64aa8983ec5cea7bc143af18829836914fa405184d56dcbdfd9df672ade85249
Revision 1 created of resource 'redis-image' for charm 'my-super-charm'
```

Charmcraft will first check if that specific image is available in Canonical's Registry, and just use it if that's the case. If not, it will try to get it from the developer's local OCI repository (needs `dockerd` to be installed and running), push it to the Canonical's Registry, and then use it. Either way, when the upload has completed, you end up with a resource revision.

To update a pre-uploaded resource, run the `upload-resource` command again. The result will be a new revision.

> See more: {ref}`ref_commands_upload-resource`

## View all the resources published on Charmhub 

To view all the resources published on Charmhub for a charm, run `charmcraft resources` followed by the charm name:

```{important}

**If you're not logged in to Charmhub:** The command will open up a browser window and ask you to log in.

```

```text
$ charmcraft resources mycharm
```

> See more: {ref}`ref_commands_resources`

(manage-resource-revisions)=
## Manage resource revisions
### List all the available resource revisions

To view all the revisions for a resource associated with a charm you've uploaded to Charmhub, run `charmcraft resource-revisions` followed by the charm name and the resource name. For example:

```text
$ charmcraft resource-revisions mycharm myresource
```

> See more: {ref}`ref_commands_resource-revisions`

### Set the architectures for a resource revision

To set the architectures for a revision of a resource associated with a charm you've uploaded to Charmhub, run `charmcraft set-resource-architectures` followed by the name of the charm, the name of the resource, and the architecture(s), using the `--resources` flag to specify the target resource revision. For example:

```text
$ charmcraft set-resource-architectures mycharm myresource --revision=1 arm64,armhf
```

> See more: {ref}`ref_commands_set-resource-architectures`
