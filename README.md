Comments to the frontend:

- postionOffset and weighting are ignored
- only mass and charge ar interpreted as constants the others as arrays

- !!! in data_structures.py, class OpenPMDDataset, parse_parameter_file is the
      size of the simulation box hard code and have to be changed for every file

Description of the scripts:

Convert_unitDimensions_to_YTUnit.py convert a openPMD unit array in a Unit
string for YT

Load_Particles_with_YT_loadParticles.py is a example to load particles with the
yt.load_particles() function instead of yt.load()

Simple_HDF5_Hierarchy_Reader.py shows the groups and attributes of a HDF5-file
as a tree

YT_Example_Plots.py contains a lot of examples plots with YT 
