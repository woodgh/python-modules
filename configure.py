#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json

''' 
    ?�경?�정
'''
class Configure:
    ''' ?�성??'''
    def __init__(self, path):
        with io.open(path + '/app.json', 'r', encoding='utf-8-sig') as f:
            doc = json.load(f)

        for k, v in doc.items():
            self.makeVal(k, v)

    ''' ?�경?�정 변???�성?�기 '''
    def makeVal(self, key, val):
        try:
            for k, v in val.items():
                self.makeVal(key + '_' + k, v)

        except Exception as e:
            if isinstance(val, basestring):
                exec('self.%s=\'%s\'' % (key.upper(), val))
            else:
                exec('self.%s=%s' % (key.upper(), val))
