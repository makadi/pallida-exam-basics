import unittest
import unique_chars


class Alltest(unittest.TestCase):

    def test_unique_characters(self):
        self.assertEqual(unique_chars.unique_characters("banagram"), ['b', 'a', 'n', 'g', 'r', 'm'])
    
    def test_not_unique_characters(self):
        self.assertNotEquals(unique_chars.unique_characters("banagram"), ['a', 'n', 'g', 'r', 'm'])

    # def test_if(self):
    #     self.assertNotEquals(unique_chars.unique_characters(2), )


if __name__ == '__main__':
    unittest.main()