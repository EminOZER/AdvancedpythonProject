from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
driver_path = "C:\\Users\\Berke\\Desktop\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://www.google.com/")
time.sleep(2)
browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("sahibinden")
time.sleep(2)
browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div[1]/a/h3/span").click()
time.sleep(2)

automobile=browser.find_element_by_xpath("//*[@id='container']/div[3]/div/aside/div[1]/nav/ul[3]/li[2]/ul/li[1]/a")
automobile.click()
BMW=browser.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/ul/div/div[1]/li[7]/a")
BMW.click()
M=browser.find_element_by_xpath("//*[@id='searchCategoryContainer']/div/div/ul/li[10]/a")
M.click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='searchResultLeft-price']/dl/dd/div/input[1]").send_keys("200000")
browser.find_element_by_xpath("//*[@id='searchResultLeft-price']/dl/dd/div/input[2]").send_keys("1000000")
browser.find_element_by_xpath("//*[@id='searchResultLeft-a5']/dl/dd/div/input[1]").send_keys("2000")
browser.find_element_by_xpath("//*[@id='searchResultLeft-a5']/dl/dd/div/input[2]").send_keys("2020")
time.sleep(2)
browser.find_element_by_xpath("//*[@id='_cllpsID_a4']").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='searchResultLeft-a4']/dl/dd/div/input[1]").send_keys("10000")
browser.find_element_by_xpath("//*[@id='searchResultLeft-a4']/dl/dd/div/input[2]").send_keys("600000")
time.sleep(1)
browser.find_element_by_xpath("//*[@id='searchResultsSearchForm']/div/div[3]/div[24]/button").click()
time.sleep(1)

html = browser.page_source
soup = BeautifulSoup(html,"lxml")


solmenu = soup.find_all("table",attrs={"id":"searchResultsTable"})
for sol in solmenu:
   a=sol.find_all("td",attrs={"class":"searchResultsTagAttributeValue"})
   b=sol.find_all("td",attrs={"class":"searchResultsAttributeValue"})
   c=sol.find_all("td",attrs={"class":"searchResultsPriceValue"})
   d = sol.find_all("td", attrs={"class": "searchResultsLocationValue"})
list =[]
list2=[]
list3=[]
list4=[]
for x in a:
    list.append(x.text)
for k in b:
    list2.append(k.text)
for z in c:
    list3.append(z.text)
for h in d:
    list4.append(h.text)
list5=[]
for index,y in enumerate(list):
    list5.append(list[index-1]+list2[3*index-3]+list2[3*index-2]+list2[3*index-1]+list3[index-1]+list4[index-1])
f = open("demofile.txt", "w")

for i in list5:
    liste = i.split("\n                    ")
    liste=i.replace('\n', '')
    f.write(liste+"\n")
