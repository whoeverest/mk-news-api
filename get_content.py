import requests as r
import justext
import sys
import json
from datetime import datetime

def extract_content(text, **kwargs):
    potential_paragraphs = justext.justext(
        text.encode('utf8'),
        justext.get_stoplist('Macedonian'),
        encoding='utf8',
        length_low=70,
        length_high=180,
        max_link_density=0.2)

    paragraphs = []
    title = { 'word_count': 0, 'text': None }

    for p in potential_paragraphs:
        if p['class'] != 'good':
            continue
        if p['heading'] == False:
            paragraphs.append(p['text'])
        if (p['heading'] == True) and (p['word_count'] > title['word_count']):
            title = p

    return {
        'title': title['text'],
        'paragraphs': paragraphs
    }

def candidates(response):
    """ Requests library sometimes can't figure out the
    right encoding, so we iterate to find the best match
    (one that actually has paragraphs etc.)
    """
    candidates = []
    for enc in ['utf-8', 'cp1251', 'iso-8859-1']:
        response.encoding = enc
        candidates.append(extract_content(response.text))
    return candidates

def best_candidate(candidates):
    """ This should be way more sophisticated.
    """
    for cand in candidates:
        if cand['paragraphs']:
            return cand
    return candidates[0]

def content(url):
    res = r.get(url)
    content = best_candidate(candidates(res))
    content['url'] = res.url
    content['timestamp'] = datetime.now().isoformat()
    return content


if __name__ == "__main__":
    print(json.dumps(content(sys.argv[1]), indent=4, ensure_ascii=False))

    """
    [('stopword_count', 0), ('linked_char_count', 0), ('text', '25.11.2013 13:43:22'),
    ('cfclass', 'short'), ('text_nodes', ['25.11.2013 13:43:22']), ('word_count', 2),
    ('link_density', 0.0), ('class', 'bad'), ('dom_path', 'html.body.div.div.div.div'),
    ('stopword_density', 0.0), ('heading', False), ('tag_count', 1)]
    """
