#!C:\Users\vra\Anaconda3\python.exe
import sys
for line in sys.stdin:
    line = line.strip().split("\t")
    make = line[1]
    year = line[2]
    print('%s\t%s\t%d' %(make,year,1))