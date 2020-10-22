#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json

''' 
    ?òÍ≤Ω?§Ï†ï
'''
class Configure:
    ''' ?ùÏÑ±??'''
    def __init__(self, path):
        with io.open(path + '/app.json', 'r', encoding='utf-8-sig') as f:
            doc = json.load(f)

        for k, v in doc.items():
            self.makeVal(k, v)

    ''' ?òÍ≤Ω?§Ï†ï Î≥Ä???ùÏÑ±?òÍ∏∞ '''
    def makeVal(self, key, val):
        try:
            for k, v in val.items():
                self.makeVal(key + '_' + k, v)

        except Exception as e:
            if isinstance(val, basestring):
                exec('self.%s=\'%s\'' % (key.upper(), val))
            else:
                exec('self.%s=%s' % (key.upper(), val))
