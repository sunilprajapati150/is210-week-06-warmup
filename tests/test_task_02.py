#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


# Import Python libs
import unittest

# Import user libs
import task_02


class Task02TestCase(unittest.TestCase):
    """Test cases for Task 02"""

    def test_ballets(self):
        """Tests that BALLETS has the correct construction."""
        expected = ['The Nutcracker',
                    'Swan Lake',
                    'Sleeping Beauty',
                    'Onegin',
                    'Manon',
                    'Le Corsair',
                    'Serenade',
                    'Agon',
                    'Apollo',
                    'Scherehazade',
                    'Giselle',
                    'Robert Schumann\'s "Davids Bundlertanze"',
                    'Firebird',
                    'Concerto Barocco',
                    'Napoli',
                    "A Midsummer Night's Dream",
                    'La Bayadere',
                    'Romeo and Juliet',
                    'Jewels',
                    'The Four Temperaments',
                    'La Valse',
                    'Herman Schmerman',
                    'Don Quixote',
                    'Sylvia'
                   ]
        self.assertEqual(task_02.BALLETS, expected)


if __name__ == '__main__':
    unittest.main()
