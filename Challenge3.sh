#!/bin/bash

# Script Name:                  Challenge3 
# Class Name:                   Ops 301
# Author Name:                  Cody Wishart
# Date of latest revision:      3/4/21
# Purpose:                      Make a ui with simple functions

# Variable
check="5"

# Main
while [ $check -ne 0 ]
do
    # UI
    echo "Functions: 1= Print Hellow World, 2= Ping loopback address, 3= Print IP info"
    echo "Please input a function number or 0 to quit"
    read check

    if [ $check == 0 ]
    then
        break
    fi 

    if [ $check -ne 1 ] && [ $check -ne 2 ] && [ $check -ne 3 ]
    then
        # Input sanitization
        echo "Invalid input"
        echo ""
    else
        # Main functions
        if [ $check == 1 ]
        then
            echo "Hello World"
            echo ""
        fi

        if [ $check == 2 ]
        then
            ping -c 5 127.0.0.1
            echo ""
        fi

        if [ $check == 3 ]
        then
            ip a 
            echo ""
        fi    
    fi 

done
