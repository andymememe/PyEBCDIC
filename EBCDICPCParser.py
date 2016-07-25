import sys
import reference

FileIn = None
FileOut = None

if len(sys.argv) < 3:
    raise Exception("Not enough arguments.")
else:
    FileIn = sys.argv[1]
    FileOut = sys.argv[2]

o = open(FileOut, 'w')

with open(FileIn, 'rt') as i:
    for line in i:
        o.write(reference.table[line.strip('\n')])
