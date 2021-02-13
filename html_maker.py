#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json
import jinja2

''' HTML 렌더링 '''
def render(path, context):
    searchpath, fs  = os.path.split(path)
    distpath = os.path.abspath(os.path.join(searchpath + '/../dist/'))  

    try:
        envir = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=searchpath))
    
    except Exception, e:
        return False

    target_render = envir.get_template(fs).render(context)

    if not os.path.exists(distpath):
        os.makedirs(distpath)

    with io.open(os.path.join(distpath, fs), 'w+', encoding='utf-8-sig') as f:
        f.write(target_render)

    return True    


