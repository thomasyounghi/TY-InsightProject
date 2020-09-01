import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re
import time
import random
import json
import pandas as pd

def scraperecentyelpreviews(aliases,firstidx,lastidx,upperlimit,proxies,delay1,delay2):
    resultList = []
    for i in range(firstidx,lastidx):
        print('i')
        print(i)
        alias = aliases[i]
        print(alias)
        baseurl = 'http://www.yelp.com/biz/' + alias + '?start='
        start = 0


        while(start < upperlimit):
            url = baseurl + str(start) + '&sort_by=date_desc'
            print(url)
            page = requests.get(url,proxies=proxies,verify=False)
            soup = BeautifulSoup(page.text,'html.parser')
            reviews = soup.find_all('div',{'itemprop':'review'})
            print('len(reviews)')
            print(len(reviews))

            #an alternative way the review information could be contained
            reviews1 = []
            if len(reviews) == 0:
                reviews2 = soup.find_all('script',{'type':'application/ld+json'})
                for k in range(len(reviews2)):
                    info = [desc.strip() for desc in reviews2[k].descendants if type(desc) == NavigableString]
                    info1 = json.loads(info[0])
                    if 'review' in info1:
                        reviews1 = info1['review']

            if len(reviews) != 0:
                for review in reviews:
                    #get the rating
                    rating = review.find('div',{'itemprop':'reviewRating'})
                    rat = rating.find("meta")['content']

                    #get the date
                    date = review.find('meta',{'itemprop':'datePublished'})
                    dat = date['content']

                    txt = review.find('p',{'itemprop':'description'})
                    print('date')
                    print(dat)
                    resultList.append([i,alias,dat,rat,txt.contents[0]])
            elif len(reviews1) != 0:
                print('lenreviews1')
                print(len(reviews1))
                for review in reviews1:
                    rat = review['reviewRating']['ratingValue']
                    dat = review['datePublished']
                    if i % 5 == 0:
                        print(dat)
                    txt = review['description']
                    resultList.append([i,alias,dat,rat,txt])
                    reviews1=[]
            else:
                print('no more reviews')
                print('current start')
                print(start)
                reviews1=[]
                break
            start = start + 20
            time.sleep(delay1 + random.uniform(0,delay2))

    resultdf = pd.DataFrame(resultList)
    resultdf.columns = ['idx','alias','date','rating','reviewtxt']
    resultdf.head(40)
    return(resultdf)


