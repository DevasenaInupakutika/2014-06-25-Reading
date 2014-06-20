# Prints list of the unique species appearing in all animals files.

for datafile in $*
do
 cut -d ',' -f 2 $datafile| sort| uniq
#cut -d ',' -f 2 $datafile|sort -u
done 
