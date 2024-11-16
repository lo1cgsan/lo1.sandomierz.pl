AUTHOR = 'Robert Bednarz'
SITENAME = 'I LO Colegium Gostomianum w Sandomierzu'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DEFAULT_CATEGORY = 'informacja'

ARTICLE_PATHS = ['articles',]
ARTICLE_URL = 'articles/{slug}_{rok}.html'
ARTICLE_SAVE_AS = 'articles/{slug}_{rok}.html'


MENUITEMS = ( 
    ('Archiwum', '/'),
    ('Działania', '/dzialania'),
    ('Olimpiady', '/olimpiady'),
    ('Szkoła', '/szkola'),
)