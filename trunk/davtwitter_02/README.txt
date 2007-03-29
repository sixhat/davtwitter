DavTwitter - An River Creator for www.twitter.com from an RSS stream
author	: David Rodrigues david.rodrigues@gmail.com
site 	: http://code.google.com/p/davtwitter/

REQUIREMENTS:

* Python
* Universal Feedparser from Dave Winer
  http://feedparser.org/

INSTALL

The install process is preaty strightforward:

1.	Verify that you have python
2.	Install Feedparser
2.1	After downloading Feedparser navigate to the extracted folder
	and run

	python setup.py install

3.	Change the files 

		davtwitter.py
		twitter.py

	betwwen the 

		# CHANGE THIS
		# DON'T CHANGE ANYTHING AFTER THIS	

	acording to your setup acounts at twitter and the RSS you want to pull

4.	create a cronjob that runs davtwitter.py every so often...

	example:

	10,40 * * * * root /usr/bin/python /home/yourUser/twiter/davtwitter.py

	This would run the script every 30 min ...

5.	Enjoy
