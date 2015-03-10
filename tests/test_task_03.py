#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03"""


# Import Python libs
import unittest

# Import user libs
import task_03
import data


class Task03TestCase(unittest.TestCase):
    """Test cases for Task 03"""

    def test_directions(self):
        """Tests that DIRECTIONS has the correct values"""
        expected = ('North', 'South', 'East', 'West')
        self.assertEqual(task_03.DIRECTIONS, expected)

    def test_data_directions(self):
        """Tests that data.DIRECTIONS remains unchanged."""
        expected = ('North', 'South', 'East', 'Spaghetti Western')
        self.assertEqual(data.DIRECTIONS, expected)


if __name__ == '__main__':
    unittest.main()
