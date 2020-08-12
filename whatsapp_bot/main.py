from selenium import webdriver

chromedriver = 'D:\Programas\ChromeDriver\chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://web.whatsapp.com/')

name = input("Group name: ")
message = input("Message: ")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

message_box = driver.find_element_by_xpath("//div[@data-tab='1']")
message_box.send_keys(message)

button = driver.find_element_by_xpath("//button[@class='_1U1xa']")
button.click()






