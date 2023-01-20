from ping3 import ping

#Ping server 
def ping_server(address) : 
    try: 
        result = ping(address) #Ping server with user address
        return result
    except: 
        return "Failed to ping server"