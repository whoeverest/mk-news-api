from crawlers.time import Newest
from get_content import content
import json

contents = {}

for i, url in enumerate(Newest()):
	contents[url] = content(url)
	if i > 10:
		break

print json.dumps(contents, ensure_ascii=False, indent=4).encode('utf8')
