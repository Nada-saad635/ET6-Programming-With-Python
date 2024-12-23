import unittest
from ..is_in_one import is_in_one 
class TestIsInOne(unittest.TestCase):
    def test_in_one_list(self):
        """Test case where the string is in only one list."""
        self.assertTrue(is_in_one("book", ["pen", "book"], ["bees", "Nada"]))
    
    def test_in_both_lists(self):
        """Test case where the string is in both lists."""
        self.assertFalse(is_in_one("Nada", ["Nada", "Aree"], ["Nada", "bees"]))
    
    def test_in_neither_list(self):
        """Test case where the string is in neither list."""
        self.assertFalse(is_in_one("apple", ["Nada", "Aree"], ["bees", "Nada"]))
    
    def test_empty_lists(self):
        """Test case where both lists are empty."""
        self.assertFalse(is_in_one("Nada", [], []))
    
    def test_edge_case_empty_string(self):
        """Test case where the input string is empty."""
        self.assertFalse(is_in_one("", ["Nada", "Aree"], ["bees", "Nada"]))
    
    def test_edge_case_empty_string_in_list1(self):
        """Test case where the input string is empty and present in list1."""
        self.assertTrue(is_in_one("", [""], ["Nada", "bees"]))
    
    def test_edge_case_empty_string_in_list2(self):
        """Test case where the input string is empty and present in list2."""
        self.assertTrue(is_in_one("", ["Nada", "Aree"], ["", "Nada"]))

if __name__ == "__main__":
    unittest.main()
