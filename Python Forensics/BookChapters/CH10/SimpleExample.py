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


# Simple Files Search Single Core Processing

import time

def SearchFile(theFile, theString):
    try:
        fp = open(theFile,'r')
        buffer = fp.read()
        fp.close()
        if theString in buffer:
            print 'File: ', theFile, ' String: ', theString, '\t', ' Found'
        else:
            print 'File: ', theFile, ' String: ', theString, '\t', ' Not Found'  
    except:
        print 'File processing error'

startTime = time.time()

SearchFile('Dictionary.txt', 'thought')
SearchFile('Dictionary.txt', 'exile')
SearchFile('Dictionary.txt', 'port')
SearchFile('Dictionary.txt', '$Slllb!')

elapsedTime = time.time() - startTime
print 'Duration: ', elapsedTime, ' Seconds'




    
