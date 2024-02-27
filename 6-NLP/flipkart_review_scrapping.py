# -*- coding: utf-8 -*-
""" Extracting reviews from flipkart """

from bs4 import BeautifulSoup as bs
import requests

link = "https://www.flipkart.com/realme-c53-champion-black-128-gb/p/itm5df90168ecd05?pid=MOBGQY9378PDVDDC&lid=LSTMOBGQY9378PDVDDC216OJI&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_2&otracker=browse&fm=organic&iid=47f04b27-9885-44d8-bbbb-fde6b4347900.MOBGQY9378PDVDDC.SEARCH&ppt=browse&ppn=browse&ssid=u3wrs4fexc0000001701745721922"
page = requests.get(link)
page
page.content
soup = bs(page.content,'html.parser')
print(soup.prettify())

###############################################################################

#scrap the review title
title = soup.find_all('p',class_="_2-N8zT")
title
review_title = []
for i in range(0,len(title)):
    review_title.append(title[i].get_text())

review_title
len(review_title)
#we got 10 titles

###############################################################################

#scrap the rating
rating = soup.find_all('div',class_="_3LWZlK _1BLPMq")
rating
rate = []
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())

rate
len(rate)
#we have get 10 ratings

###############################################################################

#scrap the review body
review = soup.find_all('div',class_="t-ZTKy")
review
body = []
for i in range(0,len(review)):
    body.append(review[i].get_text())

body
len(body)
#we got 10 review body

###############################################################################

#now we have to save the data into csv file
import pandas as pd
df = pd.DataFrame()
df['Review_Title'] = review_title
df['Rate'] = rate
df['Review'] = body
df

#create csv file
df.to_csv("flipkart_review.csv")

###############################################################################

#sentiment analysis
from textblob import TextBlob 

#polarity checking
sent = "This is very excellent garden"
pol = TextBlob(sent).sentiment.polarity
pol

#find polarity for each review we taken
df = pd.read_csv("flipkart_review.csv")
df['Polarity'] = df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['Polarity']
