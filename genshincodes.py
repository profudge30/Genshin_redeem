from selenium import webdriver
from time import sleep
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from sys import exit

DRIVER_PATH = r'C:\webdrivers\chromedriver.exe'

def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    with webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options) as driver:
        driver.get('https://www.pockettactics.com/genshin-impact/codes')
        driver.minimize_window()
        sleep(3)
        #datecheck = driver.find_element_by_xpath('/html/body/div[3]/article/div/p[1]').text
        #genshin_codes_header = driver.find_element_by_xpath('/html/body/div[5]/article/div/h2[1]').text
        current_codes = driver.find_element_by_xpath('//*[@id="site_wrap"]/article/div/ul[1]').text
        
        
        
        with open('genshincodeslog.txt', 'r') as infile:
            firstTenDays = 16
            restOfMonth = 17
            filedate = infile.readline(firstTenDays)
            filedate2 = infile.readline(restOfMonth)
            # if ((datecheck[:firstTenDays]) == filedate or (datecheck[:restOfMonth]) == filedate2):
            #     print('There are no new codes currently. Check again tomorrow.')
            #     exit(1)

        #with open('genshincodeslog.txt', 'w') as infile:
            #infile.writelines(datecheck[:firstTenDays])
        
        #print(f'CURRENT: {genshin_codes_header}')
        print('-----------------------------')
        formatCodes(current_codes)


list2 = []
def formatCodes(cur_codes):
    list1 = cur_codes.split('\n')
    for i in list1:
        counter=''
        for x in i:
            if (x == ' '):
                break
            else:
                counter+=x
        print(counter)
        with open('genshincodeslog.txt', 'a') as infile:
            infile.writelines("\n" + counter)
        list2.append(counter)
    
            
def inputCodes():

    for i in list2:
        chrome_options = Options()
        dir = "H:\\chromedriveruserdata\\User Data"
        chrome_options.add_argument("user-data-dir="+dir)
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        with webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options) as driver:
            driver.get('https://genshin.mihoyo.com/en/gift')
            driver.minimize_window()
            sleep(3)
            redeem_code = driver.find_element_by_id('cdkey__code')
            sleep(1)
            redeem_code.send_keys(i)
            redeem_code.submit()
            sleep(1)
            print(f'Successfully submitted code: {i}')
    print('Complete!')




main()
inputCodes()


