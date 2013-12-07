from functools import partial
import requests as r
import json

# DOESN'T BELONG HERE, import from 'helpers.py'

from lxml import etree
from lxml.cssselect import CSSSelector

def find(selector, content):
	""" Select elements from the DOM, like in jQuery.

	Example:
	>>> find('h1 a#link', '<h1><a id="link">Something</a></h1>')
	"""

	# Find should work on both HTML strings
	# and parsed lxml nodes.
	if type(content) == str:
		content = etree.HTML(content)

	return CSSSelector(selector)(content)

def find_one(selector, content):
	""" Same as `find` just for one element.
	"""
	elements = find(selector, content)
	return elements[0]

# </belong>

def Newest(pages=10):
	""" Crawls this page: http://www.time.mk/n/all
	and yields links to news.
	"""
	pages = min(pages, 10)
	for page in xrange(1, pages + 1):
		response = r.get('http://www.time.mk/n/all/%s' % page)
		paragraphs = find('div.cluster', response.text.encode('utf8'))
		for p in paragraphs:
			yield 'http://time.mk/' + find_one('h1 a', p).get('href')
