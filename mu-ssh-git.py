#!/usr/bin/env python

#
#	Copyright (c) 2015 Mazdak Farrokhzad.
#
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 2 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License along
#	with this program; if not, write to the Free Software Foundation, Inc.,
#	51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
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
"""

__version__ = "1.0.0"
__license__ = "GPL2+"
__status__ = "Release"
__copyright__ = "Copyright 2015, Mazdak Farrokhzad"
__author__ = "Mazdak Farrokhzad"
__maintainer__ = __author__
__credits__ = []
__email__ = "twingoow@gmail.com"

from functools import partial
import sys, os, subprocess

# Fix for most sites:
def default( host ):
	path = sys.argv[-1].split( ' ' )[-1].strip( "'" )
	user = path.split( '/' )[0]
	site = host.split( '@' )[-1].split( '.' )[0]
	return 'git@%s.%s.com' % (user, site)

# The sites which we have fixes for:
fixlist = {
	'git@github.com': default,
	'git@bitbucket.org': default,
	'git@gitlab.com': default
}

# Fix host if needed:
host = sys.argv[1]
if host in fixlist: host = fixlist[host]( host )

# Call GIT_SSH_REAL or default to `ssh`:
ssh = os.getenv( 'GIT_SSH_REAL', 'ssh' )
code = subprocess.call( [ssh, host, sys.argv[-1]] )
sys.exit( code )