import paramiko
from scp import SCPClient


class apache_logs:
  def __init__(self, ip, servername):
    self.ip = ip
    self.servername = servername
  
  def get_logs(self):
    privatekey = "rootprivkey.txt"

    pk = paramiko.RSAKey.from_private_key(open(privatekey))


    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(self.ip, username="root", pkey=pk)


    scp = SCPClient(ssh.get_transport())
    scp.get('/var/log/apache2/access.log.1', 'collectedlogs/apachelog' + self.servername)
    scp.close()
