import csv
import json

accessible_to_stop_map = csv.DictReader(open('lirr_stops.csv', 'rb'))
accessible_stop_ids = [ s["stop_id"] for s in accessible_to_stop_map if s['wheelchair_boarding'] == "1" ]

with file('accessible_stops_lirr.json', 'wb') as a:
    a.write(json.dumps(accessible_stop_ids))
