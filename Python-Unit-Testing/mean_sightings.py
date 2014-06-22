#!/usr/bin/env python

import matplotlib.mlab as ml
import numpy as np
import sys

def get_sightings(filename, focusbiosig):

    # # Load table
    tab = ml.csv2rec(filename)

    #focusbiosig = focusbiosig.capitalize()

    # Find number of records and total count of BioSignatures seen
    isfocus = (tab[ 'biosignature' ] == focusbiosig)
    totalrecs = np.sum(isfocus)
    if totalrecs == 0:
         meancount = 0
    else:
         meancount = np.mean(tab[ 'count' ][isfocus])

    # # Return num of records and biosignatures seen
    return totalrecs, meancount

