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
# NLTK Query Support Methods
# Python-Forensics
#    No HASP required
#

# Function to print the NLTK Query Option Menu
def printMenu():
    print "==========NLTK Query Options ========="
    print "[1]    Print Length of Corpus"
    print "[2]    Print Number of Token Found"
    print "[3]    Print Vocabulary Size"
    print "[4]    Print Sorted Vocabulary"
    print "[5]    Print Collocation"
    print "[6]    Search for Word Occurrence"
    print "[7]    Generate Concordance"
    print "[8]    Generate Similarities"
    print "[9]    Print Word Index"
    print "[10]  Print Vocabulary"
    print
    print "[0]    Exit NLTK Experimentation"
    print
  
 # Function to obtain user input 
    
def getUserSelection():
    printMenu()
    
    try:
        menuSelection = int(input('Enter Selection (0-10) >> ')) 
    except ValueError:
        print 'Invalid input. Enter a value between 0 -10 .'
        return -1

    if not menuSelection in range(0, 11):
        print 'Invalid input. Enter a value between 0 - 10.'
        return -1

    return menuSelection