# coding=utf-8
import json
import requests


def get_html_for_word(word):
    url_template = u"https://en.wiktionary.org/w/api.php?action=parse&page={word}&contentmodel=wikitext&format=json"
    template_replaced = url_template.format(**locals())
    wiktionary_api_response_raw_json = requests.get(template_replaced).content
    wiktionary_api_response = json.loads(wiktionary_api_response_raw_json)
    return wiktionary_api_response["parse"]["text"][u'*']
