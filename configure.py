#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json

''' 
    환경설정
'''
class Configure:
    ''' 생성자 '''
    def __init__(self, path):
        with io.open(path + '/app.json', 'r', encoding='utf-8-sig') as f:
            doc = json.load(f)

        for k, v in doc.items():
            self.makeVal(k, v)

    ''' 환경설정 변수 만들기  '''
    def makeVal(self, key, val):
        try:
            for k, v in val.items():
                self.makeVal(key + '_' + k, v)

        except Exception as e:
            if isinstance(val, basestring):
                exec('self.%s=\'%s\'' % (key.upper(), val))
            else:
                exec('self.%s=%s' % (key.upper(), val))
