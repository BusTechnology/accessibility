#!/usr/bin/python

import csv
import re
import untangle

accessibility = untangle.parse("http://advisory.mtanyct.info/eedevwebsvc/allequipments.aspx")

accessibility = accessibility.NYCEquipments

output = []

pattern = re.compile(',\s*|&\s*')
paren_pattern = re.compile('\(|\)')

for e in accessibility.equipment:
    if e.ADA == 'Y':
        serving = e.serving.cdata.strip()
        serving = re.sub(pattern,'', serving)
        serving = re.sub(paren_pattern, ' ', serving)
        o = { 
            'stop_name' : e.station.cdata,
            'borough' : e.borough.cdata,
            'lines' : e.trainno.cdata, 
            'serving' : serving
        }
        output.append(o)

with open('accessible_stations.csv', 'wb') as w:
    writer = csv.DictWriter(w, delimiter=',', fieldnames= output[0].keys())
    
    writer.writeheader()
    for row in output:
        writer.writerow(row)
