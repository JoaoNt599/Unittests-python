from baconwitheggs import bacon_with_eggs

import unittest


class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs_must_get_up_assertionerror_if_not_to_receive_int(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('')

    def test_bacon_with_eggs_must_return_bacon_with_eggs_if_entry_multiple_of_3_and_5(self):
        entrys = (15, 30, 45, 60)
        output = 'bacon with eggs'

        for entry in entrys:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(
                    bacon_with_eggs(entry),
                    output,
                    msg=f'"{entrys}" entry not return "{output}"'
                )

    def test_bacon_with_eggs_must_return_bacon_if_entry_is_multiple_only_3(self):
        entrys = (3, 6, 9, 6, 12, 18, 21)
        output = 'bacon'

        for entry in entrys:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(
                    bacon_with_eggs(entry),
                    output,
                    msg=f'"{entrys}" entry not return "{output}"'
                )

    def test_bacon_with_eggs_must_return_eggs_if_entry_is_multiple_only_5(self):
        entrys = (5, 10, 20, 25, 35)
        output = 'eggs'

        for entry in entrys:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(
                    bacon_with_eggs(entry),
                    output,
                    msg=f'"{entrys}" entry not return "{output}"'
                )

    def test_bacon_with_eggs_must_return_get_hungry_if_entry_not_multiple_of_3_and_5(self):
        entrys = (1, 2, 4, 7, 8)
        output = 'get hungry'

        for entry in entrys:
            with self.subTest(entry=entry, output=output):
                self.assertEqual(
                    bacon_with_eggs(entry),
                    output,
                    msg=f'"{entrys}" entry not return "{output}"'
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
