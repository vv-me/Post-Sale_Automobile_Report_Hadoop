import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    incident_id,vin_number = line.split(",")
    print(incident_id,"vidya",vin_number) 
    #incident_id, incident_type, vin_number, make, model, year, Incident_year, description= line.split(",")
# [derive mapper output key values]
print ('%s\t%s' % (vin_number, incident_id))

