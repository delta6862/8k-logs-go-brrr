# Import collector agents
from collection import registry as registry
from collection import nginxLogs
from collection import apacheLogs

import os

privkey = open("rootprivkey.txt").read()

#read the ips from the ip list
ips = open("blue-ips.txt").readlines()

#read the names from the name list
names = open("blue-names.txt").readlines()

# make the different nginxlog objects
nginxlog1 = nginxLogs.nginx_logs(ips[0].rstrip(), names[0].rstrip())
nginxlog2 = nginxLogs.nginx_logs(ips[1].rstrip(), names[1].rstrip())
nginxlog3 = nginxLogs.nginx_logs(ips[2].rstrip(), names[2].rstrip())
nginxlog4 = nginxLogs.nginx_logs(ips[3].rstrip(), names[3].rstrip())

#get them logs
nginxlog1.get_logs()
nginxlog2.get_logs()
nginxlog3.get_logs()
nginxlog4.get_logs()

# make apache logs objects
apachelog1 = apacheLogs.apache_logs(ips[0].rstrip(), names[0].rstrip())
apachelog2 = apacheLogs.apache_logs(ips[1].rstrip(), names[1].rstrip())
apachelog3 = apacheLogs.apache_logs(ips[2].rstrip(), names[2].rstrip())
apachelog4 = apacheLogs.apache_logs(ips[3].rstrip(), names[3].rstrip())

# get them logs
apachelog1.get_logs()
apachelog2.get_logs()
apachelog3.get_logs()
apachelog4.get_logs()

# Run each agent
#for m in registry.mods:
 #   m()

        
