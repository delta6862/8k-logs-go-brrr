from 8k_modules_go_brrr import registry
from 8k_modules_go_brrr import *

class Fortress:
    def __init__(self, name=None, ip=None, key_file=None):
        self.name = name
        self.ip = ip
        self.key_file = key_file
        self.modules = []
        for module in 8k_modules_go_brrr.registry.modules:
            self.modules.append(module(name=self.name, ip=self.ip, key_file=self.key_file))
    
    def setup(self):
        for module in self.modules:
            module.setup()

    def collect(self):
        for module in self.modules:
            module.collect()

    def healthcheck(self):
        for module in self.modules:
            module.healthcheck()

    def cleanup(self):
        for module in self.modules:
            module.cleanup()