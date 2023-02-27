import unittest

def convert(f):
    return (f - 32)*(5 / 9)

class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(convert(32), 10)

if __name__ == '__main__':
    unittest.main()