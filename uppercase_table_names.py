# uppercase_table_names.py
#
# utility script to find and uppercase all
# table names and references in mysql sql
# script. this actually uppercases anything
# in back ticks which is fine for my purposes
#
# feel free to use this script anyway you like
# -- drtomiks 2007-08-19


# see http://www.amk.ca/python/howto/regex/
# for more about using regular expressions in python
import re

def make_uppercase (match):
    input_string = str(match.group())
    return input_string.upper()

print "Beginning Program\n"

output_file=open("outputfile.sql", "w")
output_file.write("-- Uppercased Output\n")

# complile regular expression to look for
search_pattern = re.compile(r"`(.[^`]*)`", re.VERBOSE)

input_file = open("inputfile.sql")
for line in input_file.readlines():
    # find and replace
    edited_line = search_pattern.sub(make_uppercase,line)
    output_file.write(edited_line)
    print edited_line
    

input_file.close
output_file.close
print "Program Completed\n"
