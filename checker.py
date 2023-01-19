from settings import read_json
from ping3 import ping

#Reading JSON for address 
address = read_json() #JSON function from settings.py

#Ping server 
def ping_server(address) : 
    result = ping(address)
    return result