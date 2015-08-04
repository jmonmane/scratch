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
# Data Extraction - Python-Forensiscs
# Extract GPS Data from EXIF supported Images  (jpg, tiff)
# Support Module
#

import os                                  # Standard Library OS functions
from classLogging import _ForensicLog     # Abstracted Fornesic Logging Class

# import the Python Image Library 
# along with TAGS and GPS related TAGS

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


#
# Extract EXIF Data
#
# Input: Full Pathname of the target image
#
# Return: gps Dictionary and selected exifData list
#

def ExtractGPSDictionary(fileName):
     
    try:
        pilImage = Image.open(fileName)
        exifData = pilImage._getexif()
    
    except Exception:
        # If exception occurs from PIL processing
        # Report the 
        return None, None
    
    # Interate through the exifData
    # Searching for GPS Tags
    
    imageTimeStamp = "NA"
    CameraModel = "NA"
    CameraMake = "NA"
    
    
    if exifData:
            
        for tag, theValue in exifData.items():
                
            # obtain the tag
            tagValue = TAGS.get(tag, tag)
                
            # Collect basic image data if available
            
            if tagValue == 'DateTimeOriginal':
                imageTimeStamp = exifData.get(tag)
                
            if tagValue == "Make":
                cameraMake = exifData.get(tag)
                
            if tagValue == 'Model':
                cameraModel = exifData.get(tag)
                
            # check the tag for GPS
            if tagValue == "GPSInfo":
                
                # Found it !
                # Now create a Dictionary to hold the GPS Data
                
                gpsDictionary = {}
                
                # Loop through the GPS Information
                for curTag in theValue:
                    gpsTag = GPSTAGS.get(curTag, curTag)
                    gpsDictionary[gpsTag] = theValue[curTag]
                
                basicExifData = [imageTimeStamp, cameraMake, cameraModel]    
                
                return gpsDictionary, basicExifData
            
    else:
        return None, None
    
# End ExtractGPSDictionary ============================


# 
# Extract the Lattitude and Longitude Values
# From the gpsDictionary
#

def ExtractLatLon(gps):

    # to perform the calcuation we need at least
    # lat, lon, latRef and lonRef
    
    if (gps.has_key("GPSLatitude") and gps.has_key("GPSLongitude") and gps.has_key("GPSLatitudeRef") and gps.has_key("GPSLatitudeRef")):

        latitude     = gps["GPSLatitude"]
        latitudeRef  = gps["GPSLatitudeRef"]
        longitude    = gps["GPSLongitude"]
        longitudeRef = gps["GPSLongitudeRef"]
    
        lat = ConvertToDegrees(latitude)
        lon = ConvertToDegrees(longitude)
                
        # Check Latitude Reference
        # If South of the Equator then lat value is negative
        
        if latitudeRef == "S":
            lat = 0 - lat
        
        # Check Longitude Reference
        # If West of the Prime Meridian in 
        # Greenwich then the Longitude value is negative
        
        if longitudeRef == "W":
            lon = 0- lon

        gpsCoor = {"Lat": lat, "LatRef":latitudeRef, "Lon": lon, "LonRef": longitudeRef}
        
        
        return gpsCoor
    
    else:
        return None
    
# End Extract Lat Lon ==============================================

# 
# Convert GPSCoordinates to Degrees
#
# Input gpsCoordinates value from in EXIF Format
#

def ConvertToDegrees(gpsCoordinate):
    
    d0 = gpsCoordinate[0][0]
    d1 = gpsCoordinate[0][1]
    try:
        degrees = float(d0) / float(d1)
    except:
        degrees = 0.0

    m0 = gpsCoordinate[1][0]
    m1 = gpsCoordinate[1][1]
    try:
        minutes = float(m0) / float(m1)
    except:
        minutes=0.0

    s0 = gpsCoordinate[2][0]
    s1 = gpsCoordinate[2][1]
    try:
        seconds = float(s0) / float(s1)
    except:
        seconds = 0.0
    
    floatCoordinate = float (degrees + (minutes / 60.0) + (seconds / 3600.0))

    return floatCoordinate

