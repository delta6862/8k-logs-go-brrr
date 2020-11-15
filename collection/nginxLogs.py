import paramiko
from scp import SCPClient
from . import registry-collection


class nginx_logs:
  def __init__(self, ip, servername, key_file):
    self.ip = ip
    self.servername = servername
    self.keyfile = key_file
    self.get_logs(ip, servername, key_file)
  
  def get_logs(self, ip, servername, key_file):

    pk = paramiko.RSAKey.from_private_key(open(key_file))


    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username="root", pkey=pk)

    scp = SCPClient(ssh.get_transport())
    scp.get('/var/log/nginx/access.log', 'collectedlogs/nginxlog' + self.servername) # change this
    scp.close()

 registry-collection.register(nginx_logs)
