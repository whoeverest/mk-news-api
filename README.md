## An API for MK news

The idea of this project is, at the end, to provide a set of tools for discovering and parsing news from Macedonian sources. Currently, the news are pulled from Time.mk's "Newewst" feed and are parsed with the "Justext" library.

### Install

	pip install lxml
	pip install requests

	svn checkout http://justext.googlecode.com/svn/trunk/ justext-read-only
	cd justext-read-only
	python setup.py install

### Usage

Show recent news:

	python get_newest.py

Get page contents:

	python get_content.py http://someurl.com/news?id=123
