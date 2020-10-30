# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 06:47:30 2020

@author: Usuario
"""


def MCD(n,d):
    if n%d==0:
      return d
    else:
      return MCD(d, n%d)
if __name__=="__main__":
    print(MCD(40,100))