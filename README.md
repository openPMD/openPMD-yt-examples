yt-project frontend examples
============================

Please read the comments in
 - [openPMD-yt](https://github.com/openPMD/openPMD-yt)

about the status of the implementation.

This repository is still in-development and you will need our
  - [example data sets](https://github.com/openPMD/openPMD-example-datasets)

to play with it.


Comments about the frontend
---------------------------

- `postionOffset` and `weighting` are ignored
- only `mass` and `charge` are interpreted as constants the others as arrays

- !!! in `data_structures.py`, `class OpenPMDDataset`, `parse_parameter_file`
  the size of the simulation box is hard coded and needs to be changed for
  each file

Description of the Scripts
--------------------------

- `Convert_unitDimensions_to_YTUnit.py` converts an openPMD unit array in an
  unit string for YT

- `Load_Particles_with_YT_loadParticles.py` is an example to load particles
  with the `yt.load_particles()` function instead of the more general
  `yt.load()`

- `Simple_HDF5_Hierarchy_Reader.py` shows the groups and attributes of a
  HDF5-file as a tree

- `YT_Example_Plots.py` contains a selection of examples plots with YT
