"""

Programm: Simple_HDF5_Hierarchy_Reader
Author: Daniel Grassinger
Date: 25.09.2015
Python: 2.7.6
YT Version: 3.2

Description: This loads the particle position and momentum from a hdf5 file.
             The density is calculated by yt. The Plot is a ProjectionPlot
             from the density of the particles.
             This way you can only load particles and many of the yt function 
	     are not supportet like parallelism

"""

import yt
import numpy as np
import h5py

#open the file
f = h5py.File("data00000800.h5","r")
basePath = f.attrs["basePath"]
particlesPath = f.attrs["particlesPath"]

#load the particles into memory
ppx = f[basePath+particlesPath+"/electrons/position/x"][:]
ppy = f[basePath+particlesPath+"/electrons/position/y"][:]
ppz = f[basePath+particlesPath+"/electrons/position/z"][:]
pmx = f[basePath+particlesPath+"/electrons/momentum/x"][:]
pmy = f[basePath+particlesPath+"/electrons/momentum/y"][:]
pmz = f[basePath+particlesPath+"/electrons/momentum/z"][:]
ppm = np.ones_like(ppx) # Generate the same mass for all particles

#create a dictionary for yt
#! you can only use fieldtypes already known by yt
data = {'particle_position_x': ppx, # assumes input is cm
        'particle_position_y': ppy,
        'particle_position_z': ppz,
        'particle_momentum_x': pmx, # assumes input is cm/s
        'particle_momentum_y': pmy,
        'particle_momentum_z': pmz,
        'particle_mass': ppm}

#create the size of the simulation box
bbox = np.array([[min(ppx), max(ppx)], [min(ppy), max(ppy)], [min(ppz), max(ppz)]])
print bbox

#load the particles into yt
ds = yt.load_particles(data, n_ref=64, bbox=bbox)

#plot the particles
p = yt.ProjectionPlot(ds, "y", ["all_density"])
p.show()
