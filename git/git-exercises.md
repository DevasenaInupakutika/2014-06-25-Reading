#Git Exercises

##Pre-Lesson

Create a new directory, called `git-project`, NOT inside the directory we used yesterday.  
Then copy the files from yesterday's Git directory to this one.  You can do this using your mouse, or, 
if you're feeling brave, using shell commands.  A sample series of commands might be: 

~~~
$mkdir git-project

$cp ~/Desktop/2014-06-25-Reading/Git/* git-project/
~~~

Look around at the files you've just moved.  If you have time, please make an account on GitHub - we'll need it later in the lesson.  

##Notes on local commands, part 1

Open the `git-commands.md` document and take notes on the various commands we've used so far.  

##Shell review

If you're feeling adventurous, try to modify the `stats-script` file so that instead of placing results in a single output file, each result from an input file gets sent to a file named `stats-$datafile`.  

##Remote practice

Edit the README so that it's more descriptive, then commit and push changes to your repository.  

##Remotes and automation

What if you wanted to work on material in someone else’s directory/repository that's hosted online?  Which shell/git commands would you need to "download" the other person's repository onto your computer?  

Hint 1: This should take around 5 commands

Hint 2: There are 2 shell and 3 git commands.  

Hint 3: The sequence of events is a) create a directory to store the files, b) move into that directory, c) initialize that directory as a repository, d) link the other person's remote repository and your local repository, e) move the files from that remote to your local.  

##Collaboration

Pair up with someone next to you.  Go out of `project_files` into `git-project`.  Then clone your neighbor's repository to your computer using:

~~~
git clone (https://github.com/ ... ) (name for their directory)
~~~

Go into the cloned repository (use `cd`) and add a file named "paper.txt", with a title and both of you listed as authors.  Stage + commit the file.  Now try pushing to their repository (which should be named `origin`).  What happens?  

##Collaboration, part 2

After your partner has added you to their repository on github, try pushing again.  Look at what your partner has pushed to your online repository.  How do you get their additions to your files into your local copy?  

##Collaboration, part 3... ?  