from bs4 import BeautifulSoup  as bs
import requests
import pandas as pd

stars_url='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(stars_url)
print(page)

soup=bs(page.text,'html.parser')
table= soup.find_all('table')
temp_list=[]
table_rows=table[4].find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)

names=[]
distance=[]
radius=[]
mass=[]

for i in range(1,len(temp_list)):
    names.append(temp_list[i][0])
    radius.append(temp_list[i][8])
    mass.append(temp_list[i][7])
    distance.append(temp_list[i][5]) 
    
df2=pd.DataFrame(list(zip(names,distance,radius,mass)),columns=['star_name','mass','radius','distance'])
print(df2)
df2.to_csv("dwarf_stars.csv")