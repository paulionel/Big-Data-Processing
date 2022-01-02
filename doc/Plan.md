*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions

I will be creating a program that will deal with what is known as "Big Data processing"
Basically I need to be able4 to process a lot of data and print certain info based on
that data.

Goal: learn how to use dictionaries, and how to only include certain keys.

I think it should only loop throught the data once because there is so much, so keep that in mind

# 1.  System Analysis

This is going to be a command line program so the user will input the directory and 
the code will take care of the rest. There should be any further user input after this.
The output will be given by printing a report.

All data that I aquire will be sent to this report.

Output must mactch exactly what Is expected. KEEP THIS IN MIND.

How this program should work:
input is given from user as a directory, I hardcode the file name after making sure
everything is valid, it then gets opened and turned into a dictionary.
dictionary is then iterated throuh and deletes the items I don't want.
some  values are initialized. Loops through the data comparing fips, and adds to the 
initialized values. Values are then sent to the report to be printed to the main.py file.


# 2.  Functional Examples

I did this on a white board.


# 3.  Function Template

pseudocode can be seen in the src file.

# 4.  Implementation

this was done in the src files.

The thing that took me the longest to figure out was how to delete items from the dictionary.
I had some code written and it didn't work. So I was looking online when I saw a better way.
I used that as inspiration for my own code.


# 5.  Testing

Testing ran pretty smoothly. When I first ran the full data set, I had forgotten to change the items in
a list to floats so that they could be compared, so I had to go through and change like 20 different things
to a float so that it would work. After that all the numbers were right, but the formating was wrong, so
I played with that a bit and tried using .rstrip, but I don't think that works for ' " ' so i used replace instead.
everything is working now.