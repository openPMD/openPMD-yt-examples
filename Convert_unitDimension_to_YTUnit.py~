"""

Programm: Convert_unitDimension_to_YTUnit
Author: Daniel Grassinger
Date: 25.09.2015
Python: 2.7.6

Description: This little script converts a unitDimension array
	     from a openPMD Dataset into a unit string for yt 
	     
Usage: unitsToString(array with 7 float(unitDimension Attribut) )

"""
	
    
def unitsToString(units):
    def getUnitString(num):
	if(num==0):
	    return "m"
	elif(num==1):
	    return "kg"
	elif(num==2):
	    return "s"
	elif(num==3):
	    return "A"
	elif(num==4):
	    return "K"
	elif(num==5):
	    return "mole"
	elif(num==6):
	    return "cd"

    divident = ""
    divisor = ""
    
    num = 0
    for unit in units:
        if(unit==0.0):
            continue
        elif(unit==1):
            divident+=getUnitString(num) + " * "
        elif(unit==-1):
            divisor+=getUnitString(num) + " * "
        elif(unit>0):
            divident+=getUnitString(num) + "**" + str(unit) + " * "
        else:
            divisor+=getUnitString(num) + "**" + str(-1.0*unit) + " * "
        num+=1
    if(divisor==""):
        return divident[:-3]
    else:
        return "( "+ divident[:-3] + " ) / ( " + divisor[:-3] + " )"

"""

example:
	print unitsToString([-3.,  0.,  1.,  1.,  0.,  0.,  0.])

example output:
	( kg * s ) / ( m**3.0 )
"""
            
