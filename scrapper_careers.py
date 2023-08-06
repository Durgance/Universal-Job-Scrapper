import re
import json
import requests
from bs4 import BeautifulSoup

data = []

def scrape():
    response = requests.get(
    url='https://proxy.scrapeops.io/v1/',
    params={
        'api_key': 'get the api from the above url or directly get it from the above website',
        'url': 'link for the url you are trying to scrape, if the site have blocked any scraper', 
    },
    )

    # print('Response Body: ', response.content)
    print(response)
    html_content = response.text
    # print(html_content)
    soup = BeautifulSoup(html_content,'html.parser')
    links = soup.find_all("a",{"class":"css-bNzNOn"}) # Give the tag or class if the tag in which the given job is present
    BOW = ["data","science","scientist","machine","learning","deep","learning","engineer"]
    """
    This list represents the bag of word if found in the job title will be mailed to the respective email id 
    in the mailer.py 
    """

    for link in links:
        position = link.text.lower()
        position = re.sub(r'[^\w\s]','',position)
        print(position)   
        for bag in BOW:
            if bag in position:
                data.append(link)  

    return data

    

    

