#!/usr/bin/python3
import unittest
import trojuhelnik

class trojuhelnikTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(trojuhelnik.triangleArea(5, 3, 5.83), 7.499999486624983)



if __name__ == '__main__':
    unittest.main()
