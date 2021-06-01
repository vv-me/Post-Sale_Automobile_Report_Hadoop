#!C:\Users\vra\Anaconda3\python.exe
import sys
# [Define group level master information]
def reset():
# [Logic to reset master info for every new group]
# Run for end of every group
    current_vin = None


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
    if(current_vin == vin or current_vin == None):
        current_vin == vin
        if incident_type != 'A' or flag == 1:
            flag = 1
        elif incident_type == 'A' or flag == 2:
            flag == 2
            if(incident_type == 'I') :
                make = line[2]
                year = line[3]
                flush()
    else:
        if incident_type == 'A':
            flag = 2 
        else:
            flag = 1
        reset()	

# # [detect key changes]
# if current_vin != vin:
# if current_vin != None:
# # write result to STDOUT
# flush()
