import json,requests,pprint
from bs4 import BeautifulSoup

with open ("task_5.json","r+")as file:
    data=json.load(file)

def data_director(dir_movie):
    details_dict={}

    for i in dir_movie:
        dir_name=i["director"]
        
        dir_change=(str(dir_name))
        list_1=[]


        for j in dir_movie:
            if dir_change==j["director"]:
                list_1.append(j)
        details_dict[dir_change]=list_1
        print(details_dict)

    with open("task_7.json","w+")as file:
        json.dump(details_dict,file,indent=4)


data_director(data)
