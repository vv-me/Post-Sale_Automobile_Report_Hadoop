import sys
# input comes from STDIN (standard input)
vin_list = []
for line in sys.stdin:
   incident_id, incident_type, vin_number, make, model, year, Incident_date, description  = line.split(",")
   vin_list.append([vin_number,incident_type, make, year])
# [derive mapper output key values]
print(vin_list)

