import unittest
from app.models import User
from app.utils import check_number_format, find_bad_bmis


class MySimpleProjectTests(unittest.TestCase):

    def setUp(self):
        # This runs before every test
        self.test_user = User("Nurasyl", 1.80)

    # Test 1: Check if object creates correctly
    def test_user_data(self):
        self.assertEqual(self.test_user.name, "Nurasyl")
        self.assertEqual(self.test_user.height, 1.80)

    # Test 2: Check if BMI math works fine
    def test_bmi_math(self):
        self.test_user.add_new_weight(81.0)
        self.assertEqual(len(self.test_user.history), 1)
        # BMI = 81 / (1.8 * 1.8) = 25.0
        self.assertEqual(self.test_user.history[0]["bmi"], 25.0)

    # Test 3: Check if regex accepts correct format
    def test_regex_good_input(self):
        self.assertTrue(check_number_format("65.4"))

    # Test 4: Check if regex blocks text characters
    def test_regex_bad_input(self):
        self.assertFalse(check_number_format("abc"))

    # Test 5: Check if lambda and filter work
    def test_functional_filters(self):
        self.test_user.add_new_weight(60.0)  # Normal BMI
        self.test_user.add_new_weight(100.0)  # High BMI
        bad_results = find_bad_bmis(self.test_user.history)
        self.assertEqual(len(bad_results), 1)


if __name__ == "__main__":
    unittest.main()