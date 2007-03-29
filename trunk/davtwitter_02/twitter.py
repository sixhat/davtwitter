#!/usr/bin/env python
# encoding: utf-8
"""
DavTwitter is series of scripts that make a River at Twitter from an RSS file
email: david.rodrigues@gmail.com
site: http://code.google.com/p/davtwitter/

This file is part of DavTwitter.

DavTwitter is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

Foobar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import urllib2
import urllib
import sys
import re
import base64
from urlparse import urlparse

# CHANGE THIS
username = 'YOUR TWITTER ACOUNT EMAIL'
password = 'YOUR TWITTER PASSWORD'          
# DONT CHANGE ANYTHING AFTER THIS

theurl = 'http://twitter.com/statuses/update.xml'

def sendTwitter(texto):
	req = urllib2.Request(theurl)
	try:
	    handle = urllib2.urlopen(req)
	except IOError, e:
	    # here we *want* to fail
	    pass
	else:
	    # If we don't fail then the page isn't protected
	    print "This page isn't protected by authentication."
	    sys.exit(1)

	if not hasattr(e, 'code') or e.code != 401:
	    # we got an error - but not a 401 error
	    print "This page isn't protected by authentication."
	    print 'But we failed for another reason.'
	    sys.exit(1)

	authline = e.headers['www-authenticate']
# this gets the www-authenticate line from the headers
# which has the authentication scheme and realm in it

	authobj = re.compile(
	    r'''(?:\s*www-authenticate\s*:)?\s*(\w*)\s+realm=['"]([^'"]+)['"]''',
	    re.IGNORECASE)
# this regular expression is used to extract scheme and realm
	matchobj = authobj.match(authline)

	if not matchobj:
	    # if the authline isn't matched by the regular expression
	    # then something is wrong
	    print 'The authentication header is badly formed.'
	    print authline
	    sys.exit(1)

	scheme = matchobj.group(1)
	realm = matchobj.group(2)
# here we've extracted the scheme
# and the realm from the header
	if scheme.lower() != 'basic':
	    print 'This example only works with BASIC authentication.'
	    sys.exit(1)

	base64string = base64.encodestring(
	                '%s:%s' % (username, password))[:-1]
	authheader =  "Basic %s" % base64string
	req.add_header("Authorization", authheader)

	dic = {'status':texto}
	dados = urllib.urlencode(dic)
	try:
	    handle = urllib2.urlopen(req,dados)
	except IOError, e:
	    # here we shouldn't fail if the username/password is right
	    print "It looks like the username or password is wrong."
	    sys.exit(1)
	thepage = handle.read()
	return thepage
	
def main():
	pass

if __name__ == '__main__':
    main()
