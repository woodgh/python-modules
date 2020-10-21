#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json
import logging
import datetime

''' 
    로그
'''
class Logger:
    ''' 생성자 '''
    def __init__(self, path):
        targetPath = path + '/logs/'

        if not os.path.exists(targetPath):
            os.makedirs(targetPath)

        try:
            logging.basicConfig(
                filename= targetPath + str(datetime.datetime.now().strftime("%Y_%m_%d.log")),\
                filemode= "a",\
                level=logging.DEBUG,\
                maxBytes=1024,\
                backupCount=10,\
                format='[%(asctime)s] %(message)s'\
            )
            
        except Exception as e:
            logging.exception(e)
