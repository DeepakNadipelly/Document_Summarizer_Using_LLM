# import requests
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
# comment_list = list()
# for pag in range(1, 3):
#     print("here")
#     time.sleep(5)
# URL = "https://www.yelp.com/biz/the-cortez-raleigh?osq=Restaurants&start="+str(pag*10)+"&sort_by=rating_asc"
# print('downloading page ', pag*10)
# page = requests.get(URL)
# #next step: parsing
# soup = BeautifulSoup(page.content, 'lxml')
# for comm in soup.find("yelp-react-root").find_all("p", {"class" : "comment__09f24__D0cxf css-qgunke"}):
#     comment_list.append(comm.find("span").decode_contents())
#     print(comm.find("span").decode_contents())
# pd.DataFrame([comment_list]).T.to_csv("yelp.csv")
import requests
from bs4 import BeautifulSoup
import time

def scrape_yelp_reviews(url):
    comment_list = []

    # Extract the page number from the URL
    page_number = 1
    if "start=" in url:
        page_number = int(url.split("start=")[1].split("&")[0]) // 10

    # Iterate through pages (modify the range as needed)
    for pag in range(page_number, page_number + 2):  # Adjust the range as needed
        time.sleep(5)
        # URL = url.split("&start=")[0] + "&start=" + str(pag * 10) + "&sort_by=rating_asc"
        page = requests.get(url)
        
        # Parse the page content
        soup = BeautifulSoup(page.content, 'lxml')
        
        # Extract comments
        for comm in soup.find("yelp-react-root").find_all("p", {"class": "comment__09f24__D0cxf css-qgunke"}):
            comment_list.append(comm.find("span").decode_contents())
            print(comm.find("span").decode_contents())

    # Join the comments into a single string
    joined_comments = ' '.join(comment_list)
    return joined_comments

# Example usage
yelp_url = "https://www.yelp.com/biz/the-cortez-raleigh"
scraped_text = scrape_yelp_reviews(yelp_url)
print(scraped_text)


