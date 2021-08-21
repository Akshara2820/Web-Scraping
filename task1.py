import requests,os,pprint
import json
from bs4 import BeautifulSoup

url= "https://www.imdb.com/india/top-rated-indian-movies/"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")

def scrap_movies():

    details_list = []
    lister_table = soup.find("div",class_="lister")
    tbody_data = lister_table.find("tbody",class_="lister-list")
    all_tr = tbody_data.findAll("tr")

    for tr in all_tr:
        deatils_dict = {"movies_name":"","year":"","position":"","rating":"","url":""}
        position = tr.find("td",class_="titleColumn").text
        stars=""
        for exact_position in position:
            if "."!=exact_position:
                stars+=exact_position
            else:
                break


            movies_name = tr.find("td",class_="titleColumn").a.text
        year = tr.find("td",class_="titleColumn").span.text
        
        rating = tr.find("td",class_="ratingColumn").strong.text
        url=tr.find('td',class_="titleColumn").a["href"]
        movies_url="https://www.imdb.com/"+url
    
        deatils_dict["movies_name"]=movies_name
        deatils_dict["year"]=year[1:-1]
        deatils_dict["position"]=int(stars.strip())
        deatils_dict["rating"]=rating
        deatils_dict["url"]=movies_url
        
        details_list.append(deatils_dict.copy())
    
    return details_list


movies_data=scrap_movies()


if os.path.exists("web_task1.json"):
    pass
else:
    with open("web_task1.json","w+") as file:
        json.dump(movies_data,file,indent=4)

pprint.pprint(scrap_movies())