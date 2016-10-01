#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A good docstring"""

import data

BALLETS = data.BALLETS

del BALLETS[10]

BALLETS[1] = 'Swan Lake'

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote','Sylvia'])

