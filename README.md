[![License]][url: License] [![Semver]][url: Semver] [![Gittip]][url: Gittip]

# [`mu-git-ssh`]

> [`mu-git-ssh`] is a small program for handling situations where you might have multiple
> accounts/users for the same git host (e.g: `github.com`) and where you are connecting via
> SSH and you dont want to modify the domain so that you can copy-paste the git repo SSH URI.

## What is this?

`mu-ssh-git`, a tiny program that should be set as `GIT_SSH`.

When used for git repos hosted on for example github, it will
prepend the username/organization name of the repo, which is
passed as part of the last argument that git calls it with, to
the host which is passed as the first argument of `GIT_SSH`.

So for example: `git@github.com:Centril/mu-ssh-git.git` becomes:
`git@Centril.github.com:Centril/mu-ssh-git.git`

This can then be used in `/etc/ssh/ssh_config` or `~/.ssh/config`
to bind it to an identity file.

An example of a config file could be:
```
Host Centril.github*
	IdentityFile ~/.ssh/id_github_centril_keepass_rsa

Host *github*
	User git
	HostName github.com
```
This allows you to simply copy paste links from github when doing
git clone and other commands that are remote management related and
it will use the correct identity instead of failing due to wrong identity.

It works with both python2 and python3.

## Installation

Clone the repo to your local machine:

```shell
git clone git@github.com:Centril/mu-ssh-git.git
```

Set `GIT_SSH` enviromnent variable to the `mu-ssh-git.py` script.

Set `GIT_SSH_REAL` to the ssh program that `mu-ssh-git.py` should forward to.
If `GIT_SSH_REAL` is not set, then `ssh` will be used from the path. If this is
the correct program you don't have to set `GIT_SSH_REAL`.

### Windows:

Python must be set to handle `.py` files by default.
If you don't want to do this, you can instead set `GIT_SSH_COMMAND` to: `python <path>\mu-ssh-git.py`.

## Changelog

See **[CHANGES.md]**.

## Copyright & License

Licensed under the **[GPL2+ License]**.
Copyright 2015 Mazdak Farrokhzad.

## Bugs / Issues / Feature requests / Contribution

Want to contribute? Great stuff! Please use the issue system that github provides to report bugs/issues or request an enhancement. Pull requests are also more than welcome.

## Author

**Mazdak Farrokhzad / Centril [&lt;twingoow@gmail.com&gt;]**

[![twitter][twitter_image]][twitter] [![github][github_image]][github] [![facebook][facebook_image]][facebook]

<!-- references -->

[Gittip]: http://img.shields.io/gittip/Centril.svg?style=flat
[url: Gittip]: https://www.gittip.com/Centril/
[License]: http://img.shields.io/badge/license-GPL2+-blue.svg?style=flat
[url: License]: LICENSE.md
[Semver]: http://img.shields.io/badge/semver-2.0.0-blue.svg?style=flat
[url: Semver]: http://semver.org/spec/v2.0.0.html

[`mu-git-ssh`]: https://github.com/Centril/quicklaunch

[twitter]: http://twitter.com/CenoRIX
[twitter_image]: http://cdn.flaticon.com/png/128/8800.png
[github]: https://github.com/centril
[github_image]: http://cdn.flaticon.com/png/128/25231.png
[facebook]: https://www.facebook.com/Centril
[facebook_image]: http://cdn.flaticon.com/png/128/33702.png
[&lt;twingoow@gmail.com&gt;]: mailto:twingoow@gmail.com

[CHANGES.md]: CHANGES.md
[GPL2+ License]: LICENSE.md

<!-- references -->