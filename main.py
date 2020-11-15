# Import collector agents
from collector import registry
from collector import *

# Run each agent
for m in registry.mods:
    m()
