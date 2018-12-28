import string
from bs4 import BeautifulSoup
import requests
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["espn"]

mycol = mydb["cric_info"]

list_1 = [i for i in string.ascii_uppercase]

for item in list_1:
    source = requests.get("http://www.espncricinfo.com/ci/content/player/country.html?country=6;alpha={}".format(item)).text

    soup = BeautifulSoup(source, 'lxml')

    rows = soup.find("table").find_all('tr')


    if(item == "X"):
        continue

    for row in rows:
        res = row.find('td', class_="ciPlayernames")
        name = res.a.text.strip()
        id = res.a['href'].split('/')[-1].strip('.html')
        # print("{}: {} :{}".format(name, id, "espncricinfo"))

        if (mycol.find({"id": id}).count() > 0):
            print("item already exists")
        else:
            mycol.insert_one({"name": name, "id": id, "platform": "espncricinfo"})


    print("*"* 30   )