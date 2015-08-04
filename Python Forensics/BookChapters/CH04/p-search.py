'''
Copyright (c) 2014 Chet Hosmer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

usage: Python Search [-h] [-v] -k KEYWORDS -t SRCHTARGET -m THEMATRIX

optional arguments:

  -h,                           --help  show this help message and exit
  -v,                           --verbose  enables printing of additional program data
  -k KEYWORDS       --keyWords KEYWORDS  specify the file containing search word
  -t SRCHTARGET     --srchTarget SRCHTARGET  specify the target file to search
  -m THEMATRIX     --theMatrix THEMATRIX specify the weighted matrix file

'''

# 
# p-search : Python Word Search
# Author: C. Hosmer
# August 2013
# Version 1.0
#
# Simple p-search python program
#
# Read in a list of search words
# Read a binary file into a bytearray
# Search the bytearray for occurances of any specified search words
# Print a HEX/ ASCII display localizing the matching words
# Print out a list of possible words identified that didn't match
#
# Definition of a word.  a word for this example is an uninterrupted sequence of 
# 4 to 12 alpha characters 
#

import logging
import time
import _psearch

if __name__ == '__main__':

    PSEARCH_VERSION = '1.0'
       
    # Turn on Logging
    logging.basicConfig(filename='pSearchLog.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

    # Process the Command Line Arguments
    _psearch.ParseCommandLine()
   
    log = logging.getLogger('main._psearch')
    log.info("p-search started")

    # Record the Starting Time
    startTime = time.time()
    
    # Perform Keyword Search
    _psearch.SearchWords()
    
    # Record the Ending Time
    endTime = time.time()    
    duration = endTime - startTime   
    
    logging.info('Elapsed Time: ' + str(duration) + ' seconds')
    logging.info('')
    logging.info('Program Terminated Normally')

    
    
    


   

        






