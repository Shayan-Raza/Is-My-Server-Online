import json 

#Creating settings.json
def create_json() : 
    with open("settings.json", "w") as f : 
        address = input("Server Address (Ex: 192.168.1.180): ")
        json_dic = {"address" : address} #Creating JSON
        json.dump(json_dic, f, indent=4) #Writing to settings.JSON

#Reading the saved JSON
def read_json() : 
    with open("settings.json", "r") as f : #Opening settings.json file
        address = json.load(f) #Loading JSON file
        address = address["address"] #Retrieving the address from the JSON
        return address 