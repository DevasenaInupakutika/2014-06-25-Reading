# Takes name of directory (here data) and filename extension (here .pdb) as command line parameters and prints
# name of the file with most number of lines in this directory with the mentioned extension.

for datafile in $1/*.$2
do
  wc -l $datafile >> result.txt
done

sort -n result.txt|tail -1
