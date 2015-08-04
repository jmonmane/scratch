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
import logging

# 
# Class: _ForensicLog
#
# Desc: Handles Forensic Logging Operations
#
# Methods  constructor:  Initializes the Logger
#          writeLog:     Writes a record to the log
#          destructor:   Writes message and shutsdown the logger

class _ForensicLog:

    def __init__(self, logName):
        try:
            # Turn on Logging
             logging.basicConfig(filename=logName,level=logging.DEBUG,format='%(asctime)s %(message)s')            
        except:
            print "Forensic Log Initialization Failure ... Aborting"
            exit(0)

    def writeLog(self, logType, logMessage):
        if logType == "INFO":
             logging.info(logMessage)
        elif logType == "ERROR":
            logging.error(logMessage)
        elif logType == "WARNING":
            logging.warning(logMessage)
        else:
            logging.error(logMessage)
        return

    def __del__(self):
        logging.info("Logging Shutdown")
        logging.shutdown()
