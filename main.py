# .py from the project
from settings import create_json, read_json
from notif import notify
from checker import ping_server

# Libraries 
import os 
import time

# Creating JSON file
# Skipping if settings.json already exists 
if os.path.exists("settings.json") : 
    pass
else: 
    create_json()

address = read_json() #Reading server address from JSON above

#Pinging server
while True : 
    if ping_server(address=address) == "Failed to ping server" :
        print("""
An error occured:
Pls check if the script is running in sudo or has admin privileges
        """)
        break
    elif str(ping_server(address=address)) == "False" : 
        notify(address=address)
        break
    else : 
        print(f"Delay to server {ping_server(address=address)}")
        time.sleep(10)