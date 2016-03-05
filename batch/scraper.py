import json
import lxml.html
import requests


def get_json_skiingrun():
    target_url = 'https://www.snowlove.net/snowfall.php'

    target_html = requests.get(target_url).text
    roots = lxml.html.fromstring(target_html)
    skiingrun_list = []
    for root in roots.cssselect('dt a'):
        skiingrun_list.append({'skiingrun': root.text})  # スキー場名以外Noneだった

    return json.dumps(skiingrun_list)
