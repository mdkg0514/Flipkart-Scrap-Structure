from bs4 import BeautifulSoup
from selenium import webdriver
import time
driver = webdriver.Chrome()
import pandas as pd
url = "https://www.flipkart.com"
for x in range(1):
    baseurl = f"https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Sports+Shoes&page={x}"
    driver.get(baseurl)
    time.sleep(5)
    response = driver.page_source
    soup = BeautifulSoup(response, "html.parser")
    products = soup.find_all("div", class_="_13oc-S")
    list = set()
    for item in products:
        links = item.find_all("a")
        for link in links:
            list.add(url + link['href'])
titles_list = []
discounted_price_list = []
actual_price_list = []
review_list = []
for urls in list:
    driver.get(urls)
    responses = driver.page_source
    soups = BeautifulSoup(responses,"html.parser")
    titles = soups.find("span",class_ = "B_NuCI")
    titles_list.append(titles.text)
    discounted_price = soups.find("div",class_ = "_30jeq3 _16Jk6d")
    discounted_price_list.append(discounted_price.text)
    actual_price = soups.find("div",class_ = "_3I9_wc _2p6lqe")
    actual_price_list.append(actual_price.text)
    try:
        review = soups.find("div",class_ = "_3LWZlK _3uSWvT")
        review_list.append(review.text)
    except:
        review = None
dic = {
    "Title":titles_list,
    "Discounted Price":discounted_price_list,
    "Actual Price":actual_price_list,
    "Review":review_list
}
df = pd.DataFrame(dic)
df.to_csv("Flipkart.csv",index=False)
print(df.head())