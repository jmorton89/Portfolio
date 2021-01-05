from ptest import rearrange
import unittest

class TestPtest(unittest.TestCase):
    def test1(self):
        testcase = "Morton, Joel"
        expected = "Joel Morton"
        self.assertEqual(rearrange(testcase), expected)
    def test2(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange(testcase), expected)
    def test3(self):
        testcase = "Morton, Joel R."
        expected = "Joel R. Morton"
        self.assertEqual(rearrange(testcase), expected)
    def test4(self):
        testcase = "Joel"
        expected = "Joel"
        self.assertEqual(rearrange(testcase), expected)
    def test5(self):
        self.assertRaises(TypeError, rearrange, "name", 1)
unittest.main()