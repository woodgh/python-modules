#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json

class Configure:
    envir = dict()

    def __init__ (self, path):
        with io.open(path, 'r', encoding='utf-8-sig') as f:
            self.envir = json.load(f)

        f.close()

    def get(self, key=None):
        if key is None:
            return self.envir
        
        return self.envir[key]
