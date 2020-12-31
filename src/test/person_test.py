# Created by Leon Hunter at 11:23 AM 10/24/2020
from numbers import Number
from unittest import TestCase

from src.main.person import Person


class PersonTest(TestCase):
    def _test(self, method_to_test, value_sets):
        for value_set in value_sets:
            # given
            input_value = value_set[0]
            expected_calculation = value_set[1]

            # when
            actual_calculation = method_to_test(input_value)

            calculation_error_message = '''
            first_value = {}
            expected_calculation = {}
            actual_calculation = {}
            '''.format(input_value, expected_calculation, actual_calculation)

            return_type_error_message = '''
            expected return value of `{}` to be of type `str`
            instead was of type `{}`
            '''.format(method_to_test.__name__, type(actual_calculation))

            # then
            self.assertTrue(isinstance(actual_calculation, str), return_type_error_message)
            self.assertAlmostEqual(expected_calculation, actual_calculation, calculation_error_message)

    def test_set_first_name(self):
        self._test(Person().set_first_name, [
            ("Leon", "Leon"),
            ("Christopher", "Christopher"),
            ("Hunter", "Hunter"),
        ])
