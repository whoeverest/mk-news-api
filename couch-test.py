import couchdbkit as cdbk
import restkit
from datetime import datetime

server = cdbk.Server('http://88.80.185.91:5984',
	filters=[restkit.BasicAuth('andrej', 'zx-1001')])
db = server.get_db('news')

class News(cdbk.Document):
		url = cdbk.StringProperty()
		status = cdbk.StringProperty()

News.set_db(db)

from crawlers.time_newest import TimeNewest
from get_content import content
import json

contents = {}

for i, url in enumerate(TimeNewest()):
	print url
	News(url=url, status='new').save()

print json.dumps(contents, ensure_ascii=False, indent=4).encode('utf8')
