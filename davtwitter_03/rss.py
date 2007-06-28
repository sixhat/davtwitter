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
import feedparser

def getRSS(rss):
	d = feedparser.parse(rss)
	k = len(d.entries)
	out = {}
	for i in range(k):
		item = { "titulo" : d.entries[i].title.encode("UTF-8") , "link" : d.entries[i].link }
		out[i] =  item 
		
	return out
	


def main():
	pass

if __name__ == '__main__':
    main()

