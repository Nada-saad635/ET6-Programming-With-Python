import unittest
from ..is_in_both import is_in_both 
class TestIsInBoth(unittest.TestCase):
    def test_in_both_lists(self):
        """Test case where the string is in both lists."""
        self.assertTrue(is_in_both("Nada", ["Nada", "Aree"], ["bees", "Nada"] ), True)
    
    def test_not_in_both_lists(self):
        """Test case where the string is not in both lists."""
        self.assertFalse(is_in_both("lap", ["pen", "book"], ["bees", "Nada"]),False )
    
    def test_in_one_list_only(self):
        """Test case where the string is in one list but not the other."""
        self.assertFalse(is_in_both("pen", ["pen", "book"], ["Nada", "Aree"]),False)
    
    def test_empty_lists(self):
        """Test case where both lists are empty."""
        self.assertFalse(is_in_both("Nada", [], []))
    
    def test_text_not_in_either_list(self):
        """Test case where the string is not in either list."""
        self.assertFalse(is_in_both("apple", ["Nada", "Aree"], ["bees", "Nada"]))
    
    def test_invalid_input_text(self):
        """Test case for invalid text input."""
        with self.assertRaises(AssertionError):
            is_in_both(123, ["Nada", "Aree"], ["bees", "Nada"])  # text is not a string

    def test_invalid_input_list1(self):
        """Test case for invalid list1 input."""
        with self.assertRaises(AssertionError):
            is_in_both("Nada", "Not a list", ["bees", "Nada"])  # list1 is not a list

    def test_invalid_input_list2(self):
        """Test case for invalid list2 input."""
        with self.assertRaises(AssertionError):
            is_in_both("Nada", ["Nada", "Aree"], "Not a list")  # list2 is not a list

# Run the tests
if __name__ == "__main__":
    unittest.main()
