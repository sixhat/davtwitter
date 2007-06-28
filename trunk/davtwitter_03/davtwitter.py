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

import sys
import os
import time
import rss
import tiny
import twitter

# CHANGE THIS
INTERVALO=TIME TO WAIT BETWEEN POST IF THERES MORE THAN ONE TO POST
LOG='PLACE OF YOUR LOG FILE'
PIPE='URL OF RSS FILE'
# DONT CHANGE ANYTHING AFTER THIS

def main():
	items = rss.getRSS(PIPE)
	
	try:
		ficheiro = open(LOG,'r')
	except IOError:
		ficheiro = open(LOG,'a')
		
	logs = ficheiro.readlines()
	ficheiro.close()
	j=len(items)-1
	
	if (len(items) > 2):
		j=2	
	
	for r in range(j+1):
		segue = 1
		for url in logs:
			if (url == items[j]['link']+"\n"):
				print "rss repetido: "+url
				segue = 0
				break
		
		if segue:
			tinie = tiny.tinyGet(items[j]['link'])
			if (len(tinie) + len(items[j]['titulo']) > 118):
				lit = len(items[j]['titulo'])
				lti = len(tinie)
				items[j]['titulo'] = items[j]['titulo'][0:(115-lti)]+"..."
			post = items[j]['titulo']+" "+tinie
			print post
			twitter.sendTwitter(post)
		
			ficheiro = open(LOG,'a')
			ficheiro.write(items[j]['link']+"\n")
			ficheiro.close
		
		j = j-1
		
		
		time.sleep(INTERVALO)


if __name__ == '__main__':
	main()

