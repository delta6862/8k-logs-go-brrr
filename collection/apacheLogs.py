import paramiko
from scp import SCPClient
from . import registry_collection

class apache_logs:
  def __init__(self, ip, servername, key_file):
    self.ip = ip
    self.servername = servername
    self.key_file = key_file
    self.get_logs(ip, servername, key_file)
  
  def get_logs(self, ip, servername, key_file):

    pk = paramiko.RSAKey.from_private_key(open(key_file))

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(self.ip, username="root", pkey=pk)


    scp = SCPClient(ssh.get_transport())
    scp.get('/var/log/apache2/access.log.1', 'collectedlogs/apachelog' + self.servername) # change
    scp.close()

registry_collection.register(apache_logs)
