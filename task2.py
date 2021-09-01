import requests,json,pprint
from bs4 import BeautifulSoup


with open("web_task_1.json","r+")as data:
    data1=json.load(data)
    # pprint.pprint(data1)

def group_by_year(movies):

    details_dict={}

    for i in movies:
        # print(i)
        year1=i["Year"]
        # print(year1)
        details_list=[]
        
        for j in movies:
            if year1==j["Year"]:
                details_list.append(j)
        details_dict[year1]=details_list
        # pprint.pprint(details_dict)


        with open("year_by_task2.json","w+")as file:
            json.dump(details_dict,file,indent=4)


group_by_year(data1)
