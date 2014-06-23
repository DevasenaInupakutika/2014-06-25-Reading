# UNIT TESTING WITH NOSE

## Step1:

Create a function to extract mean number of BioSignatures seen on MARS per sighting from a `.csv` file and name it `mean_sightings.py`.

## Step2:

Now that we have function in a module, write some unit tests to make sure the function is giving us correct answers. Create a new text file called `test_mean_sightings.py` which will hold our unit tests. At the top of the file type or copy below code:

~~~
from mean_sightings import get_sightings

filename = 'sightings_tab_sm.csv'
~~~

## Step3:


