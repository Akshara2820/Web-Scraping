import requests,pprint,json
from bs4 import BeautifulSoup

with open("web_task_1.json","r+")as file:
    data1=json.load(file)
    # print(data1)

def group_ten_year(movies):

    details_dict={}
    movie_1960=[]
    movie_1970=[]
    movie_1980=[]
    movie_1990=[]
    movie_2000=[]

    for movies_Details in movies:
        # print(movies_Details)
        if (int(movies_Details["Year"]>=1960 and movies_Details["Year"]<=1969)):
            movie_1960.append(movies_Details)
        elif (int(movies_Details["Year"]>=1970 and movies_Details["Year"]<=1979)):
            movie_1970.append(movies_Details)
        elif (int(movies_Details["Year"]>=1980 and movies_Details["Year"]<=1989)):
            movie_1980.append(movies_Details)
        elif (int(movies_Details["Year"]>=1990 and movies_Details["Year"]<=1999)):
            movie_1990.append(movies_Details)
        else:
            movie_2000.append(movies_Details)

        details_dict["1960"]=movie_1960
        details_dict["1970"]=movie_1970
        details_dict["1980"]=movie_1980
        details_dict["1990"]=movie_1990
        details_dict["2000"]=movie_2000

    with open("10_year.json","w+")as file:
        json.dump(details_dict,file,indent=4)






group_ten_year(data1)