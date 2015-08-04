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


# Simple Files Search MultiProcessing

from multiprocessing import Process
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

#  
# Create Main Function
#

if __name__ == '__main__':
    
    startTime = time.time()
    
    p1 = Process(target=SearchFile, args=('Dictionary.txt', 'thought') )
    p1.start()
    
    p2 = Process(target=SearchFile, args=('Dictionary.txt', 'exile')  )
    p2.start()
    
    p3 = Process(target=SearchFile, args=('Dictionary.txt', 'port')  )
    p3.start()
    
    p4 = Process(target=SearchFile, args=('Dictionary.txt', '$Slllb')  )
    p4.start()
    
    # Next we use the join to wait for all processes to complete
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    elapsedTime = time.time() - startTime
    print 'Duration: ', elapsedTime
    
# Program Output

