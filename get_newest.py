import requests as r
import json
import codecs
from lxml import etree
from lxml.cssselect import CSSSelector

def get_news():
    res = r.get('http://www.time.mk/n/all')
    html = etree.HTML(res.text)
    
    select = {
        'clusters': CSSSelector('div.cluster'),
        'title': CSSSelector('h1 a'),
        'text': CSSSelector('div.article_body p.snippet'),
        'source': CSSSelector('div.article_body a.source'),
        'when': CSSSelector('div.article_body span.when'),
        'when_now': CSSSelector('div.article_body span.when_now')
    }

    news = {}
    clusters = select['clusters'](html)

    for cluster in clusters:
        news_url = 'http://time.mk/' + select['title'](cluster)[0].get('href')
        news[news_url] = {
            'title': select['title'](cluster)[0].text,
            'snippet': select['text'](cluster)[0].text,
            'source': select['source'](cluster)[0].text,
            'when': when[0].text if select['when'](cluster) else select['when_now'](cluster)[0].text
        }
    
    return news

if __name__ == "__main__":
    news = get_news()
    print(json.dumps(news, ensure_ascii=False, indent=4).encode('utf8'))
