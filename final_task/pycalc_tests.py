import unittest
import pycalc


class pycalc_test(unittest.TestCase):
    def test_searching_for_constants(self):
        self.assertEqual(pycalc.searching_for_constants(
            ['e', '+', 'pi']),
            ['2.718281828459045', '+', '3.141592653589793'])
        self.assertEqual(pycalc.searching_for_constants(
            ['tau', '-', 'inf', '+', 'nan']),
            ['6.283185307179586', '-', 'inf', '+', 'nan'])

    def test_merging_pluses_and_minuses(self):
        self.assertEqual(pycalc.merging_pluses_and_minuses('3+---++-++-4'), '3-4')
        self.assertEqual(pycalc.merging_pluses_and_minuses('++4--4'), '+4+4')

    def test_positive_and_negative(self):
        self.assertEqual(pycalc.positive_and_negative(['-', '4']), ['-4.0'])


if __name__ == '__main__':
    unittest.main()
