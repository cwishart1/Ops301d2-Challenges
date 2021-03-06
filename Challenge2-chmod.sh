#!/bin/bash

# Script Name:                  Challenge2-chmod 
# Class Name:                   Ops 301
# Author Name:                  Cody Wishart
# Date of latest revision:      3/3/21
# Purpose:                      Use chmod to change permissions

# Variables
targetDir=""
newPerm=""

# Main
echo "Enter target directory"
read targetDir
cd $targetDir
echo "Enter new permission #"
read newPerm
chmod $newPerm ./*
echo ""
ls -al
