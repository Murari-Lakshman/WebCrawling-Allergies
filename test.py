# Making a python file to get all the links from a page
# Importing Required Modules
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Setting the URL
url = "http://research.bmh.manchester.ac.uk/informall/allergenic-foods/"
r = requests.get(url)  # Loading the page in the Memory
content = r.content

# Setting the parser

soup = BeautifulSoup(content, 'html.parser')

# Finding the element that contains all the links

anchor = soup.find(id='content')
final_link = anchor.find_all('a')  # Filtering the links from all the other elements

all_links = set()  # Creating a set to store all the links

# Using for loop to make a link

for link in final_link:
    link_text = "http://research.bmh.manchester.ac.uk" + link.get('href')
    all_links.add(link_text)  # Adding all the links to the SET

df = pd.DataFrame(all_links)  # Using pandas to create a dataframe df

df.to_csv('test.csv', index=False)  # Writing all the links to file called test.csv
