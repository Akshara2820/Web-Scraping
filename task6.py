import requests,pprint,json
from bs4 import BeautifulSoup

with open("task_5.json","r+")as file:
    data=json.load(file)

def movie_language(lan_data):

    details_dict={}

    for i in lan_data:
        language_1=i["langauge"]
        details_list=[]

        for j in lan_data:
            if language_1==j["langauge"]:
                details_list.append(j)
        details_dict[language_1]=details_list


        with open("task_6.json","w+")as data1:
            json.dump(details_dict,data1,indent=4)

movie_language(data)



