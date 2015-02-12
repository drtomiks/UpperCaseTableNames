# UpperCaseTableNames
A simple Python script to uppercase table names in a SQL script. (Throwback Thursday ancient script)

Back in 2007, I ran into a problem with MySQL case sensitivity going from case insensitive table names in
Windows to a production server on Linux that was configured for case sensitivity. I had a very large dump
file whose lowercased table names needed to be converted to uppercase in order for everything on the 
production server to work correctly.

I couldn’t find anything else around at the time to solve the problem, so I wrote this script. The table
names and references were all in back ticks, so the script simply uppercases anything it finds in back
ticks using regex.

I’ve inclueded a sample input file. Feel free to use this script any way you like.
