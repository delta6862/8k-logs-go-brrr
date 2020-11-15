# Import collector agents
from collection import registry_collection
from collection import *

# Import setup agents
from setup import registry_setup
from setup import *

import configparser
import os

config = configparser.ConfigParser()
config.read('8k-configs-go.brrr')

privkey = config['General']['key_file']

# Run each collection agent
for fortress in config['Blue-Fortress-IP']:
    for m in registry_collection.collection_mods:
        m(config['Blue-Fortress-IP'][fortress], fortress, privkey)

        
