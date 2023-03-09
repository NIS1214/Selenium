#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:37:58 2022

@author: nis
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:27:40 2022

@author: nis
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "users/nis/desktop/All/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://facebook.com/signup")
print(driver.title)

search = driver.find_element(By.NAME,"firstname")
search.send_keys("sanis")
search2 = driver.find_element(By.NAME,"lastname")
search2.send_keys("mahato")
search3 = driver.find_element(By.NAME,"reg_email__")
search3.send_keys("sanismahato@gmail.com")
search4 = driver.find_element(By.NAME,"reg_email_confirmation__")
search4.send_keys("sanismahato@gmail.com")
search5 = driver.find_element(By.NAME,"reg_passwd__")
search5.send_keys("sanis2000dec14")
search6 = driver.find_element(By.NAME,"birthday_month")
search6.send_keys("Dec")
search7 = driver.find_element(By.NAME,"birthday_day")
search7.send_keys("14")
search8 = driver.find_element(By.NAME,"birthday_year")
search8.send_keys("2000")
search9 = driver.find_element(By.CLASS_NAME, "_8esa").click()
search10 = driver.find_element(By.NAME,"websubmit").click()

search.send_keys(Keys.RETURN)

