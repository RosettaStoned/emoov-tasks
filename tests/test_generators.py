import itertools
from src.generators import chain, compress, cycle

class TestGenerators(unittest.TestCase):

    def setUp(self):
        pass

    def test_chain(self):
        self.assertEqual(list(chain.chain(range(0, 4), range(4, 8))), list(chain(range(0, 4), range(4, 8)))) 

    def test_compress(self):
        self.assertEqual(list(compress.compress(["Dimitar", "Rostislav", "emoov"], [False, False, True])), list(compress(["Dimitar", "Rostislav", "emoov"], [False, False, True])))

if __name__ == '__main__':
    unittest.main()

