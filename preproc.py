#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:15 2017

@author: rsilva
"""

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
    print('Hello, data in path: '+basedir)
    
def main():
    basedir='/home/rsilva/repos/code/nc-wkshop/fmri_workshop/data'
    prepro(basedir)
    
main()