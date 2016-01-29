# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import yt

# <codecell>

from numpy import *

# <codecell>

import sys
print(sys.path)

# <codecell>

"""

Programm: YT_Example_Plots
Author: Daniel Grassinger
License: Modified BSD License (also known as New or Revised BSD)
Date: 25.09.2015
Python: 2.7.6
YT Version: 3.2

Description: This file show some examples how to plot data in yt

more examples and docomentation on:
http://yt-project.org/doc/visualizing/

Required: an example openPMD called "data00000800.h5" file must
          exitst in the same folder

"""

import yt
import numpy as np
import h5py
import math


# load an example dataset
ds = yt.load("/home/fwktg1/openPMD-example-datasets/example-3d/hdf5/data00000200.h5")

#First some general informations on the dataset

print "1: General Informations:"
ds.print_stats()

print "   This Fields does yt know or could generate them"
ds.field_list

print "   Size of Simulation Box: "
print ds.domain_width

# This returns the data of this field as a YTArray with units
print "   The Data and Units of the Field E_x"
ad = ds.all_data()
print ad["E_x"] 

#First simple plots
print "2: Simple Plots"

print "   Projection Plot of E_x"
p = yt.ProjectionPlot(ds, "y", "E_x")

# This adds a Title to the Plot
p.annotate_title('Projection Plot of E_x')

# Shows the Plot on Screen
p.show()
# Saves the Plot as .png
p.save()

# This makes a SlicePlot of rho and overplot the contur of E

# This Function discribes how E is calculated out of E_x, E_y, E_z
def _absE_x(field, data):
    return np.sqrt(data["E_x"]*data["E_x"]+data["E_y"]*data["E_y"]+data["E_z"]*data["E_z"])

# Here E is defined as a new Field called "absE_x"
ds.add_field(("openPMD", "absE_x"),function=_absE_x,units="V/m")

# This makes a SlicePlot of rho
p = yt.SlicePlot(ds, "y", ['rho'])

# This overplots the contur of E
p.annotate_contour(("openPMD","absE_x"),ncont=5, clim=(1e12,1e11))
p.show()

# There are a lot of another annotations and additional parameters for the visualisation on the yt website

#Plotting time series
print "3: Plotting time series"

# Only load with yt.load but use ? or * instead of characters creats a time series
timeseries = yt.load("/home/fwktg1/openPMD-example-datasets/example-3d/hdf5/data0000??00.h5")

# Get every dataset from timeseries and plot it
for ds in timeseries:
    p = yt.SlicePlot(ds, "y","E_x") 
    p.show()

# Volume Rendering of 3D Data
# As OpenPMD 3D Datasets are not tested yet we use other sample Data
#Sample Data from http://yt-project.org/data/
ds = yt.load("/bigdata/hplsim/external/fwktg1/yt/IsolatedGalaxy/galaxy0030/galaxy0030")

#This creates and shows a 3D Model of the sample Data
print "4: Volume Rendering of Example Galaxy"
tf = yt.ColorTransferFunction((-28, -25))
tf.add_layers(4, w=0.03)
cam = ds.camera([0.5, 0.5, 0.5], [1.0, 1.0, 1.0], (20.0, 'kpc'), 512, tf, no_ghost=False)
cam.show(clip_ratio=4.0)


# <codecell>

p.save()

# <codecell>


