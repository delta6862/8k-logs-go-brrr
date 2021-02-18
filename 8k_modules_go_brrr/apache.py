# System imports
from termcolor import colored
from scp import SCPClient
import paramiko
import requests
import random


# Custom imports
from . import registry

class Apache:
    def __init__(self, ip=None, name=None, key_file=None):
        self.ip = ip
        self.name = name
        self.key_file = key_file
        if self.healthcheck() != "Up":
            print(colored(self.name + "[Apache]" + ":", "blue"), colored("Down", "red"))
    
    def setup(self):
        pass
    
    def collect(self):
        pk = paramiko.RSAKey.from_private_key(open(self.key_file))
        ssh = paramiko.SSHClient()
        # Bit risky maybe? But then MITM is probably not top on the threat model in an a&d ctf
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, username="root", pkey=pk)
        scp = SCPClient(ssh.get_transport())
        scp.get('/var/log/apache2/access.log.1', 'collectedlogs/apachelog' + self.name) # change
        scp.close()
    
    def healthcheck(self):
        naughty_word = random.randint(100000, 200000)
        requests.get("http://" + str(self.ip) + "/" + str(naughty_word))

        pk = paramiko.RSAKey.from_private_key(open(self.key_file))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, username="root", pkey=pk)
        _, stdout, _ = ssh.exec_command("cat /var/log/apache2/access.log.1")
        if naughty_word in str(stdout):
            self.up = True
            return "Up"
        else:
            self.up = False
            return "Down"
    
    def cleanup(self):
        pass

registry.register(Apache)