import paramiko
from scp import SCPClient
from . import registry_setup

class pspy64:
    def __init__(self, ip, key_file):
        self.ip = ip
        self.keyfile = key_file
        self.upload_pspy(ip, key_file)
        self.prepare_log(ip, key_file)
        self.start(ip, key_file)
  
    def upload_pspy(self, ip, key_file):
        pk = paramiko.RSAKey.from_private_key(open(key_file))

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username="root", pkey=pk)

        scp = SCPClient(ssh.get_transport())
        scp.put('/binaries/pspy64', '/bin/xjava_run')
        scp.close()

    def prepare_log(self, ip, key_file):
        pk = paramiko.RSAKey.from_private_key(open(key_file))

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username="root", pkey=pk)

        ssh.exec_command('mkdir /etc/kthread')
        ssh.exec_command('touch /etc/kthread/log')
    
    def start(self, ip, key_file):
        pk = paramiko.RSAKey.from_private_key(open(key_file))

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username="root", pkey=pk)

        ssh.exec_command('/bin/xjava_run --color=false -i 0 -f -r "/usr,/tmp,/home,/var,/opt" >> /etc/kthread/log')

registry_setup.register(pspy64)