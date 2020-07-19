"""Build an index mapping word -> list of occurrences"""

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
# parse current python script file
with open(sys.argv[0], encoding='utf-8') as fp:
    # enumerate function assigns an index(starts is defined by 1 below) to each item in an iterable object(fp below)
    for line_no, line in enumerate(fp, 1):
        # finditer() finds all substrings where the RE matches, and returns a sequence of "match object" instances as an iterator
        for match in WORD_RE.finditer(line):
            # group() returns the string matched by the RE
            word = match.group()
            # start() returns the starting position of the match
            column_no = match.start()+1
            location = (line_no, column_no)

            # !!! this is ugly; coded like this to make a point
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            index.setdefault(word, []).append(location)

# print in alphabetical order
for word in sorted(index, key=str.upper):  # <4>
    print(word, index[word])
