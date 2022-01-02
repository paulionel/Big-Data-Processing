# CS 1440 Assignment 2: Big Data Processing 

* [Instructions](instructions/README.md)
* [Hints](instructions/Hints.md)
* [Rubric](instructions/Rubric.md)
* [Installing the Text Tools](instructions/Installing_Text_Tools.md)


*Note: this file is a placeholder for your own notes.  When seeking help from
TAs or Coaches replace the text in this file with a description of your problem
and push it to your repository on GitLab*

## Resources I used to help solve problems throughout the assignment:
https://www.geeksforgeeks.org/python-ways-to-remove-a-key-from-dictionary/
https://data.bls.gov/cew/doc/titles/area/area_guide.htm
https://data.bls.gov/cew/doc/layouts/csv_annual_layout.htm
https://usu-edu.zoom.us/rec/play/YdGToVgSefUVJbBeD2ql7gCmrAI78M1D5KW2QSZmfqepO3wjYIFluWfdtZX2T8e3GihId4A8WqVkulhH.AuGfNnjs2CH8zGff
https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn2/-/blob/master/data/USA_full/area_titles.csv
https://gitlab.cs.usu.edu/erik.falor/fa20-cs1440-lecturenotes/-/blob/master/Module2/Lec16-Wed_Oct_07/mapping.py
https://gitlab.cs.usu.edu/erik.falor/fa20-cs1440-lecturenotes/-/blob/master/Module2/Lec16-Wed_Oct_07/favorite_colors.dat
https://stackoverflow.com/questions/5384914/how-to-delete-items-from-a-dictionary-while-iterating-over-it
https://www.geeksforgeeks.org/python-string-rstrip/
https://www.journaldev.com/23674/python-remove-character-from-string#python-remove-character-from-string-using-replace


## Overview

Your last project was a great success! The customer was very pleased with their
new Text Tools and so impressed with the quality of your work that they have
decided to contract you to finish the entire project for them.

Your task is to analyze a large body of data and produce a report of the
findings.  This program summarizes national employment data collected by the
U.S. Bureau of Labor Statistics in 2019.  The report consists of two sections,
a summary across all industries and a summary across the software publishing
industry.  I worked with the customer far enough to develop the format of the
report.  It is your task to analyze a 489MB CSV file to pull out the data
needed by the report.


## Objectives

-   Learn how to process a large body of data
-   Using Python's built-in string operations
-   Research programming documentation
-   Reading, understanding, and following instructions
-   Using advanced data structures (list, dictionary, set)
-   Apply problem solving strategies
    -   Divide the problem
    -   Reduce the problem
    -   Don't get frustrated
-   Exercise debugging techniques
    -   Direct debugging with the IDE
    -   Indirect debugging
    -   Wolf-Fence debugging


## Expected Behavior

Each subfolder of [data/](data) contains a file named `output.txt`.
Your program's output for that dataset should match that file exactly.

Instructions for creating the testing data sets using the Text Tools from
Assignment #1 are provided.  These crafted input files should form the basis of
your verification procedure.
