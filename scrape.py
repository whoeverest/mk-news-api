import json
import requests as r
import mongoengine as m
from concurrent.futures import ThreadPoolExecutor

from get_newest import get_news
from get_content import content

m.connect('time_news')

class Paragraph(m.EmbeddedDocument):
	text = m.StringField()

class News(m.Document):
	url = m.StringField(required=True, unique=True)
	title = m.StringField()
	paragraphs = m.ListField(m.EmbeddedDocumentField(Paragraph))
	timestamp = m.DateTimeField()

def save_news(url):
	print('saving', url)
	news = content(url)
	n = News()
	n.url = news['url']
	n.title = news['title']
	n.timestamp = news['timestamp']
	n.paragraphs = map(lambda t: Paragraph(text=t), news['paragraphs'])
	n.save()

def save_news(url):
	print(content(url))

with ThreadPoolExecutor(max_workers=1) as pool:
	for res in pool.map(save_news, get_news()):
		print(res)
	# print(pool.results())

# print(json.dumps(news_contents, indent=4, ensure_ascii=False))
