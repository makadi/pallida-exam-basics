import unittest
import unique_chars


class Alltest(unittest.TestCase):

    def test_unique_chars(self):
        self.assertEqual(unique_chars.unique_characters("baaaanagram"), ['b', 'a', 'n', 'g', 'r', 'm'])
    
    def test_not_enought_chars(self):
        self.assertNotEquals(unique_chars.unique_characters("banaagram"), ['a', 'n', 'g', 'r', 'm'])

    def test_upper_or_lower(self):
        self.assertNotEquals(unique_chars.unique_characters("baaaanagram"), ['B', 'A', 'N', 'G', 'R', 'M'])

if __name__ == '__main__':
    unittest.main()