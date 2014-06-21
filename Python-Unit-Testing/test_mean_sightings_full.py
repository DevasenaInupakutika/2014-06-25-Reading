#!/usr/bin/python

'''
Unit tests for mean_sightings module. Uses sightings_tab_sm.csv as test data.
'''

from mean_sightings import get_sightings

# Always use this file for testing
filename = 'sightings_tab_sm.csv'

# Start the unit tests
def test_Water_is_correct():
    watrec, watmean = get_sightings(filename, 'Water')
    assert watrec == 2, 'Number of records for Water is wrong'
    assert watmean == 17, 'Mean sightings for Water is wrong'

def test_Clay_is_correct():
    clrec, clmean = get_sightings(filename, 'Clay')
    assert clrec == 2, 'Number of records for Clay is wrong'
    assert clmean == 25.5, 'Mean sightings for Clay is wrong'

def test_biosig_not_present():
    biosigrec, biosigmean = get_sightings(filename, 'NotPresent')
    print biosigrec, biosigmean
    assert biosigrec == 0, 'BioSignature missing should return zero records'
    assert biosigmean == 0, 'BioSignature missing should return zero mean'

def test_arg_capitalization_wrong():
    watrec, watmean = get_sightings(filename, 'Water')
    assert watrec == 2, 'Number of records for Water is wrong'
    assert watmean == 17, 'Mean sightings for Water is wrong'
