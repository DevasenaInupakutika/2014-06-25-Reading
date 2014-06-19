for datafile in *.txt
do
    bash goostats $datafile >> output.txt
done