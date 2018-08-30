import unittest
import os
from mnist import Mnist


class TestMnist(unittest.TestCase):
    """ Tests ... """

    def setUp(self):
        self._mnist = Mnist(os.path.join(os.path.dirname(__file__), 'resources/mnist.csv'))

    def tearDown(self):
        pass

    def test_load_data(self):
        """
        Test case for ...
        """
        assert len(self._mnist.get()) == 10
        assert self._mnist.get()[0].label == 7
        pass

    def test_rand(self):
        """
        Test case for ...
        """
        assert len(self._mnist.random()[:5]) == 5
        pass


if __name__ == '__main__':
    unittest.main()
