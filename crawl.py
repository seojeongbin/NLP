from selenium import webdriver
from bs4 import BeautifulSoup
import time, os
from datetime import datetime
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

### 0. 크롤링 문법
'''
elements by class name() [0]
클래스가 없는 경우
elements by css selector
- id의 경우 ('#~~')
- class는 앞에.
- 보라색은 그냥 (' ')
- 포함관계는 띄어쓰기 하면됨 (#react-reet form) 이런식이면 id가 react-reet이면서 form보라색 태그인 아이
'''

# ======== params =========
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(r'C:\Users\서정빈\Desktop\crawling\chromedriver.exe', chrome_options=options) # 크롬드라이버 위치
home = "https://news.naver.com/main/list.naver?mode=LS2D&sid2=259&sid1=101&mid=shm&date=20220528&page=1" # 분석대상 사이트
sleep_time = 2
# ======== params =========


def go_home() :
    driver.get(home)
    time.sleep(sleep_time) # click이나 get 등 사이트 이동 할때는 항상 time.sleep


def crawl(article) :

    article.click()
    time.sleep(sleep_time) 
    article = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div')
    soup = BeautifulSoup(article.get_attribute('innerHTML'), 'html.parser')
    content = soup.find('div', class_= 'go_trans _article_content')

    print(content.text)
    go_home()


if __name__ == "__main__" : 
    go_home()
    article = driver.find_elements_by_css_selector('ul li dl a')[0] 
    crawl(article)

    # articles = driver.find_elements_by_css_selector('ul li dl a')
    
    # for article in articles :
    #     crawl(article)
    

