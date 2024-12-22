#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import unittest

from ..repeat_character import repeat_character

class TestRepeatCharacter(unittest.TestCase):
    def test_repeat_character(self):
        """Test cases for repeat_character function."""
        self.assertEqual(repeat_character("Omnia", "m", 7), "Ommmmmmmnia")
        self.assertEqual(repeat_character("Nada", "a", 4), "Naaaadaaaa")
        self.assertEqual(repeat_character("Hassa", "e", 33333), "Hassa")  # Character not in text
        self.assertEqual(repeat_character("", "a", 5), "")  # Empty string
        self.assertEqual(repeat_character("hello", "o", 0), "hell")  # No repetition


if __name__ == "__main__":
    unittest.main()
