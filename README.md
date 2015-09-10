[![License]][url: License] [![Semver]][url: Semver] [![Gittip]][url: Gittip]

# [`mu-git-ssh`]

> [`mu-git-ssh`] is a small program for handling situations where you might have multiple
> accounts/users for the same git host (e.g: `github.com`) and where you are connecting via
> SSH and you dont want to modify the domain so that you can copy-paste the git repo SSH URI.

## Ideas

Currently, [`mu-git-ssh`] is at the planning/idea stage.

Aims of the project are:

+ Small footprint
+ Developed in `rust`.
+ GPL+ license.
+ Terminal based, supposed to be used in `GIT_SSH` and then forward to `OpenSSH`, or similar.
+ Possibly some GUI prompts if applicable later on, but this is for later versions if any.
+ Replace e.g: `github.com` with for example `centril.github.com` if you are logging in as user `centril`.
	* This requires the user to create an entry for `centril.github.com` in `~/.ssh/config`.
+ Possibly ask for a key file path if the user/account is not recognized, i.e: client has not done anything with
  a repo of that user/account before... Then auto-generate some config to add in `~/.ssh/config`.
  This will work well with `KeeAgent` and other managers.

## Installation & Building

Building will of course be based on rust/cargo.
@TODO

## Changelog

See **[CHANGES.md]**.

## Bugs / Issues / Feature requests / Contribution

Want to contribute? Great stuff! Please use the issue system that github provides to report bugs/issues or request an enhancement. Pull requests are also more than welcome.

## Author

**Mazdak Farrokhzad / Centril [&lt;twingoow@gmail.com&gt;]**

+ [twitter]
+ [github]

## Copyright & License

Licensed under the **[GPL 2 License]**.
Copyright 2015 Mazdak Farrokhzad.

## Acknowledgements

> PLACEHOLDER

<!-- references -->

[Gittip]: http://img.shields.io/gittip/Centril.svg?style=flat
[url: Gittip]: https://www.gittip.com/Centril/
[License]: http://img.shields.io/badge/license-GPL_2-blue.svg?style=flat
[url: License]: LICENSE.md
[Semver]: http://img.shields.io/badge/semver-2.0.0-blue.svg?style=flat
[url: Semver]: http://semver.org/spec/v2.0.0.html

[`mu-git-ssh`]: https://github.com/Centril/quicklaunch

[twitter]: http://twitter.com/CenoRIX
[github]: http://github.com/centril
[&lt;twingoow@gmail.com&gt;]: mailto:twingoow@gmail.com

[CHANGES.md]: CHANGES.md
[GPL 2 License]: LICENSE.md

<!-- references -->