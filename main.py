# Import collector agents
from collection import registry
from collection import *

# Run each agent
for m in registry.mods:
    m()
