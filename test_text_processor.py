import unittest
from text_processor import TextProcessor


class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        self.t1 = "Hello, World!"
        self.t2 = "123 ABC!!!"
        self.t3 = "this is a test"
        self.t4 = "hello world"
        self.proc1 = TextProcessor(self.t1)
        self.proc2 = TextProcessor(self.t2)
        self.proc3 = TextProcessor(self.t3)
        self.proc4 = TextProcessor(self.t4)

    def test_clean_text_removes_non_alpha_characters(self):
        self.proc1.clean_text()
        self.assertEqual(self.proc1.cleaned_text, "hello world")

    def test_clean_text_lowercase_conversion(self):
        self.proc2.clean_text()
        self.assertEqual(self.proc2.cleaned_text, "abc")

    def test_clean_text_empty_string(self):
        empty_processor = TextProcessor("")
        empty_processor.clean_text()
        self.assertEqual(empty_processor.cleaned_text, "")

    def test_remove_stop_words(self):
        self.proc3.clean_text()
        self.proc3.remove_stop_words(['this', 'is'])
        self.assertEqual(self.proc3.cleaned_text, "a test")

    def test_remove_stop_words_clean_text_not_called(self):
        self.proc4.remove_stop_words([])
        self.assertEqual(self.proc4.cleaned_text, "hello world")

    def test_remove_stop_words_no_stop_words(self):
        self.proc4.clean_text()
        self.proc4.remove_stop_words([])
        self.assertEqual(self.proc4.cleaned_text, "hello world")


if __name__ == '__main__':
    unittest.main()
