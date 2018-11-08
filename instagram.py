from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

wd = webdriver.Chrome(r'/Users/dima/git/grower/chromedriver')

wd.get('https://www.instagram.com/')

wd.add_cookie({'domain': '.instagram.com',
  'expiry': 1572183806.239896,
  'httpOnly': True,
  'name': 'sessionid',
  'path': '/',
  'secure': True,
  'value': '2320751870%3APART2qLpQRQvmO%3A5'})

wd.get('https://www.instagram.com/viktoriaa_88/')

# click on followers link
followers_button = wd.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
number_of_followers = followers_button.text.split(' ')[0]

followers_button.click()

sleep(5)

list_of_followers = []

for i in range(4):    #(int(number_of_followers)): # [0, 1, .. 197]
    follower = wd.find_element_by_xpath(f'/html/body/div[3]/div/div/div[2]/ul/div/li[{i+1}]')
    wd.execute_script('arguments[0].scrollIntoView()', follower)
    one_name_follower = follower.find_element_by_xpath('div[1]/div[2]/div[1]')
    print(one_name_follower.text)

    list_of_followers.append(one_name_follower.text)

    sleep(2)

print(list_of_followers)
print()