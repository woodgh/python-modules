#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json
import github

''' 원격 저장소 (using Github) '''
class Archive:
    kDefaultArchive = 1

    ''' 생성자 '''
    def __init__(self, token, repo):
        try:
            self.repo = github.Github(token).get_user().get_repo(repo)

        except Exception as e:
            pass

    ''' 불러오기 '''
    def load(self):
        try:
            res = self.repo.get_issue(self.kDefaultArchive).body

        except Exception as e: 
            return json.dumps({})
        
        return json.loads(res)

    ''' 저장하기 '''
    def save(self, body):
        try:
            issue = self.repo.get_issue(self.kDefaultArchive)

        except Exception as e: 
            return False

        try:
            issue.edit(body=body)
        
        except Exception as e: 
            return False

        return True
