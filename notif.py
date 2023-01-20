from plyer import notification
import time

def notify(address) : 
    #Creating Notification 
    notification.notify(
        title = "Your server is down" , 
        message = f"{address} could not be reached"
    )
    
    #Creating a result in the shell
    print(f"Server is down. {time.ctime()} ")