from mean_sightings import get_sightings

filename = 'sightings_tab_sm.csv'

def test_water_is_correct():
	watrec, watmean = get_sightings(filename, 'Water')
	assert watrec == 2, 'Number of records for water is wrong'
	assert watmean == 17, 'Mean sightings for water is wrong'
	
def test_clay_is_correct():
        clayrec, claymean = get_sightings(filename, 'Clay')
        assert clayrec == 2, 'Number of records for Clay is wrong'
        assert claymean == 25.5, 'Mean sightings for Clay is wrong'

def test_nothing_is_correct():
        norec, nomean = get_sightings(filename, 'NotPresent')
        assert norec == 0, 'Biosignature missing should return zero records'
        assert nomean == 0, 'Biosignature missing should return zero mean'

def test_water_is_correct():
        watrec, watmean = get_sightings(filename, 'waTeR')
        assert watrec == 2, 'Number of records for water is wrong'
        assert watmean == 17, 'Mean sightings for water is wrong'
