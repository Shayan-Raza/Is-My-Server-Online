from ping3 import ping

#Ping server 
def ping_server(address) : 
    try: 
        result = ping(address)
        return result
    except: 
        print("Failed to ping server")