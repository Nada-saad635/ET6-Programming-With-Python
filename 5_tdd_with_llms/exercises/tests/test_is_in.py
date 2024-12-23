import unittest
from ..is_in import is_in

class TestIsIn(unittest.TestCase):
    
    def test_in_first_list(self):
        """Test case where the string is in the first list only."""
        self.assertTrue(is_in("Nada", ["Nada", "Aree"], ["bees", "Nada"]))

    def test_in_second_list(self):
        """Test case where the string is in the second list only."""
        self.assertTrue(is_in("book", ["pen", "pencil"], ["bees", "book"]))

    def test_in_both_lists(self):
        """Test case where the string is in both lists."""
        self.assertTrue(is_in("Nada", ["Nada", "Aree"], ["Nada", "bees"]))

    def test_in_neither_list(self):
        """Test case where the string is in neither list."""
        self.assertFalse(is_in("apple", ["Nada", "Aree"], ["bees", "Nada"]))

    def test_empty_lists(self):
        """Test case where both lists are empty."""
        self.assertFalse(is_in("Nada", [], []))

    def test_invalid_input_text(self):
        """Test case for invalid text input."""
        with self.assertRaises(AssertionError):
            is_in(123, ["Nada", "Aree"], ["bees", "Nada"])  # text is not a string

    def test_invalid_input_list1(self):
        """Test case for invalid list1 input."""
        with self.assertRaises(AssertionError):
            is_in("Nada", "Not a list", ["bees", "Nada"])  # list1 is not a list

    def test_invalid_input_list2(self):
        """Test case for invalid list2 input."""
        with self.assertRaises(AssertionError):
            is_in("Nada", ["Nada", "Aree"], "Not a list")  # list2 is not a list

if __name__ == "__main__":
    unittest.main()
