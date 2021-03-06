#!/bin/bash

# Script Name:                  Challenge5-logCLear
# Class Name:                   Ops 301
# Author Name:                  Cody Wishart
# Date of latest revision:      3/6/21
# Purpose:                      Clear logs
# Must be run as sudo

# Main
echo "Contents of Syslog:"
cat /var/log/syslog
echo "Clearing now"
echo ""
echo "" > /var/log/syslog
cat /var/log/syslog

echo "Contents of WTMP:"
cat /var/log/wtmp
echo ""
echo "Clearing WTMP"
echo "" > /var/log/wtmp
cat /var/log/wtmp
