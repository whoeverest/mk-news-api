import requests as r
import json
import codecs
from lxml import etree
from lxml.cssselect import CSSSelector

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

new_clusters = {}

clusters = select['clusters'](html)

for cluster in clusters:
    title_el = select['title'](cluster)[0]
    title = title_el.text
    time_url = title_el.get('href')
    snippet = select['text'](cluster)[0].text
    source = select['source'](cluster)[0].text
    when = select['when'](cluster)
    if when:
        when = when[0].text
    else:
        when = select['when_now'](cluster)[0].text
    new_clusters['http://time.mk/' + time_url] = {
        'title': title,
        'snippet': snippet,
        'source': source,
        'when': when
    }

print json.dumps(new_clusters, ensure_ascii=False, indent=4).encode('utf8')
