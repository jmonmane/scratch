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

#
# NLTK QUERY FRONT END
# Python-Forensics
#    No HASP required
#

import sys
import _NLTKQuery

print "Welcome to the NLTK Query Experimentation"
print "Please wait loading NLTK ... "

import _classNLTKQuery

oNLTK = _classNLTKQuery.classNLTKQuery()

print
print "Input full path name where intended corpus file or files are stored"
print "Format for Windows e.g. c:\simpson\ "
print

userSpecifiedPath = raw_input("Path: ") 

# Attempt to create a text Corpus
result = oNLTK.textCorpusInit(userSpecifiedPath)

if result == "Success":
    
    menuSelection = -1
    
    while menuSelection != 0:
        
        if menuSelection != -1:
            print
            s = raw_input('Press Enter to continue...')
            
        menuSelection = _NLTKQuery.getUserSelection()        
        
        if menuSelection == 1:
            oNLTK.printCorpusLength()
        
        elif menuSelection == 2:
            oNLTK.printTokensFound()

        elif menuSelection == 3:
            oNLTK.printVocabSize()

        elif menuSelection == 4:
            oNLTK.printSortedVocab()

        elif menuSelection == 5:
            oNLTK.printCollocation()           

        elif menuSelection == 6:         
            oNLTK.searchWordOccurrence()      

        elif menuSelection == 7:    
            oNLTK.generateConcordance()      

        elif menuSelection == 8:
            oNLTK.generateSimiliarities()      

        elif menuSelection == 9:    
            oNLTK.printWordIndex()

        elif menuSelection == 10:    
            oNLTK.printVocabulary()
            
        elif menuSelection == 0:    
            print "Goodbye"
            print        
            
        elif menuSelection == -1:
            continue
        
        else:
            print "please select another option"
            menuSelection = 11

else:
        print "Closing NLTK Query Experimentation"
    
    
    
