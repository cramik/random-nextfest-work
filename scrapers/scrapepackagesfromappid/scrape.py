import requests
import json


with open('appids.txt', 'r') as appids:
	for appid in appids:
		receive=requests.get(f'https://store.steampowered.com/api/appdetails?appids={appid}')
		jsonn = json.loads(receive.text) 
		try:
			for package in jsonn[appid[:-1]]["data"]["packages"]:
				print(package)
		except:
			pass