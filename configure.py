#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json

class Configure:
    envir = dict()

    def __init__ (self, path):
        try:
            with io.open(path, 'r', encoding='utf-8-sig') as f:
                self.envir = json.load(f)

            f.close()
            
        except Exception, e:
            logging.exception("init to Logger..." + e)

    def get(self, key):
        return self.envir[key]