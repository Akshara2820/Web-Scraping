import requests,os,pprint, time, random
import json
from bs4 import BeautifulSoup

with open("web_task_1.json","r+")as file:
    data1=json.load(file)


s=[]
for i in data1:
    s.append(i)
s1=s[:10]
list1=[]
for i in s1:

    url=i["Url"]
    dict1={}
    abc=random.randint(1,4)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")

    poster=soup.find("div",class_="ipc-poster").a["href"]
    
    poster1="https://www.imdb.com"+poster

    dict1["name"]=i["Movie_name"]
    dict1["poster_image_url"]=poster1
    biodata=soup.find("span",class_="GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA").text

    dict1["bio"]=biodata

    para1=soup.find_all('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    for k in para1:



        para2=k.find_all('li')

        for i in para2:
            if "Language" in i.text:
                a=i.find('a').text
                dict1["langauge"]=a
            elif 'Country of origin' in i.text:
                a=i.find('a').text
                dict1["country"]=a

    para1=soup.find('div', class_="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr")
    para=para1.find_all('li')
    para3=para[-1].text.split(' ')


    k=para3[0][0]
    if (len(para3)) >1:

        k1=para3[1].split('m')
        runtime=(int(k)*60)+int(k1[0])
    else:
        runtime=(int(k)*60)




    dict1['runtime']=runtime

    dram=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all Storyline__StorylineMetaDataList-sc-1b58ttw-1 esngIX ipc-metadata-list--base")
    # print(dram)
    namedata=dram.find_all("li",class_="ipc-metadata-list__item")
    
    l1=[]

    for j in namedata:
        if "Genre" in j.text:
            k=j.find_all('a')
            for l in k:
                l1.append(l.text)
            break
    dict1['genres']=l1

    der=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt")
    der1=der.find_all('li')
    der2=der1[0].find_all('a')

    l2=[]
    for k in der2:
        # l2.append(k.text)
        l2=(k.text)
    dict1['director']=l2
    list1.append(dict1)


with open ("task_5.json","w+")as file:
    data=json.dump(list1,file,indent=4)
    