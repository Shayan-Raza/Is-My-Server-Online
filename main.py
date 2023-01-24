# .py from the project
from settings import create_json, read_json
from notif import notify
from checker import ping_server

# Libraries 
import os 

# Creating JSON file
# Skipping if settings.json already exists 
if os.path.exists("settings.json") : 
    pass
else: 
    create_json()

address = read_json() #Reading server address from JSON above