#!/usr/bin/env python

'''
Module/script to calculate mean number of sightings of a given biosig in a 
given sightings csv file.
'''

import sys
import matplotlib.mlab as ml
import numpy as np


def get_sightings(filename, focusbiosig):

    # Load table
    tab = ml.csv2rec(filename)

    # Standardize capitalization of focusbiosig
    focusbiosig = focusbiosig.capitalize()

    # Find number of records and total count of biosigs seen
    isfocus = (tab['BioSignature'] == focusbiosig)
    totalrecs = np.sum(isfocus)

    if totalrecs == 0:
        meancount = 0
    else:
        meancount = np.mean(tab['count'][isfocus])

    # Return num of records and biosigs seen
    return totalrecs, meancount


def get_sightings_loop(filename, focusbiosig):

    # Load table
    tab = ml.csv2rec(filename)

    # Standardize capitalization of focusbiosig
    focusbiosig = focusbiosig.capitalize()

    # Loop through all records, countings recs and biosignaturess
    totalrecs = 0.
    totalcount = 0.
    for rec in tab:
        if rec['BioSignature'] == focusbiosig:
            totalrecs += 1
            totalcount += rec['count']

    if totalrecs==0:
        meancount = 0
    else:
        meancount = totalcount/totalrecs

    # Return num of records and biosignaturess seen
    return totalrecs, meancount

if __name__ == '__main__':
    #print sys.argv
    filename = sys.argv[1]
    focusbiosig = sys.argv[2]
    print get_sightings(filename, focusbiosig)
