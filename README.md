# Oxidized Scripts

## Check_Nodes.py
Nagios Script written in python to fetch Status of Nodes from oxdizied webservice "Puma". It checks for HTTP headers for reverse proxy, if no HTTP headers are
proivded it shows CIRT alert.

If the reverse proxy is online but the oxidized service has crsahed it will return CIRT as oxdized web gui is down.

When the nodes status is sent in JSON it parse to check for nodes which are down and not being monitored/backed up.

## Check Oxidized Scripts
Cron Bash script to check if oxidized web process "puma" is running or if multiple process are running. If the oxidized process is running multiple process it will kill and start new process. 

