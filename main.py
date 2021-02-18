# System imports
import configparser
import os

# Custom imports
from fortress import *

# Parse configuration file
config = configparser.ConfigParser()
config.read('8k-configs-go.brrr')

fortresses = []

for fortress in config['Blue-Fortress-IP']:
    fortresses.append(
        fortress.Fortress(
        name=fortress, 
        ip=config['Blue-Fortress-IP'][fortress], 
        key_file = config['General']['key_file']
        )
    )

        
