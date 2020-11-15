#import library stuff

class apache_logs:
  def __init__(self, ip, name)
    self.ip = ip
    self.name = name
    self.get_logs(ip, name)
  
  def get_logs(ip, name):
    os.system("scp -i key root@" + ip)
  
  
  
  registry.register(ssh)
