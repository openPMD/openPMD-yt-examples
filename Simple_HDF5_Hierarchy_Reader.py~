"""

Programm: Simple_HDF5_Hierarchy_Reader
Author: Daniel Grassinger
Date: 25.09.2015
Python: 2.7.6

Description: This little script read a HDF5-File and prints all 
	     the groups and datasets and attributes as a tree.

Usage: readkey(file, startFolder(most times "/"), indentation(as a string) )

"""

def readkeys(f, folder, ebene):
    #print "Folder: "+folder
    try:
        for attr in f[folder].attrs.keys():
            print ebene +"Attribut: "+ attr
    except AttributeError:
        pass
    try:
        for key in f[folder].keys():
            print ebene + "Gruppe: "+ key    
            readkeys(f,folder+"/"+key, ebene+"        ")
    except AttributeError:
        pass

"""

example:

	f = h5py.File("data00000400.h5")
	readkeys(f,"/","    ")


example output:

    Attribut: openPMD
    Attribut: openPMDextension
    Attribut: software
    Attribut: softwareVersion
    Attribut: date
    Attribut: meshesPath
    Attribut: particlesPath
    Attribut: iterationEncoding
    Attribut: iterationFormat
    Attribut: basePath
    Gruppe: data
            Gruppe: 400
                    Attribut: time
                    Attribut: dt
                    Attribut: timeUnitSI
                    Gruppe: fields
                            Attribut: fieldSolver
                            Attribut: fieldBoundary
                            Attribut: particleBoundary
                            Attribut: currentSmoothing
                            Attribut: currentSmoothingParameters
                            Attribut: chargeCorrection
                            Gruppe: B
                                    Attribut: unitDimension
                                    Attribut: timeOffset
                                    Attribut: geometry
                                    Attribut: gridSpacing
                                    Attribut: axisLabels
                                    Attribut: dataOrder
                                    Attribut: gridUnitSI
                                    Attribut: gridGlobalOffset
                                    Attribut: fieldSmoothing
                                    Gruppe: x
                                            Attribut: unitSI
                                            Attribut: position
                                    Gruppe: y
                                            Attribut: unitSI
                                            Attribut: position
                                    Gruppe: z
                                            Attribut: unitSI
                                            Attribut: position
"""
