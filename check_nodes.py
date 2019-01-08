#!/usr/bin/env python
import json
import requests
import sys

url = 'http://oxidized.noc.netline.net.uk/nodes.json'

try:
	resp = requests.get(url=url)
except Exception as exc:
	if (exc):
		print("Check Nginx Service")
		sys.exit(2)

if resp.status_code is not 200:
	print("Oxidized Service is not Running")
	sys.exit(2)

data = resp.json()
nodes_down = []
nodes_up = []
for i in data:
	if i['status'] == "no_connection":
		nodes_down.append(i['name'])
	elif i['status'] == "success":
		nodes_up.append(i['name'])

nodes_down = ','.join(map(str, nodes_down))
if nodes_down:
	print("The following nodes are not connected: " + nodes_down)
	sys.exit(2)
else:
	sys.exit(0)

