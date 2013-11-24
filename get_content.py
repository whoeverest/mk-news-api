import requests as r
import justext
import sys
import json

url = sys.argv[1]

res = r.get(url)

potential_paragraphs = justext.justext(
	res.text.encode('utf8'),
	justext.get_stoplist('Macedonian'),
	length_low=70,
	length_high=200,
	max_link_density=0.2)

paragraphs = []
title = None

for p in potential_paragraphs:
	if p['class'] == 'good' and p['heading'] == False:
		paragraphs.append(p['text'])
	if p['class'] == 'good' and p['heading'] == True:
		print 'title', p['text']
		title = p['text']

print json.dumps({
	'url': url,
	'title': title,
	'paragraphs': paragraphs
}, ensure_ascii=False)
