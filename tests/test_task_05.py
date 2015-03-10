#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05"""


# Import Python libs
import unittest

# Import user libs
import task_05
import data


class Task05TestCase(unittest.TestCase):
    """Test cases for Task 05"""

    def test_flip_keys_large(self):
        """Tests that process data produces the correct output."""
        inputdata = data.get_nested_data()
        expected = [v[::-1] for v in inputdata]
        self.assertEqual(task_05.flip_keys(inputdata), expected)

    def test_flip_keys_small(self):
        """Tests process_data() with a smaller sample"""
        inputdata = [(7, 8, 9), 'xyz']
        expected = [(9, 8, 7), 'zyx']
        self.assertEqual(task_05.flip_keys(inputdata), expected)

    def test_list_operations_in_place(self):
        """Tests that the list operations are performed in-place"""
        inputdata = [(1, 2, 3)]
        self.assertIs(task_05.flip_keys(inputdata), inputdata)


if __name__ == '__main__':
    unittest.main()
