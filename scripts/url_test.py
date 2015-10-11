from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import date
import requests

# setting default date time to use for fuzzy comparison
default_dt = date(1980, 1, 1)

# scrape url and read into variable
r = requests.get('http://www.japanblockfair.com')
html = r.text

# initiate html parser
soup = BeautifulSoup(html, "html.parser")

# loop thru each child html tags
tags = soup.body.descendants
for t in tags:

    # if there there is something and ti's not empty~ish
    if t.string and t.string.rstrip():
        try:
            guess = parse(t.string, fuzzy=True, default=default_dt)
            if guess:
                if not guess.year == default_dt.year:
                    print 'original: [%s]\nguess: [%s]\n===\n' % (t.string,
                                                                  repr(guess))
        except:
            print 'error with t.string, see [%s]\n===\n' % t.string
