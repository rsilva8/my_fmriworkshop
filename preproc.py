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
    input=glob.glob(os.path.join(basedir,'sub-*','func','sub-*task-bart_bold.nii.gz'))
    for item in input:
        output=item.strip('.nii.gz')+'_brain.nii.gz'
        if os.path.exists(output):
            print(output+' already processed BET')
        else:
            os.system('bet %s %s -F'%(item,output))
        print('Done')
    
def main():
    basedir='/home/rsilva/repos/code/nc-wkshop/data'
    
    input=glob.glob(basedir+'/sub-*/func/sub-*task-bart_bold.nii.gz')
    #print(input[0:10])
    
    x=input[1]
    
    sub=input[1].split('/')[7] # 7 is subject number
    #print(input[1])
    #print(sub)
    
    subtask=input[1].split('/')[9].split('.')[0] # 9 is file name
    #print(subtask)
    
    #output=subtask+'_brain'
    
    output=input[1].strip('.nii.gz')+'_brain'
    #os.system('bet %s %s -F'%(x,output))
    
    prepro(basedir)
    
main()

#%run onset_parser.py -task bart -cols action_CASHOUT action_ACCEPT action_EXPLODE