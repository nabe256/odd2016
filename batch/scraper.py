import requests
from HTMLParser import HTMLParser

target_url = 'https://www.snowlove.net/snowfall.php'
target_html = requests.get(target_url).text
print target_html
