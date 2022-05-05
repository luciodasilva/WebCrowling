from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://google.com.br")

print(driver.current_url)
print(driver.title)
print(driver.capabilities['browserVersion'])

element = driver.find_element_by_name("q")
element.click()
element.send_keys("pyJamas Conf")
element.submit()

sleep(4)

driver.close()
