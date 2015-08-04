'''
Copyright (c) 2014 Chet Hosmer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

'''

import argparse                        # Python Standard Library - Parser for command-line options, arguments
import os                              # Standard Library OS functions

# Name: ParseCommand() Function
#
# Desc: Process and Validate the command line arguments
#           use Python Standard Library module argparse
#
# Input: none
#  
# Actions: 
#              Uses the standard library argparse to process the command line
#
def ParseCommandLine():

    parser = argparse.ArgumentParser('PS-NMT')
       
    parser.add_argument('-v', '--verbose', help="Display packet details", action='store_true')

    # setup a group where the selection is mutually exclusive and required.
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--TCP',  help = 'TCP Packet Capture',   action='store_true')
    group.add_argument('--UDP',  help = 'UDP Packet Capture',   action='store_true')  
    
    parser.add_argument('-m',  '--minutes', help='Capture Duration in minutes',type=int)  
    parser.add_argument('-p',  '--outPath', type= ValidateDirectory, required=True, help="Output Directory")         
    
    theArgs = parser.parse_args()           

    return theArgs

# End Parse Command Line ===========================

def ValidateDirectory(theDir):

    # Validate the path is a directory
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')

    # Validate the path is writable
    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not writable')

#End ValidateDirectory ===================================
