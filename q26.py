import unittest

def name(x):
    return x

class myName(unittest.TestCase):
    def test(self):

        self.assertEqual(name("MIGUEL"),"MIGUEL")

if __name__ == '__main__':

    unittest.main()

print(name)