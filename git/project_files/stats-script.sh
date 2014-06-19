for datafile in *.txt
do
    bash goostats $datafile | echo
done