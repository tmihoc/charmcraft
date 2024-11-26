(manage-names)=
# Manage names


(register-a-name)=
## Register a name on Charmhub


To register a name for your charm on Charmhub, use the `chamrcraft register` command followed by your desired name. E.g.,

```bash
$ charmcraft register my-awesome-charm
Congrats! You are now the publisher of 'my-awesome-charm'
```

> See more: {ref}`command-charmcraft-register`

This creates four channels, with track `latest` with risk level  `edge`, `beta`, `candidate`, `stable`, respectively.

> See more: {ref}`manage-channels`

## View registered names

To view the names you've registered on Charmhub, run `charmcraft names`.

> See more: {ref}`command-chamcraft-names`

## Unregister a name

```{caution}
A name can be unregistered only if you haven't yet uploaded anything to it.
```

To unregister a name, run `charmcraft unregister` followed by the name.

> See more: {ref}`command-charmcraft-unregister`
