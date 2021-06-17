#!/usr/bin/env python
import sys
# [Define group level master information]
def reset():
# [Logic to reset master info for every new group]
# Run for end of every group
    current_vin = None
    flag = None

def flush():
# [Write the output]
     print('%s\t%s\t%s' % (vin, make, year))

# input comes from STDIN
current_vin = None
flag = None
for line in sys.stdin:
# [parse the input we got from mapper and update the master info]
    line = line.strip().split("\t")
    incident_type = line[1]
    vin = line[0]
    if(current_vin == vin or current_vin == None or flag == 2):
        if(current_vin != vin and current_vin != None):
            reset()
        current_vin == vin
        if incident_type == 'A':
            flag = 1
        elif incident_type == 'I' and flag == 1:
            make = line[2]
            year = line[3]
            flag = 2
            flush()
        elif incident_type == 'R':
            flag = 2  
            
