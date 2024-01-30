from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
time.sleep(2)

username = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
username.send_keys("Admin")
time.sleep(2)

password = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
password.send_keys("admin123")
time.sleep(2)
login=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

login.click()
time.sleep(2)

pim=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
pim.click()
time.sleep(2)

addemployee=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
addemployee.click()
time.sleep(2)

firstname=driver.find_element(By.XPATH,'div[1]/div/div/div[2]/div[1]/div[2]/input')

firstname.send_keys("anbu")
time.sleep(2)

lastname=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
lastname.send_keys("s")
time.sleep(2)

save=driver.find_element(By.XPATH,'')
save.click()
time.sleep(2)