#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""


# Import Python libs
import unittest

# Import user libs
import task_04
import data


class Task04TestCase(unittest.TestCase):
    """Test cases for Task 04"""

    def test_process_data_large(self):
        """Tests that process data produces the correct output."""
        inputdata = data.get_data_as_list()[0:2500]
        total = sum(inputdata)
        expected = (total, total / float(len(inputdata)))
        self.assertEqual(task_04.process_data(inputdata), expected)

    def test_process_data_small(self):
        """Tests process_data() with a smaller sample"""
        inputdata = [329, 467, 201]
        total = sum(inputdata)
        expected = (total, total / float(len(inputdata)))
        msg = 'Failed to process data. Values tried: {}'.format(expected)
        self.assertEqual(task_04.process_data(inputdata), expected, msg)


if __name__ == '__main__':
    unittest.main()
