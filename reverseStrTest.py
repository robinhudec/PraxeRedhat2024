#!/usr/bin/python3
import unittest
import reverseStr

class reverseStrTest(unittest.TestCase):
    def testAbcd(self):
        self.assertEqual(reverseStr.reverseStr("abc"), "cba")

    def testSpace(self):
        self.assertEqual(reverseStr.reverseStr("a b"), "b a")
    
    def testInt(self):
        self.assertEqual(reverseStr.reverseStr(12), "21")

    def testBool(self):
        self.assertEqual(reverseStr.reverseStr(True), "eurT")

    def testBlank(self):
        self.assertEqual(reverseStr.reverseStr(""), "")

    def testNot(self):
        self.assertNotEqual(reverseStr.reverseStr(12), "2")



if __name__ == '__main__':
    unittest.main()

