# Exercises

#### Creating Things

1.  What is the output of the closing `ls` command in the sequence shown below?

    ~~~
    $ pwd
    /home/thing/data
    $ ls
    proteins.dat
    $ mkdir recombine
    $ mv proteins.dat recombine
    $ cp recombine/proteins.dat ../proteins-saved.dat
    $ ls
    ~~~

2.  Suppose that:

    ~~~
    $ ls -F
    analyzed/  fructose.dat    raw/   sucrose.dat
    ~~~

    What command(s) could you run so that the commands below will produce the output shown?

    ~~~
    $ ls
    analyzed   raw
    $ ls analyzed
    fructose.dat    sucrose.dat
    ~~~

3.  What does `cp` do when given several filenames and a directory name, as in:

    ~~~
    $ mkdir backup
    $ cp thesis/citations.txt thesis/quotations.txt backup
    ~~~

    What does `cp` do when given three or more filenames, as in:

    ~~~
    $ ls -F
    intro.txt    methods.txt    survey.txt
    $ cp intro.txt methods.txt survey.txt
    ~~~

4.  The command `ls -R` lists the contents of directories recursively,
    i.e., lists their sub-directories, sub-sub-directories, and so on
    in alphabetical order at each level.
    The command `ls -t` lists things by time of last change,
    with most recently changed files or directories first.
    In what order does `ls -R -t` display things?

#### Pipes and Filters

1.  If we run `sort` on this file:

    ~~~
    10
    2
    19
    22
    6
    ~~~

    the output is:

    ~~~
    10
    19
    2
    22
    6
    ~~~

    If we run `sort -n` on the same input, we get this instead:

    ~~~
    2
    6
    10
    19
    22
    ~~~

    Explain why `-n` has this effect.

2.  What is the difference between:

    ~~~
    wc -l < mydata.dat
    ~~~

    and:

    ~~~
    wc -l mydata.dat
    ~~~


3.  A file called `animals.txt` contains the following data:

    ~~~
    2012-11-05,deer
    2012-11-05,rabbit
    2012-11-05,raccoon
    2012-11-06,rabbit
    2012-11-06,deer
    2012-11-06,fox
    2012-11-07,rabbit
    2012-11-07,bear
    ~~~

    What text passes through each of the pipes and the final redirect in the pipeline below?

    ~~~
    cat animals.txt | head -5 | tail -3 | sort -r > final.txt
    ~~~

4.  The command:

    ~~~
    $ cut -d , -f 2 animals.txt
    ~~~

    produces the following output:

    ~~~
    deer
    rabbit
    raccoon
    rabbit
    deer
    fox
    rabbit
    bear
    ~~~

    What other command(s) could be added to this in a pipeline to find
    out what animals the file contains (without any duplicates in their
    names)?


#### Finding Things

1.  Write a short explanatory comment for the following shell script:

    ~~~
    find . -name '*.dat' -print | wc -l | sort -n
    ~~~

2.  The `-v` flag to `grep` inverts pattern matching, so that only lines
    which do *not* match the pattern are printed. Given that, which of
    the following commands will find all files in `/data` whose names
    end in `ose.dat` (e.g., `sucrose.dat` or `maltose.dat`), but do
    *not* contain the word `temp`?

    1. `find /data -name '*.dat' -print | grep ose | grep -v temp`

    2. `find /data -name ose.dat -print | grep -v temp`

    3. `grep -v temp $(find /data -name '*ose.dat' -print)`

    4. None of the above.

#### Loops

1.  Suppose that `ls` initially displays:

    ~~~
    fructose.dat    glucose.dat   sucrose.dat
    ~~~

    What is the output of:

    ~~~
    for datafile in *.dat
    do
        ls *.dat
    done
    ~~~

2.  In the same directory, what is the effect of this loop?

    ~~~
    for sugar in *.dat
    
    do
        echo $sugar
        cat $sugar > xylose.dat
    done
    ~~~

    1.  Prints `fructose.dat`, `glucose.dat`, and `sucrose.dat`, and
        copies `sucrose.dat` to create `xylose.dat`.
    2.  Prints `fructose.dat`, `glucose.dat`, and `sucrose.dat`, and
        concatenates all three files to create `xylose.dat`.
    3.  Prints `fructose.dat`, `glucose.dat`, `sucrose.dat`, and
        `xylose.dat`, and copies `sucrose.dat` to create `xylose.dat`.
    4.  None of the above.

3.  The `expr` does simple arithmetic using command-line parameters:

    ~~~
    $ expr 3 + 5
    8
    $ expr 30 / 5 - 2
    4
    ~~~

    Given this, what is the output of:

    ~~~
    for left in 2 3
    do
        for right in $left
        do
            expr $left + $right
        done
    done
    ~~~

#### Scripting

1.  Leah has several hundred data files, each of which is formatted like this:

    ~~~
    2013-11-05,deer,5
    2013-11-05,rabbit,22
    2013-11-05,raccoon,7
    2013-11-06,rabbit,19
    2013-11-06,deer,2
    2013-11-06,fox,1
    2013-11-07,rabbit,18
    2013-11-07,bear,1
    ~~~

    Write a shell script called `species.sh` that takes any number of
    filenames as command-line parameters, and uses `cut`, `sort`, and
    `uniq` to print a list of the unique species appearing in each of
    those files separately.

2.  Write a shell script called `longest.sh` that takes the name of a
    directory and a filename extension as its parameters, and prints
    out the name of the file with the most lines in that directory
    with that extension. For example:

    ~~~
    $ bash longest.sh /tmp/data pdb
    ~~~

    would print the name of the `.pdb` file in `/tmp/data` that has
    the most lines.







 





