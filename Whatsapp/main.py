from selenium import webdriver
import keyboard

chromedriver = 'D:\Programas\ChromeDriver\chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://web.whatsapp.com/')

name = input("Group name: ")
message = input("Message: ")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

message_box = driver.find_element_by_class_name('_3uMse')
message_box.send_keys(message)


