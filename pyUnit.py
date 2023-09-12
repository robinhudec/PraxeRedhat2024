import unittest
import factorial

class Testing(unittest.TestCase):
    def test5(self):
        self.assertEqual(factorial.fact(5), 120)
    
    def test4(self):
        self.assertEqual(factorial.fact(4), 24)

if __name__ == '__main__':
    unittest.main()



