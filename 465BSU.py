#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:18:16 2022

@author: nis
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.select import Select


PATH = "users/nis/desktop/All/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.bowiestate.edu/")
print(driver.title)

directory = driver.find_element(By.LINK_TEXT, 'Directory').click()
time.sleep(3)

emails = driver.find_elements(By.CSS_SELECTOR, "a[href^='mailto:']")

for email in emails[:5]:
    print(email.text)


faculty = driver.find_element(By.LINK_TEXT, 'David Abrahams').click()

time.sleep(5)
driver.close()



