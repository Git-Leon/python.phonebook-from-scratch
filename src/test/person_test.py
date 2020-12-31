# Created by Leon Hunter at 11:23 AM 10/24/2020
from unittest import TestCase

from src.main.person import Person


class PersonTest(TestCase):
    def _test(self, object_to_test, value_sets):
        for value_set in value_sets:
            # given
            setter_method = value_set[0]
            getter_method = value_set[1]
            set_value = value_set[2]
            expected_value = value_set[3]
            current_value = getter_method()
            self.assertNotEqual(current_value, expected_value)

            # when
            actual_value = setter_method(set_value)

            # then
            self.assertEquals(actual_value, expected_value)


    def test_set_first_name(self):
        person = Person()
        self._test(person, [
            (person.set_first_name, person.get_first_name, "Leon", "Leon"),
            (person.set_first_name, person.get_first_name, "Christopher", "Christopher"),
            (person.set_first_name, person.get_first_name, "Hunter", "Hunter"),
        ])

    def test_set_last_name(self):
        person = Person()
        self._test(person, [
            (person.set_last_name, person.get_last_name, "Leon", "Leon"),
            (person.set_last_name, person.get_last_name, "Christopher", "Christopher"),
            (person.set_last_name, person.get_last_name, "Hunter", "Hunter"),
        ])