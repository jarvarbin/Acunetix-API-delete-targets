#Dudas preguntar a juan
import requests
import json
import datetime
from dateutil.parser import parse
import sys


api_url = 'FILL ME'
api_key = 'FILL ME'
#el tiempo se cambia aqui en weeks
one_week_ago = datetime.datetime.now() - datetime.timedelta(weeks=1)
headers = {"X-Auth": api_key, "Content-Type": "application/json"}
response = requests.get(f"{api_url}/targets", headers=headers, verify=False)
if response.status_code != 200:
    print(f"Error al obtener targets: {response.status_code}")
    exit()

# Iterar sobre los targets y eliminar aquellos anteriores a la fecha límite
targets = json.loads(response.text)
targets = targets.get("targets")
for target in targets:
    print(target)
    target_id = target.get("target_id")
    if not target_id:
        continue
    created_time_str = target.get("last_scan_date")	
    if not created_time_str:
	    argumento = sys.argv
	    if len(argumento)>1:
	        argumento = argumento[1]
	        print(argumento)
	        response = requests.delete(f"{api_url}/targets/{target_id}", headers=headers, verify=False)
	        if response.status_code != 204:
	            print(f"Error al eliminar target {target_id}: {response.status_code}")
	        else:
	            print(f"Target sin escanear {target_id} eliminado")
    continue
    #created_time = parse(created_time_str)
    created_time = datetime.datetime.strptime(created_time_str.split(".")[0], '%Y-%m-%dT%H:%M:%S')
    print(created_time)
    print(one_week_ago)
    if created_time < one_week_ago:
        response = requests.delete(f"{api_url}/targets/{target_id}", headers=headers, verify=False)
        if response.status_code != 204:
            print(f"Error al eliminar target {target_id}: {response.status_code}")
        else:
            print(f"Target {target_id} eliminado")

