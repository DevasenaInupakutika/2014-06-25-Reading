---
layout: lesson
root: ../..
title: Introducing the Shell
---


#### Objectives
*   Explain how the shell relates to the keyboard, the screen, the operating system, and users' programs.
*   Explain when and why command-line interfaces should be used instead of graphical interfaces.

Josie Taylor, a biologist along with Nathan Ahmed, a robotics Engineer who captured 3D stereoscopic images of the species,
has just returned from a six-month survey of the
species detected by Mars Curiosity Rover in Mars,
where she has been sampling life existing on Mars.
She has 300 samples in all, and now needs to:

1.  Run each sample through an assay machine
    that will measure the relative abundance of 300 different proteins.
    The machine's output for a single sample is
    a file with one line for each protein.
2.  Calculate statistics for each of the proteins separately
    using a program her supervisor wrote called `goostat`.
3.  Compare the statistics for each protein
    with corresponding statistics for each other protein
    using a program one of the other graduate students wrote called `goodiff`.
4.  Write up.
    Her supervisor would really like her to do this by the end of the month
    so that her paper can appear in an upcoming special issue of *Mars Goo Letters*.

It takes about half an hour for the assay machine to process each sample.
The good news is,
it only takes two minutes to set each one up.
Since her lab has eight assay machines that she can use in parallel,
this step will "only" take about two weeks.

The bad news is that if she has to run `goostat` and `goodiff` by hand,
she'll have to enter filenames and click "OK" 45,150 times
(300 runs of `goostat`, plus 300&times;299/2 runs of `goodiff`).
At 30 seconds each,
that will take more than two weeks.
Not only would she miss her paper deadline,
the chances of her typing all of those commands right are practically zero.

The next few lessons will explore what she should do instead.
More specifically,
they explain how she can use a command line
to automate the repetitive steps in her processing pipeline
so that her computer can work 24 hours a day while she writes her paper.
As a bonus,
once she has put a processing pipeline together,
she will be able to use it again whenever she collects more data.

#### What and Why


A shell is a program like any other.
What's special about it is that its job is to run other programs
rather than to do calculations itself.
The most popular Unix shell is Bash,
the Bourne Again SHell
(so-called because it's derived from a shell written by Stephen Bourne&mdash;this
is what passes for wit among programmers).
Bash is the default shell on most modern implementations of Unix,
and in most packages that provide Unix-like tools for Windows.

Using Bash or any other shell
sometimes feels more like programming than like using a mouse.
Commands are terse (often only a couple of characters long),
their names are frequently cryptic,
and their output is lines of text rather than something visual like a graph.
On the other hand,
the shell allows us to combine existing tools in powerful ways with only a few keystrokes
and to set up pipelines to handle large volumes of data automatically.
In addition,
the command line is often the easiest way to interact with remote machines.
As clusters and cloud computing become more popular for scientific data crunching,
being able to drive them is becoming a necessary skill.



#### Key Points
*   A shell is a program whose primary purpose is to read commands and run other programs.
*   The shell's main advantages are its high action-to-keystroke ratio,
    its support for automating repetitive tasks,
    and that it can be used to access networked machines.
*   The shell's main disadvantages are its primarily textual nature
    and how cryptic its commands and operation can be.

