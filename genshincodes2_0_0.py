from bs4 import BeautifulSoup
import requests
from lxml import etree
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime

def main():
    codeget = requests.get('https://www.pockettactics.com/genshin-impact/codes')
    soupelement = BeautifulSoup(codeget.text, 'html.parser')
    etreeelement = etree.HTML(str(soupelement))

    xpaths = xpath_handler(5)
    codelist = make_code_list(xpaths, etreeelement)
    log_codes(codelist)

    if codelist == read_log(codelist):
        return print('No new codes today')
    else:
        inputCodes(codelist)


def read_log(inlist):
    length = len(inlist)
    with open('genshincodes2_0_0-log.txt', 'r') as infile:
        comparelist = (infile.readlines()[-length:])
        for i in range(length):
            x = comparelist[i].replace('\n', '')
            comparelist[i] = x
        return comparelist


#log date, and codes for that day.
def log_codes(inlist):
    with open('genshincodes2_0_0-log.txt', 'a') as outfile:
        curtime = datetime.now()
        outfile.write(f'{str(curtime)}\n')
        for i in inlist:
            outfile.write(f'{i}\n')


def make_code_list(pathlist, etree):
    codelist = []
    count = 1
    for path in pathlist:  
        xpathelement = etree.xpath(path)
        for i in xpathelement:
            codelist.append(i.text)
            print(f'Code{count}: {i.text}')
            count+=1
    return codelist

def xpath_handler(val):
    xpaths = []
    for path in range(val):
        xpaths.append(f'//*[@id="site_wrap"]/article/div/ul[1]/li[{path+1}]/strong')    
    return xpaths

def inputCodes(codelist):
    DRIVER_PATH = Service(r'C:\webdrivers\chromedriver.exe')
    for i in codelist:
        chrome_options = Options()
        dir = "H:\\chromedriveruserdata\\User Data"
        chrome_options.add_argument("user-data-dir="+dir)
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        with webdriver.Chrome(service=DRIVER_PATH, options=chrome_options) as driver:
            driver.get('https://genshin.mihoyo.com/en/gift')
            sleep(3)
            redeem_code = driver.find_element(By.ID, 'cdkey__code')
            sleep(1)
            redeem_code.send_keys(i)
            redeem_code.submit()
            sleep(1)
            print(f'Successfully submitted code: {i}')
    print('Complete!')



if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f'Program execution time: {end - start:.3f} seconds.')
    

