from mean_sightings import get_sightings

filename = 'sightings_tab_sm.csv'

def test_water_is_correct():
	watrec, watmean = get_sightings(filename, 'Water')
	assert watrec == 2, 'Number of records for water is wrong'
	assert watmean == 17, 'Mean sightings for water is wrong'
	
