import csv
import json

accessible_to_stop_map = csv.DictReader(open('MTA_stops_with_ada_external.csv', 'rb'))
accessible_stop_ids = [ s["stop_id"] for s in accessible_to_stop_map if s['ada_tc'] == "1" ]

with file('accessible_stops.json', 'wb') as a:
    a.write(json.dumps(accessible_stop_ids))