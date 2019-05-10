from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:/seleniumwebdriver/chromedriver.exe')  #execute selenium
driver.get("http://localhost:5000/") #localhost in port 5000 accessing
print(driver.find_element_by_tag_name('body').text)