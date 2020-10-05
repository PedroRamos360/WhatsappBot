from selenium import webdriver
import time
import os

chromedriver = 'D:\Programas\ChromeDriver\chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://web.whatsapp.com/')

name = input("Group name: ")
message = input("Message: ")
when = input("Execution date (day:hour:minute:second): ")
shutdown = input("Shutdown after execution (y/n)? ")

day, hour, minute, second = when.split(":")

day = int(day)
hour = int(hour)
minute = int(minute)
second = int(second)

now = time.localtime()
now_in_seconds = now.tm_mday * 86400 + now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
date_in_seconds = day * 86400 + hour * 3600 + minute * 60 + second

sleep_time = date_in_seconds - now_in_seconds

time.sleep(sleep_time)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

message_box = driver.find_element_by_xpath("//div[@data-tab='1']")
message_box.send_keys(message)

button = driver.find_element_by_xpath("//button[@class='_1U1xa']")
button.click()

if shutdown.lower().strip() == 'y':
	os.system("shutdown -s -t 60")





