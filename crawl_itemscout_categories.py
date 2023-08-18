# import re
# from urllib.request import urlretrieve
# import selenium.common.exceptions
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import pyautogui
# import clipboard
# from bs4 import BeautifulSoup
# import openpyxl as xl
# import os
# import pandas as pd
# import win32com.client as win32
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import time
import zipfile
import os
from selenium.common import exceptions


url = r'https://itemscout.io/category'
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")


driver = webdriver.Chrome(options=options) # 크롬드라이버 액세스
wait = WebDriverWait(driver, 10) # 디폴트 딜레이
driver.get(url) #드라이버 실행
driver.set_window_position(0, 0)
driver.maximize_window()
time.sleep(3)
try:
    popup_exit = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div[4]/a')
    popup_exit.click()
    print("popup 종료")
except:
    pass

time.sleep(0.3)

def select_category(num): # 1차 카테고리 선택창 클릭 num은 1차 2차 3차
    select_first_category = driver.find_element(By.XPATH, '//*[@id="category-header"]/div[1]/div[2]/div/div['+str(num)+']/div[1]')
    select_first_category.click()
    time.sleep(1)

def select_seperated_category(parsed_item):
    second_cat = driver.find_element(By.XPATH, "//*[contains(text(),'" + parsed_item + "')]")
    second_cat.click()
    time.sleep(2)

def get_category_options():
    category_elements = driver.find_elements(By.XPATH, '//*[@id="category-header"]/div[3]/div/div')
    elems = []
    for elem in category_elements:
        elems.append(elem.text)
    text = elem.text

    # 주어진 텍스트를 줄바꿈 기준으로 분리하여 리스트로 변환
    parsed_list = text.split('\n')

    lenth = len(parsed_list)
    return parsed_list, lenth

first_list = []
first_lenght = 0

temp_list = []
temp_len = 0

second_lists = []


select_category(1)
first_list, first_lenght = get_category_options()
print(first_list)
print(first_lenght)
f_loop_index = 0
s_loop_index = 0
for item in first_list:
    select_seperated_category(item)
    select_category(2)
    print(item)
    temp_list, temp_len = get_category_options()
    second_lists.append(temp_list)
    select_category(1)

print(second_lists)


try:

    select_fourth_category = driver.find_element(By.XPATH,'//*[@id="category-header"]/div[1]/div[2]/div/div[4]/div[1]')
    select_fourth_category.click()
except exceptions.NoSuchElementException:
    print("항목이 없습니다.")







#
# #
#
#  # 2차 카테고리 시도
#
#
# # // *[ @ id = "category-header"] / div[4] / div / div
# # // *[ @ id = "category-header"] / div[4] / div / div
#
# # //*[@id="category-header"]/div[3]/div/div/div[1]
# # //*[@id="category-header"]/div[3]/div/div/div[2]
# # //*[@id="category-header"]/div[3]/div/div/div[12]
while True:
    time.sleep(2)
