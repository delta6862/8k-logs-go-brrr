# System imports
from scp import SCPClient
import paramiko

# Custom imports
from . import registry

class Apache:
    def __init__(self, ip=None, name=None, key_file=None):
        self.ip = ip
        self.name = name
        self.key_file = key_file
    
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
        pass
    
    def cleanup(self):
        pass

registry.register(Apache)