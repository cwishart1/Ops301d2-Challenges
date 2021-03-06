#!/bin/bash

# Script Name:                  Challenge1-syslogBackup 
# Class Name:                   Ops 301
# Author Name:                  Cody Wishart
# Date of latest revision:      3/2/21
# Purpose:                      copy syslog, append date to it

# Variables
dir="pwd"
logDate="date"

# Main
cp /var/log/syslog "$dir"      # I figured storing pwd in a var would be an easy way to make sure the log goes into the exact dir you are in
mv pwd "syslog: $($logDate)"   # Why the heck is the log renamed pwd when this line is commented out
