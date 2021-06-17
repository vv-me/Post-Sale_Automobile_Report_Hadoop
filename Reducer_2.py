#!C:\Users\vra\Anaconda3\python.exe
import sys
dict = {}
for line in sys.stdin:
    line = line.strip().split("\t")
    identify = line[0]
    num = int(line[1])
    if identify in dict.keys():
        dict[identify] += num
    else:
        dict[identify] = num    

for i in dict:
    print("%s\t%s" %(i,dict[i]))
        

