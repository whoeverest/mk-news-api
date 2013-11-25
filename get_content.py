import requests as r
import justext
import sys
import json

def extract_content(text):
    potential_paragraphs = justext.justext(
        res.text.encode('utf8'),
        justext.get_stoplist('Macedonian'),
        encoding='utf8',
        length_low=70,
        length_high=180,
        max_link_density=0.2)

    paragraphs = []
    title = { 'word_count': 0 }

    for p in potential_paragraphs:
        if p['class'] != 'good':
            continue
        if p['heading'] == False:
            paragraphs.append(p['text'])
        if (p['heading'] == True) and (p['word_count'] > title['word_count']):
            title = p

    return {
        'url': url,
        'title': title['text'],
        'paragraphs': paragraphs
    }

url = sys.argv[1]
res = r.get(url)

for enc in ['utf-8', 'cp1251', 'iso-8859-1']:
    res.encoding = enc
    content = extract_content(res.text)
    if content['paragraphs']:
        print json.dumps(content, indent=4, ensure_ascii=False)
        break

"""
[('stopword_count', 0), ('linked_char_count', 0), ('text', '25.11.2013 13:43:22'),
('cfclass', 'short'), ('text_nodes', ['25.11.2013 13:43:22']), ('word_count', 2),
('link_density', 0.0), ('class', 'bad'), ('dom_path', 'html.body.div.div.div.div'),
('stopword_density', 0.0), ('heading', False), ('tag_count', 1)]
"""
