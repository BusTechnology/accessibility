#!/usr/bin/python
"""
Compare two lists of accessible stations. 
Because there are stations with duplicate names (e.g. 72 St for 1/2/3 and 72 St for Q), this is more of a sanity check than an exhaustive matching process.
It will point to 
"""

#how could you not love a library called fuzzywuzzy?!?
from fuzzywuzzy import process
import csv

accessible_to_stop_map = csv.DictReader(open('MTA_stops_with_ada_external.csv', 'rb'))
accessible_to_stop_map_names = [ s["stop_name"] for s in accessible_to_stop_map if s['ada_tc'] == "1" ]
matched = []
unmatched = []

with open('accessible_stations.csv','rb') as a:
    accessible_stations = csv.DictReader(a)
    stations = [ s["stop_name"] for s in accessible_stations ]
    for s in stations:
        accessible = process.extract(s, accessible_to_stop_map_names, limit=1)
        if len(accessible) == 0:
            unmatched.append(accessible)
        else:
            matched.append(accessible)

print " completed matching:"
print "total matched " + str(len(matched))
print "total unmatched" + str(len(unmatched))
if len(unmatched) > 0:
    print "unmatched stations:"
    print ",".join(unmatched)