import requests
from dotenv import dotenv_values
from pprint import pprint

API = "https://open-atms.airlab.aero/api/v1/"
AIRPORT = f"{API}airac/airports"
SID = f"{API}/airac/sids/airport/"
CONFIG = dotenv_values(".env")
HEADERS = {"api-key":f"{CONFIG['KEY']}"}
ICAO_WAYPOINTS = None
TEMP1 = None
TEMP2 = None
TEMP3 = None

def get_data(airport_attr):
    airports_data = requests.get(AIRPORT,headers=HEADERS).json()
    data = [dic[airport_attr] for dic in airports_data]
    return data

icao_list = get_data('icao')
ICAO_WAYPOINTS = {icao:{'SIDs':[]} for icao in icao_list}

for icao in icao_list:
    icao_data = requests.get(f"{SID}{icao}", headers=HEADERS).json()
    if len(icao_data) > 0:
        for icao_attr in icao_data:
            # Insert Waypoint into ICAO
            TEMP1 = set(list(ICAO_WAYPOINTS[icao].keys()))
            for waypoint in icao_attr["waypoints"]:
                if waypoint["name"] in TEMP1:
                    ICAO_WAYPOINTS[icao][waypoint["name"]] += 1
                else:
                    ICAO_WAYPOINTS[icao].setdefault(waypoint["name"], 1)

            ICAO_WAYPOINTS[icao]['SIDs'].append(icao_attr["name"])
            ICAO_WAYPOINTS[icao]['SIDs'] = list(set(ICAO_WAYPOINTS[icao]['SIDs']))

        # Rearrange Data
        TEMP3 = ICAO_WAYPOINTS[icao]['SIDs']

        del ICAO_WAYPOINTS[icao]['SIDs']
        TEMP1 = None

        TEMP1 = {v: k for k, v in ICAO_WAYPOINTS[icao].items()}
        TEMP2 = list(TEMP1.keys())
        TEMP2.sort(reverse=True)

        ICAO_WAYPOINTS[icao] = {'WAYPOINT_COUNT': {TEMP1[TEMP2[0]]: TEMP2[0], TEMP1[TEMP2[1]]: TEMP2[1]}, 'SIDs': TEMP3}
        TEMP1 = None
        TEMP2 = None
        TEMP3 = None
pprint(ICAO_WAYPOINTS)
