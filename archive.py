#!/usr/bin/python
# -*- coding:utf-8 -*-
import io 
import os
import sys
import json
import github

''' ?κ²© ??₯μ (using Github) '''
class Archive:
    kDefaultData = 1

    ''' ?μ±??'''
    def __init__(self, token, repo):
        try:
            self.repo = github.Github(token).get_user().get_repo(repo)
            self.data = json.loads(
                self.repo.get_issue(self.kDefaultData).body
            )

        except Exception as e:
            pass

    ''' ??₯νκΈ?'''
    def find(self, key):
        if key not in self.data:
            return {}

        return self.data[key]

    ''' ??₯νκΈ?'''
    def update(self, key, value):
        try:
            self.data[key] = value

        except Exception as e: 
            return False
        
        return True

    ''' ??₯νκΈ?'''
    def save(self):
        try:
            issue = self.repo.get_issue(self.kDefaultData)

        except Exception as e: 
            return False

        try:
            issue.edit(body=json.dumps(self.data))
        
        except Exception as e: 
            return False

        return True
