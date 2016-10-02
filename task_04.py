#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tasks with loop"""

import data

def process_data(data):
    for num in data:
        total = sum(data)
        return (total, float(total/len(data)))
    
    
