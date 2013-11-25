## An API for MK news

The idea of this project is, at the end, to provide a set of tools for discovering and parsing news from Macedonian sources. Currently, the news are pulled from Time.mk's "Newest" feed and are parsed with the "Justext" library.

### Install

	pip install lxml
	pip install requests

	svn checkout http://justext.googlecode.com/svn/trunk/ justext-read-only
	cd justext-read-only
	python setup.py install

	git clone https://github.com/whoeverest/mk-news-api.git

### Usage

Show recent news:

	python get_newest.py

```json
{
    "http://time.mk/r/56ba75af71/6cd61e7469/": {
        "snippet": "Дваесет и двегодишната Худа ал Ниран од Саудиска Арабија во Јемен, пркосејќи им на правилата на двете конзервативни држави, го повика јеменскиот суд да и дозволи да остане во државата и да се омажи ...", 
        "source": "А1 On", 
        "when": " тукушто објавено", 
        "title": "ФОТО: „Јулија“ од Саудиска Арабија сака да се омажи за „Ромео“ од Јемен"
    }, 
    "http://time.mk/r/9070799625/7811c5578d/": {
        "snippet": "Вчера и завчера вистински хит беше видеото на Јутјуб на кое се гледа како Наумче Мојсовски навива за белградски Партизан на кошаркарскиот меч со Фенербахче, што наиде на остра реакција, особено кај ...", 
        "source": "МКД", 
        "when": " тукушто објавено", 
        "title": "Комити со специјална порака за верниот партизановец Мојсовски (ФОТО)"
    }, [...]
```

Get page contents:

	python get_content.py http://www.utrinski.mk/?ItemID=1260FBFBE2333242A272C66B78B9D1BF


```json
{
    "url": "http://www.utrinski.mk/?ItemID=1260FBFBE2333242A272C66B78B9D1BF", 
    "paragraphs": [
        "Од април идната година македонските граѓани со „Визер“ ќе можат да летаат на уште три нови дестинации - Париз, Брисел и Франкфурт. Ова денеска го најави премиерот Никола Груевски, кој истакна дека со „Визер“ се договориле за уште три нови линии на кои граѓаните ќе можат да летаат по цени почнувајќи од 1.500 денари.", 
        "Владата го субвенционира авиопревозникот „Визер“ со по 8 евра по патник. Оваа година за нискобуџетните авиокомпании Владата доделуваше по 9 евра за секој патник, за идната цената на субвенцијата ќе биде 8 евра. (Ек.Р.)"
    ], 
    "title": null
}

```

It's not perfect, but it's a start.