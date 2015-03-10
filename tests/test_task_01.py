#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


# Import Python libs
import unittest

# Import user libs
import task_01


class Task01TestCase(unittest.TestCase):
    """Test cases for Task 01"""

    def test_elements(self):
        """Tests that ELEMENTS has the correct construction."""
        expected = (None,
                    'Hydrogen',
                    'Helium',
                    'Lithium',
                    'Beryllium',
                    'Boron',
                    'Carbon'
                   )
        self.assertEqual(task_01.ELEMENTS, expected)

    def test_operations_order(self):
        """Tests that OPERATIONS_ORDER has the correct construction."""
        expected = ['Parentheses',
                    'Exponents',
                    'Multiplication',
                    'Division',
                    'Addition',
                    'Subtraction'
                   ]
        self.assertEqual(task_01.OPERATIONS_ORDER, expected)


if __name__ == '__main__':
    unittest.main()
