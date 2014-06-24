#!/usr/bin/env python

import matplotlib.mlab as ml
import numpy as np
import sys

def get_sightings(filename, focusbiosig):

    # # Load table
    tab = ml.csv2rec(filename)

    focusbiosig = focusbiosig.capitalize()


    # Loop through all records, countings recs and biosignatures
    totalrecs = 0
    totalcount = 0
    for rec in tab:
                if rec['biosignature'] == focusbiosig:
            	   totalrecs += 1
                   totalcount += rec['count']

    if totalrecs == 0:
         meancount = 0
    else:
         meancount = totalcount/totalrecs

    # Return num of records and biosignatures seen
    return totalrecs, meancount

