# This file should only contain the logic, implementation details must be pushed into other files

# Move print help to a different file

# python3 hsearch.py "<search phrase>" "<files to include>"
# e.g.:
# python3 hsearch.py "hunt moby tartar" "/Users/H/HP/Dropbox/Kaizen/**/*.json"


import sys
import glob

search_phrase = sys.argv[1]
files_list = sys.argv[2]

# loop through each of the files

if __name__ == "__main__":
    for filename in glob.iglob(files_list, recursive=True):
        with open(filename, 'r') as myfile:


            myfile.close()

# split file into lines

# search phrase matches the lines ?

# print result

# TODO:

# indexing

# simple split at newline, split into english sentences

# simple search, regex search, fuzzy search, semantic search

