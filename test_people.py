"""
class People
    __init__
        name str
        surname str
        data obtained bool (start False)

    API:
        get_all_data -> method
            OK
            404

            data_will_be_True_if_successfully-obtained
"""

import unittest
from unittest.mock import patch
from People import People


class TestPeople(unittest.TestCase):
    def setUp(self):
        self.p1 = People('João', 'Vieira')
        self.p2 = People('Maria', 'Miranda')

    def test_people_attr_name_correct_value(self):
        self.assertEqual(self.p1.name, 'João')
        self.assertEqual(self.p2.name, 'Maria')

    def test_people_attr_name_is_str(self):
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p2.name, str)

    def test_people_attr_surname_correct_value(self):
        self.assertEqual(self.p1.surname, 'Vieira')
        self.assertEqual(self.p2.surname, 'Miranda')

    def test_people_attr_surname_is_str(self):
        self.assertIsInstance(self.p1.surname, str)
        self.assertIsInstance(self.p2.surname, str)

    def test_people_attr_data_obtained_start_false(self):
        self.assertFalse(self.p1.data_obtained)
        self.assertFalse(self.p2.data_obtained)

    def test_get_all_data_success_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'SUCCESSFULLY CONNECTED')
            self.assertTrue(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'SUCCESSFULLY CONNECTED')
            self.assertTrue(self.p2.data_obtained)

    def test_get_all_data_failed_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p2.data_obtained)

    def test_get_all_data_success_and_failed_sequential(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'SUCCESSFULLY CONNECTED')
            self.assertTrue(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'SUCCESSFULLY CONNECTED')
            self.assertTrue(self.p2.data_obtained)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p2.data_obtained)


if __name__ == '__main__':
    unittest.main(verbosity=2)
