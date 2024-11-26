# Charmcraft (`charmcraft`)

```{toctree}
:maxdepth: 2
:hidden: true

tutorial/index
howto/index
reference/index
explanation/index
```

Charmcraft (`charmcraft`) is a tool designed to simplify the creation, building, and sharing of a [`juju` charm](https://juju.is/docs/juju/charmed-operator).

When you initialise a charm with the `charmcraft` CLI, you automatically get all the crucial project files, pre-populated with helpful template content. These files are such that they can be `charmcraft`-packed right away; however, to make them meaningul for the application you are charming, you'll want to customise the YAML and [`ops`](https://juju.is/docs/sdk/ops)-powered Python in these files. For certain types of applications (Django, FastAPI, Flask, Go), if you initialise with a suitable `charmcraft` extension, things are even easier -- just tweak a few values in the YAML and you get a fully functioning charm. Either way, once you're pleased with what you've got, you can again use `chamcraft` to publish your charm on [Charmhub](https://charmhub.io/).

You can create, build, and share a charm any way you want, but with `charmcraft` you get state-of-the-art results in record time.

If you're a charm author, you *must* use `charmcraft`!


---------

## In this documentation

````{grid} 1 1 2 2

```{grid-item-card} [Tutorial](/index)
:link: tutorial/index
:link-type: doc

**Start here**: a hands-on introduction to Example Product for new users
```

```{grid-item-card} [How-to guides](/index)
:link: howto/index
:link-type: doc

**Step-by-step guides** covering key operations and common tasks
```

````

````{grid} 1 1 2 2
:reverse:

```{grid-item-card} [Reference](/index)
:link: reference/index
:link-type: doc

**Technical information** - specifications, APIs, architecture
```

```{grid-item-card} [Explanation](/index)
:link: explanation/index
:link-type: doc

**Discussion and clarification** of key topics
```

````

---------


## Project and community

Charmcraft is a member of the Canonical family. It's an open source project
that warmly welcomes community projects, contributions, suggestions, fixes
and constructive feedback.

* [Ubuntu Code of Conduct](https://ubuntu.com/community/code-of-conduct).
* [Canonical contributor licenses agreement](https://ubuntu.com/legal/contributors).

<!--
Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
-->