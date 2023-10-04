import unittest

def area(length):
    return length * length

def perimeter (length):
    return length *4

class myTest(unittest.TestCase):
    def test(self):

        self.assertEqual(area(5),25)
        self.assertEqual(perimeter(5),20)

if __name__ == '__main__':

    unittest.main()
