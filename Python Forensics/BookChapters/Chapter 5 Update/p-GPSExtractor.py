#
# GPS Extraction
# Python-Forensics
# No HASP required
#

import os
import _modEXIF
import _csvHandler
import _commandParser
from classLogging import _ForensicLog

# Offsets into the return exifData for
# TimeStamp, Camera Make and Model

TS = 0
MAKE = 1
MODEL = 2

# Process the Command Line Arguments
userArgs = _commandParser.ParseCommandLine()

# create a log object
logPath = userArgs.logPath+"ForensicLog.txt"
oLog = _ForensicLog(logPath)

oLog.writeLog("INFO", "Scan Started")

csvPath = userArgs.csvPath+"imageResults.csv"
oCSV = _csvHandler._CSVWriter(csvPath)

# define a directory to scan
scanDir = userArgs.scanPath
try:
    picts = os.listdir(scanDir)
except:
    oLog.writeLog("ERROR", "Invalid Directory "+ scanDir)
    exit(0)

print "Program Start"
print

for aFile in picts:
    
    targetFile = scanDir+aFile
    
    if os.path.isfile(targetFile):

        gpsDictionary, exifList = _modEXIF.ExtractGPSDictionary(targetFile)

        if (gpsDictionary != None):

            # Obtain the Lat Lon values from the gpsDictionary
            # Converted to degrees
            # The return value is a dictionary key value pairs
            
            dCoor = _modEXIF.ExtractLatLon(gpsDictionary)

            if dCoor:
                lat = dCoor.get("Lat")
                latRef = dCoor.get("LatRef")
                lon = dCoor.get("Lon")
                lonRef = dCoor.get("LonRef")
                
                if ( lat and lon and latRef and lonRef):
                    print str(lat)+','+str(lon)
                    # write one row to the output file         
                    oCSV.writeCSVRow(targetFile, exifList[TS], exifList[MAKE], exifList[MODEL],latRef, lat, lonRef, lon)
                    oLog.writeLog("INFO", "GPS Data Calculated for :" + targetFile)
                else:
                    oLog.writeLog("WARNING", "No GPS EXIF Data for "+ targetFile)
            else:
                oLog.writeLog("WARNING", "Improper GPS Data for "+targetFile)
        else:
            oLog.writeLog("WARNING", "No GPS EXIF Data for "+ targetFile)
    else:
        oLog.writeLog("WARNING", targetFile + " not a valid file")

print "Program End"
# Clean up and Close Log and CSV File        
del oLog
del oCSV
        
