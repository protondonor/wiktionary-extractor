# coding=utf-8
from bs4 import BeautifulSoup

from wiktionary.get_html_for_word import get_html_for_word


def get_middle_chinese_for_character(character):
    html_string = get_html_for_word(character)
    html_soup = BeautifulSoup(html_string, "html.parser")
    middle_chinese_link = html_soup.find("a", {"title": "w:Middle Chinese"})
    if middle_chinese_link is not None:
        ipa_span = middle_chinese_link.parent.find("span", {"class": "IPA"})
        ipa_text = ipa_span.contents[0].replace('/', '').replace(', ', ' , ')
        ipa_span_sup = ipa_span.find("sup")
        if ipa_span_sup is not None:
            if ipa_span_sup.string == 'H':
                ipa_text += u'ᴴ'
            elif ipa_span_sup.string == 'X':
                ipa_text += u'ˣ'
        return ipa_text
    else:
        try:
            traditional_chinese = html_soup.find(text="For pronunciation and definitions of").parent.parent.find("a")\
                .string
            return get_middle_chinese_for_character(traditional_chinese)
        except AttributeError:
            try:
                traditional_chinese = html_soup.find("table", class_="wikitable floatright").find(
                    "a", {"title": "wikipedia:Traditional Chinese"}).next_element.next_element.next_element.text
                middle_chinese_reading = get_middle_chinese_for_character(traditional_chinese)
                if middle_chinese_reading == u'':
                    simplified_chinese = html_soup.find("table", class_="wikitable floatright").find(
                        "a", {"title": "wikipedia:Simplified Chinese"}).next_element.next_element.next_element.text
                    middle_chinese_reading = get_middle_chinese_for_character(simplified_chinese)
                return middle_chinese_reading
            except AttributeError:
                try:
                    simplified_chinese = html_soup.find("a", text="simp.").next_element.next_element.next_element.text
                    return get_middle_chinese_for_character(simplified_chinese)
                except AttributeError:
                    return u''
