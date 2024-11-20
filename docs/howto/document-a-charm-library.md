(how-to-document-a-charm-library)=
# How to document a charm library

<!-- This doc uses content from https://discourse.charmhub.io/t/document-your-library/4422 , removing all content already covered in other docs and focusing just on the documentation part. It supersedes said doc.-->

You've created your charm library. It is now time to document it. Libraries have 3 types of documentation sections: the metadata, the header of the file, and the Python docstring. This document shows how to use each.

**Contents:**

- [The metadata](#heading--the-metadata) 
- [The header](#heading--the-header)
- [The docstring](#heading--the-docstring)


<a href="#heading--the-metadata"><h2 id="heading--the-metadata">The metadata</h2></a>

The command `charmcraft create-lib` automatically generates inside the `<libname>.py`  the following metadata fields:

```python
# Do not change
LIBID = "abcdef12345" # Unique ID that refers to the library forever
LIBAPI = 3 # API version for non-backwards compatibility evolution
LIBPATCH = 2 # A patch version for all non-breaking changes

def function():
	return "foo"

class Example:
	def __init__(self, foo, bar):
    		self.foo = foo
    		self.bar = bar

	def info(self, add):
    		return add + self.foo 
```

`LIBID` is a unique identifier for the library across the entire universe of charms that is assigned by Charmhub to this particular library automatically at library creation time.  It enables Charmhub and `charmcraft` to track the library uniquely even if the charm or the library are renamed, which allows updates to warn and guide users through the process. Make sure to never change it.

`LIBAPI` and `LIBPATCH` are set to an initial state (`0` and `1` correspondingly), which is fine for now, but in general note that LIBAPI must match the major version in the import path and LIBPATCH must match the current patch version (needs to be updated when changing).

<a href="#heading--the-header"><h2 id="heading--the-header">The header</h2></a>

The header of the file is a Python comment at the top of your library written using the triple quote:  `"""Like this """`. It supports Markdown following the [CommonMark](https://commonmark.org/) specification.

Use the header to describe the library.

<!--I DON'T UNDERSTAND HOW THIS FITS WITH THE ABOVE. THERE ARE NO TRIPLE QUOTES IN THE EXAMPLE BELOW.
Describe this class by adding a section at the top of the library:

```
 # My library

This library was made as while following **a tutorial**.

You can find more information on {ref}`the Charmhub website <5784md>`).
```

Note that the section supports markdown.
-->


<a href="#heading--the-docstring"><h2 id="heading--the-docstring">The docstring</h2></a>


The Python docstring is used to describe the functions and classes that the library provides. It supports the [Google Python Docstring](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) format.

Use Python docstrings to explain each function.

``` python
def function():
	"""This sentence is a summary of the function.

	This section gives more details about the function and what
	it does. In this case the function returns foo.

	Returns:
    		A string containing "foo"

 	"""

	return "foo"

class Example:
	"""A one sentence summary of the class.
	This section gives more details about the class and what
	it does.

	Arguments:
    		foo (int): the argument foo
    		bar (str): the argument bar

	Attributes:
    		foo (int): the attribute foo
    		bar (str): the attribute bar
	"""

	def __init__(self, foo, bar):
    		self.foo = foo
    		self.bar = bar

	def info(self, add=1):
        	"""Return foo plus add.

        	This function adds add to foo 

        	Arguments:
            	    add (int, optional): The number to add to foo. Defaults to 1.

        	Returns:
               	self.foo plus add
        	"""

    		return add + self.foo
```
