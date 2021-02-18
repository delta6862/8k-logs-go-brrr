# System imports
from scp import SCPClient
import paramiko
import os

# Custom imports
from . import registry

class Nginx:
    def __init__(self, ip=None, servername=None, key_file=None):
        self.servername = servername
        self.key_file = key_file
        self.ip = ip

    def setup(self):
        pass

    def collect(self):
        # Open the private key for the box
        pk = paramiko.RSAKey.from_private_key(open(self.key_file))

        # Login via ssh to the box
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, username="root", pkey=pk)
        # transfer the log file via scp and save it on our own box
        scp = SCPClient(ssh.get_transport())
        scp.get('/var/log/nginx/access.log', 'collectedlogs/' + self.servername + "/nginxlogs/logtmp") # change this
        scp.close()

        # We add the new lines of the logtmp to the log file

        # Open the log files
        firstlog = open(f'collectedlogs/{self.servername}/nginxlogs/log', 'r')
        newlog = open(f'collectedlogs/{self.servername}/nginxlogs/logtmp', 'r')
        newerlog = open(f'collectedlogs/{self.servername}/nginxlogs/lognew', "w")

        firstloglines = firstlog.readlines()
        newloglines = newlog.readlines()
        # Compare the two files
        for newline in newloglines:
            for oldline in firstloglines:
                if oldline == newline:
                    break
                else:
                    newerlog.write(newline + "\n")
                    break
        firstlog.close()
        newerlog.close()

        newerlog = open(f'collectedlogs/{self.servername}/nginxlogs/lognew', "r")
        firstlog = open(f'collectedlogs/{self.servername}/nginxlogs/log', 'a')   

        # append the new files from lognew to the old log file
        for line in newerlog.readlines():
            firstlog.write(line +"\n")
            
            firstlog.close()
            newlog.close()
            newerlog.close()

        # clean up
        os.remove(f'collectedlogs/{self.servername}/nginxlogs/lognew')
        os.remove(f'collectedlogs/{self.servername}/nginxlogs/logtmp')

    def healthcheck(self):
        pass

    def cleanup(self):
        pass

registry.register(Nginx)
