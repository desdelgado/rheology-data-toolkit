# README

## Description
This package is meant to help users process their rheology data into an HDF5 file that can be
uploaded to the [Materials Data Facility](https://materialsdatafacility.org/).  The rheodata package
contains `extractors` that are instrument specific.  Currently, the list of supported rheometer extractors are:

* Anton Paar MCR302
* ARES G2 4010-0602

This package also contains a `data_converter` file that will take the raw and parsed data from the extractors
and convert them into a single HDF5 file.  One can also add metadata to the overall project and to individual
tests.

## Installation
Before installing, make sure to pip install the [`xlrd`](https://xlrd.readthedocs.io/en/latest/ package).

This package is currently published on PyPi and can be installed by:
`pip install rheodata`

If you are using anaconda, first make sure you have `pip` installed and then run:
`pip install rheodata`

in your anaconda prompt.


## Getting Started

For a tutorial and guide for how to use some of the functions, there is a jupyter notebook in 
`getting_started/Demo.ipynb`.

## To Do 
Documentation still needs to be added






    
