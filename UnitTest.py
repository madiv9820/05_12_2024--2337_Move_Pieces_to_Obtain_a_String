from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ('_L__R__R_', 'L______RR', True),
                            2: ('R_L_', '__LR', False),
                            3: ('_R', 'R_', False)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        start, target, output = self.__testCases[1]
        result = self.__obj.canChange(start = start, target = target)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        start, target, output = self.__testCases[2]
        result = self.__obj.canChange(start = start, target = target)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_3(self):
        start, target, output = self.__testCases[3]
        result = self.__obj.canChange(start = start, target = target)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()