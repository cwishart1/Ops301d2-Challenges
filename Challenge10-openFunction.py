#!/usr/bin/env python3

# Script Name:                  Challenge10-openFunction
# Class Name:                   Ops 301
# Author Name:                  Cody Wishart
# Date of latest revision:      3/15/21
# Purpose:                      Create and manipulate a txt file

# Import OS
import os

# Main
f = open('test.txt', 'w') 
f.write('1\n2\n3')
f = open('test.txt', 'r')
print(f.read(1))
os.remove("test.txt")
