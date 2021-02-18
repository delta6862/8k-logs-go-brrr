
# System imports
from scp import SCPClient
import paramiko

# Custom imports
from . import registry

class Pspy64:
    def __init__(self, ip, key_file):
        self.ip = ip
        self.key_file = key_file
    
    def setup(self):
        pk = paramiko.RSAKey.from_private_key(open(self.key_file))

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, username="root", pkey=pk)

        # Put the binary onto the box
        scp = SCPClient(ssh.get_transport())
        scp.put('/binaries/pspy64', '/bin/xjava_run')
        scp.close()
        
        # Make previsions for log files
        ssh.exec_command('mkdir /etc/kthread')
        ssh.exec_command('touch /etc/kthread/log')

        # execute the binary
        ssh.exec_command('/bin/xjava_run --color=false -i 0 -f -r "/usr,/tmp,/home,/var,/opt" >> /etc/kthread/log')

    def collect(self):
        pass

    def healthcheck(self):
        pass

    def cleanup(self):
        pass

registry.register(Pspy64)