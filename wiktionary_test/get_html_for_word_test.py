# coding=utf-8
import unittest


class GetHtmlForWordTest(unittest.TestCase):
    def test_get_html_for_word(self):
        from wiktionary.get_html_for_word import get_html_for_word
        html_for_word = get_html_for_word("brompheniramine")

        self.assertIsNotNone(html_for_word)

        self.assertTrue("An <a href=\"/wiki/antihistamine\" title=\"antihistamine\">antihistamine</a> "
                        "<a href=\"/wiki/drug\" title=\"drug\">drug</a> of the <a href=\"/wiki/propylamine\" "
                        "title=\"propylamine\">propylamine</a> class." in html_for_word)

    def test_get_html_for_word_unicode(self):
        from wiktionary.get_html_for_word import get_html_for_word
        html_for_word = get_html_for_word("וואָרט")

        self.assertIsNotNone(html_for_word)

        self.assertTrue("From <span class=\"etylcleanup\"><span class=\"etyl\"><a href="
                        "\"https://en.wikipedia.org/wiki/Old_High_German_language\" class=\"extiw\" title="
                        "\"w:Old High German language\">Old High German</a></span></span> <i class=\"Latn mention\" "
                        "lang=\"goh\" xml:lang=\"goh\"><a href=\"/wiki/wort#Old_High_German\" title=\"wort\">wort</a>"
                        "</i>." in html_for_word)

