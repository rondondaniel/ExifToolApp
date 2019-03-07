# -*- coding: utf-8 -*-
"""
Daniel Rondon - Drone Geomodeling
"""

import os

# main fonction
def main():
    try :
        #const variables 
        ALT='D:\Temp\ALT'
        MSL='D:\Temp\MSL'
        Datum="60"
    
        #commands generator
        rwAltRef='exiftool -n -GPSAltitudeRef=0 ' + ALT
        rwAlt='exiftool -n -tagsFromFile @ "-RelativeAltitude>GPSAltitude" ' + ALT
        rwMSL='exiftool -n -GPSAltitude+=' + Datum + ' ' + ALT + ' ' + '-o ' + MSL
        readAlt='exiftool -n -GPSAltitude ' + ALT
        readMSL='exiftool -n -GPSAltitude ' + MSL

        #commands execution by exiftool.exe
        os.system("cls")
        print('Executing GPSAltitudeRef...' )
        os.system(rwAltRef)
        print('Executing RelativeAltitude>GPSAltitude...' )
        os.system(rwAlt)
        print('Executing GPSAltitude+DATUM...' )
        os.system(rwMSL)
        print('Check...')
        os.system(readAlt)
        os.system(readMSL)

        return 0

    except:
        print 'Exception occurred'
        sys.exit()

    print 'fatal error'
    
#App Begining
if __name__=="__main__":
    main()

