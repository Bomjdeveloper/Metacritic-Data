import requests
from bs4 import BeautifulSoup as bfs
import pandas as pd

page_number = 0

#Find how many pages to scrap
request = requests.get("https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?", headers={'User-agent': 'Mozilla/5.0'})
page = bfs(request.content, "html.parser") 
last_page_number = int(page.select("li.page.last_page > a")[0].text) + 1
print(last_page_number)

#lists where we put the data
name_of_the_game = []
name_of_the_platform = []
user_score_list = []
meta_score_list = []

for a in range(last_page_number):
    #find where data
    find_title = page.find_all("a", class_="title")
    find_platform = page.find_all("div", class_="clamp-details")
    find_user_score = page.find_all("div", class_="clamp-userscore")
    find_meta_score = page.find_all("div", class_="clamp-score-wrap")

    #colect data, and put to the lists
    for title in find_title:
        name = title.find("h3")
        name_of_the_game.append(name.text)

    for platform in find_platform:
        platform_name = platform.select(".platform > span.data")
        platform_name = str(platform_name[0].text).replace(''' ''', "").replace('''
''', "")
        name_of_the_platform.append(platform_name)

    for user_score in find_user_score:
        user_score_numb = user_score.select("a > div")
        user_score_numb = str(user_score_numb[0].text)
        if user_score_numb == 'tbd':
           user_score_numb = '0' #then we will remove 0 values
        else: 
            user_score_numb = float(user_score_numb) * 10
            user_score_numb = int(user_score_numb)
        user_score_list.append(str(user_score_numb))

    for meta_score in find_meta_score:
        meta_score_numb = meta_score.select("a > div")
        meta_score_numb = int(meta_score_numb[0].text)
        meta_score_list.append(meta_score_numb)
    

    #change the page to next
    url = "https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?" + "page=" + str(page_number)
    print(url)
    request = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}) 
    page = bfs(request.content, "html.parser")
    page_number = page_number + 1

#sort data, and make csv file
data = {"Name" : name_of_the_game,
    "Platform name" : name_of_the_platform,
    "User score": user_score_list,
    "Meta score": meta_score_list}
pd.set_option('display.max_rows', None)
data_to_csv = pd.DataFrame(data)
data_to_csv.to_csv("data.csv")
print(data_to_csv)