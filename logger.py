#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
import time
import logging
import datetime

class Logger:
    def __init__(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

        try:
            logging.basicConfig(
                filename= path + '/' + str(datetime.datetime.now().strftime("%Y_%m_%d.log")),\
                filemode= "a",\
                level=logging.DEBUG,\
                maxBytes=1024,\
                backupCount=10,\
                format='[%(asctime)s] %(message)s'\
            )
            
        except Exception as e:
            logging.exception("init to Logger..." + e)
