from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

"""

# Test Cases for COCOMO

"""
from cocomo import *
from badSmells import *
 
PROJECTS  = [osp]
TREATMENTS= [doNothing, hw3_1]

@go
def _effortsTreated():
  for project in PROJECTS:
    print("\n#### ",project.__name__," ","#"*50,"\n")
    sample(projects=[project],treatments=TREATMENTS)

@go
def _badSmellsTreated():
  rseed(1)
  for project in PROJECTS:
    print("\n#### ",project.__name__," ","#"*50,"\n")
    sample(projects=[project],treatments=TREATMENTS,score=badSmell)
