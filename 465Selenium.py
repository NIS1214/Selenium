#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:51:04 2022

@author: nis
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "users/nis/desktop/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element(By.NAME,"s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
        )
except:
    driver.quit()

print(main.text)



driver.quit()