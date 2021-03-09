#!/usr/bin/env python3

# Script Name:                  Challenge6-pythonIntro
# Class Name:                   Ops 301
# Author Name:                  Cody Wishart
# Date of latest revision:      3/8/21
# Purpose:                      Practice in Python3

# Import Library
import os

# Variables
who = "whoami"
ip = "ip a"
lsh = "lshw -short"

# Main
print("Hello") 
os.system(who)
print("\nHere is your IP info:")
os.system(ip)
print("\nAnd your computer info:")
os.system(lsh)
