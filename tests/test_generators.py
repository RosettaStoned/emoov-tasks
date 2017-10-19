import sys

sys.path.append('../')
sys.path.append('../../')

import unittest
import itertools
from src.generators import chain, compress, cycle

class TestGenerators(unittest.TestCase):

    def setUp(self):
        pass

    def test_chain(self):

        my_chain = list(chain.chain(range(0, 4), range(4, 8)))
        othr_chain = list(itertools.chain(range(0, 4), range(4, 8)))
        self.assertEqual(my_chain, othr_chain)

    def test_compress(self):

        my_compress = list(compress.compress(["Dimitar", "Rostislav", "emoov"], [False, False, True]))
        othr_compress = list(itertools.compress(["Dimitar", "Rostislav", "emoov"], [False, False, True]))
        self.assertEqual(my_compress, othr_compress)

if __name__ == '__main__':
    unittest.main()

