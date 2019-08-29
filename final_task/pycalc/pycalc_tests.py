import unittest
import pycalc.pycalc as pycalc
import pycalc.Data as Data


class MainModuleTest(unittest.TestCase):
    """Tests for functions of python.py"""
    @classmethod
    def setUpClass(cls) -> None:
        print('Functions of main module: ')

    def test_pycalc(self):
        self.assertTrue(pycalc.pycalc('----').startswith('ERROR:'))
        self.assertTrue(pycalc.pycalc('log').startswith('ERROR:'))
        self.assertTrue(pycalc.pycalc('()(((((())').startswith('ERROR:'))
        self.assertEqual(pycalc.pycalc('3^1^2'), 3)
        self.assertEqual(pycalc.pycalc('sin(pi/2)'), 1)

    def test_searching_for_constants(self):
        self.assertEqual(pycalc.searching_for_constants(
            ['e', '+', 'pi']),
            ['2.718281828459045', '+', '3.141592653589793'])
        self.assertEqual(pycalc.searching_for_constants(
            ['tau', '-', 'inf', '+', 'nan']),
            ['6.283185307179586', '-', 'inf', '+', 'nan'])

    def test_merging_pluses_and_minuses(self):
        self.assertEqual(pycalc.merging_pluses_and_minuses(list('3+---++-++-4')), list('3-4'))
        self.assertEqual(pycalc.merging_pluses_and_minuses(list('++4--4')), list('+4+4'))

    def test_positive_and_negative(self):
        self.assertEqual(pycalc.positive_and_negative(['-', '4']), ['-4.0'])

    def test_raising_a_power(self):
        self.assertEqual(pycalc.raising_a_power(['2', '^', '3']), ['8.0'])

    def test_inclusion_in_general_expression(self):
        self.assertEqual(
            pycalc.inclusion_in_general_expression(['2', '*', '(', '1', '+', '2', ')'], ['3'], 2, 6),
            ['2', '*', '3.0'])

    def test_calculating_expression_in_brackets(self):
        self.assertEqual(pycalc.calculating_expression_in_brackets(list('2^2^(6/3)')), ['2', '^', '2', '^', '2.0'])


class DataModuleTest(unittest.TestCase):
    """Tests for functions of Data.py"""
    @classmethod
    def setUpClass(cls) -> None:
        print('Functions of data module: ')

    def test_addition(self):
        self.assertEqual(Data.addition(3.0, 4.0), 7.0)

    def test_subtraction(self):
        self.assertEqual(Data.subtraction(7.0, 4.0), 3.0)

    def test_multiplication(self):
        self.assertEqual(Data.multiplication(3.0, 4.0), 12.0)

    def test_division(self):
        self.assertEqual(Data.division(12.0, 3.0), 4.0)

    def test_whole_division(self):
        self.assertEqual(Data.whole_division(11.0, 3.0), 3.0)

    def test_division_with_remainder(self):
        self.assertEqual(Data.division_with_remainder(11.0, 3.0), 2.0)

    def test_less(self):
        self.assertEqual(Data.less(1.0, 3.0), True)
        self.assertEqual(Data.less(3.0, 3.0), False)

    def test_less_or_equal(self):
        self.assertEqual(Data.less_or_equal(3.0, 3.0), True)
        self.assertEqual(Data.less_or_equal(3.0, 4.0), True)

    def test_greater(self):
        self.assertEqual(Data.greater(4.0, 3.0), True)
        self.assertEqual(Data.greater(3.0, 3.0), False)

    def test_greater_or_equal(self):
        self.assertEqual(Data.greater_or_equal(4.0, 3.0), True)
        self.assertEqual(Data.greater_or_equal(3.0, 3.0), True)

    def test_unequal(self):
        self.assertEqual(Data.unequal(4.0, 3.0), True)
        self.assertEqual(Data.unequal(3.0, 3.0), False)

    def test_equal(self):
        self.assertEqual(Data.equal(4.0, 3.0), False)
        self.assertEqual(Data.equal(3.0, 3.0), True)


if __name__ == '__main__':
    unittest.main()
