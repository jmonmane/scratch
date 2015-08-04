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
# NLTK QUERY CLASS MODULE
# Python-Forensics
#    No HASP required
#

import os                                    # Standard Library OS functions
import sys
import logging                          # Standard Library Logging functions
import nltk                                 # Import the Natural Language Toolkit
from nltk.corpus import PlaintextCorpusReader   #Import the PlainTextCorpusReader Module

# NLTKQuery Class

class classNLTKQuery:
    
            def textCorpusInit(self, thePath):
               
                        # Validate the path is a directory
                        if not os.path.isdir(thePath):
                                    return "Path is not a Directory"

                        # Validate the path is readable
                        if not os.access(thePath, os.R_OK):
                                    return "Directory is not Readable"
                
                        # Attempt to Create a corpus with all .txt files found in the directory
                        try:
                                    
                                    self.Corpus = PlaintextCorpusReader(thePath, '.*')
                                    print "Processing Files : "
                                    print self.Corpus.fileids()
                                    print "Please wait ..."
                                    self.rawText = self.Corpus.raw()
                                    self.tokens = nltk.word_tokenize(self.rawText)
                                    self.TextCorpus = nltk.Text(self.tokens)         
                        except:
                                    return "Corpus Creation Failed"
                
                        self.ActiveTextCorpus = True
                        
                        return "Success"
       
            def printCorpusLength(self):
                        print "Corpus Text Length: ",
                        print len(self.rawText)
                        
            
            def printTokensFound(self):
                        print "Tokens Found: ",
                        print len(self.tokens)    
                        
            def printVocabSize(self):
                        print "Calculating ..."
                        print "Vocabulary Size: ",
                        vocabularyUsed = set(self.TextCorpus)
                        vocabularySize = len(vocabularyUsed)                        
                        print vocabularySize
    
            def printSortedVocab(self):
                        print "Compiling ..."
                        print "Sorted Vocabulary ",
                        print sorted(set(self.TextCorpus))
                        
            def printCollocation(self):
                        print "Compiling Collocations ..."
                        self.TextCorpus.collocations()
                        
            def searchWordOccurrence(self):
                        myWord = raw_input("Enter Search Word : ")
                        if myWord:
                                    wordCount = self.TextCorpus.count(myWord)
                                    print myWord+" occured: ",
                                    print  wordCount,
                                    print " times"
                        else:
                                    print "Word Entry is Invalid"                        
                        
            def generateConcordance(self):
                        myWord = raw_input("Enter word to Concord : ")
                        if myWord:
                                    self.TextCorpus.concordance(myWord)
                        else:
                                    print "Word Entry is Invalid"
                        
            def generateSimiliarities(self):
                        
                        myWord = raw_input("Enter seed word : ")
                        if myWord:
                                    self.TextCorpus.similar(myWord)
                        else:
                                    print "Word Entry is Invalid"          
                                    
            def printWordIndex(self):
                        myWord = raw_input("Find first occurrence of what Word? : ")
                        if myWord:
                                    wordIndex = self.TextCorpus.index(myWord)
                                    print "First Occurrence of: " + myWord + " is at offset: ",
                                    print wordIndex
                        else:
                                    print "Word Entry is Invalid"     
                        
            def printVocabulary(self):
                        print "Compiling Vocabulary Frequencies",
                        vocabFreqList = self.TextCorpus.vocab()         
                        print vocabFreqList.items()


                


            
