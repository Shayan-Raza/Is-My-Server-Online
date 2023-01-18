import json 

#Creating settings.json
def create_json() : 
    with open("settings.json", "w") as f : 
        address = input("Server Address: ")
        json_dic = {"address" : address} #Creating JSON
        json.dump(json_dic, f) #Writing to settings.JSON
