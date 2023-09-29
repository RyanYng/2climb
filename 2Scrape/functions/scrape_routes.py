import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

''' A collection of functions to scrape the route data in a given bouldering location'''

def find_crag_title(soup):
    title = soup.find('title')
    str = title.text.split("|")[0]
    location = str.split("in")[1]
    return location

def find_crag_routes(soup,title):
    routes = soup.find_all("tr",{"data-nodename": True})
    route_data = []
    for i in range(len(routes)):
        route_data.append(title + routes[i].text)

    route_data = [i.split("\n") for i in route_data]

    for list in range(len(route_data)):
        sub_list = route_data[list]
        route_data[list] = [i for i in route_data[list] if i]
    
    return route_data

def create_crag_df(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    title = find_crag_title(soup)
    data = find_crag_routes(soup,title)
    crag_df = pd.DataFrame(data, columns = ['location','grade','route','class'])

    return (crag_df,title)








