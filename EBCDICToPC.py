import sys
import reference

FileIn = None
FileOut = None

if len(sys.argv) < 3 :
    raise Exception("Not enough arguments.")
else :
    FileIn = sys.argv[1]
    FileOut = sys.argv[2]

i = open(FileIn, 'r')
o = open(FileOut, 'w')

data = i.read()

for c in data :
    for pun, val in reference.table.items() :
        if val == c :
            o.write(pun + '\n')
