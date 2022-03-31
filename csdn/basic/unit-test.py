from csdn.basic.SysDemo import abs
import unittest
class Test(unittest.TestCase):
    def test_Abs1(self):
        a = abs(-10)
        self.assertEqual(a, 10)
if __name__ == '__main__':
    unittest.main()