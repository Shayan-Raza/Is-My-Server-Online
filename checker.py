from ping3 import ping

#Ping server 
def ping_server(address) : 
    result = ping(address)
    return result