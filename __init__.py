#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json
import github
import logging
import datetime
import requests
import logger
import configure
import archive

''' Initialize '''
def Configure(path):
    # Requests warning disabled
    requests.packages.urllib3.disable_warnings(
        requests.packages.urllib3.exceptions.InsecureRequestWarning
    )

    # Logger
    # logger.Logger(path)

    # Configure
    return configure.Configure(path)

''' Logger '''
def Logger(path):
    return logger.Logger(path)

''' Archive '''
def Archive(token, repo):
    return archive.Archive(token, repo)
