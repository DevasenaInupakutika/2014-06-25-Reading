# UNIT TESTING WITH NOSE

## Step 1:

Create a function to extract mean number of BioSignatures (for example `Water`) seen on MARS per sighting from  `sightings_tab_sm.csv` file and name it `mean_sightings.py`.

## Step 2:

Now that we have function in a module, write some unit tests to make sure the function is giving us correct answers. Create a new text file called `test_mean_sightings.py` which will hold our unit tests. At the top of the file type or copy below code:

~~~
from mean_sightings import get_sightings

filename = 'sightings_tab_sm.csv'
~~~

## Step 3:

Write first test function `test_water_is_correct`, which will simply test to make sure our function written above gives correct answer when called using small data set `sightings_tab_sm.csv`.

## Step 4:

Test above function for `Clay` results.

## Step 5:

Fix function for Boundary case.

## Step 6:

Fix function for bad input.

## Step 7:

Run test suite again to make sure above created four tests now pass.

## Step 8:

Examine and Fix regression.

## Step 9:

Test Driven Development (TDD).

## Step 10:

Make a Standalone script based on above tested module.
