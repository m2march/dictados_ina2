import os
import sys
import music21 as m21

if len(sys.argv) < 2:
    print 'Usage: {} abc_file'.format(sys.argv[0])
    exit()

s = m21.converter.parseFile(sys.argv[1])
s.write('lily.pdf', sys.argv[1].replace('abc', 'ly'))
os.remove(sys.argv[1].replace('abc', 'ly'))
os.rename(sys.argv[1].replace('abc', 'ly.pdf'),
        sys.argv[1].replace('abc', 'pdf'))

