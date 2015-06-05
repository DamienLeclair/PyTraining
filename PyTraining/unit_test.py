__author__ = 'dleclair'

import random
import unittest

class RandomTest(unittest.TestCase):

    def setUp(self):
        self.list = list(range(10))

    def test_choice(self):
        elt = random.choice(self.list)
        self.assertIn(elt, self.list)

    def test_shuffle(self):
        random.shuffle(self.list)
        self.list.sort()
        self.assertEqual(self.list, list(range(10)))

    def test_sample(self):
        subset = random.sample(self.list, 5)
        for element in subset:
            self.assertIn(element, self.list)

        with self.assertRaises(ValueError):
            random.sample(self.list, 20)