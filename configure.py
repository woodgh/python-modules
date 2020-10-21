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
            self.makeKey(k, v)

    ''' 환경설정 변수 생성하기 '''
    def makeKey(self, key, val):
        try:
            for k, v in val.items():
                self.makeKey(key + '_' + k, v)

        except Exception as e:
            exec('self.%s=\'%s\'' % (key.upper(), val))
