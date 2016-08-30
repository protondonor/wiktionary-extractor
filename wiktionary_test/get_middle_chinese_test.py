# coding=utf-8
import unittest
from wiktionary.get_middle_chinese import get_middle_chinese_for_character


class GetMiddleChineseWordTest(unittest.TestCase):
    def test_get_middle_chinese_for_character(self):
        middle_chinese_reading = get_middle_chinese_for_character(u'字')

        self.assertIsNotNone(middle_chinese_reading)

        self.assertEqual(u'd͡zɨᴴ', middle_chinese_reading)

    def test_get_middle_chinese_for_character_no_character(self):
        self.assertEqual(u'', get_middle_chinese_for_character('brompheniramine'))

    def test_get_middle_chinese_for_character_shinjitai(self):
        middle_chinese_reading = get_middle_chinese_for_character(u'両')

        self.assertIsNotNone(middle_chinese_reading)

        self.assertEqual(u'lɨɐŋˣ', middle_chinese_reading)

    def test_get_middle_chinese_multiple_middle_chinese_readings(self):
        middle_chinese_reading = get_middle_chinese_for_character(u'列')

        self.assertIsNotNone(middle_chinese_reading)

        self.assertEqual(u'ʈɨo , liᴇt̚', middle_chinese_reading)
