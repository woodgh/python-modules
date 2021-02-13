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
import html_maker

''' Configure '''
def Configure(path):
    return configure.Configure(path)

''' Logger '''
def Logger(path):
    return logger.Logger(path)

''' Archive '''
def Archive(token, repo):
    return archive.Archive(token, repo)

''' HtmlMaker '''
def HtmlMaker(path, context):
    return html_maker.render(path, context)
