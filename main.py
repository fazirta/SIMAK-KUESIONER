from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import random

driver = webdriver.Firefox()
driver.get("https://man4jkt.simakonline.com/login")
driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys("USERNAME")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("PASSWORD")
driver.find_element(By.XPATH, '/html/body/div/form/div[1]/button').click()
for i in range(1, 20):
    try:
        driver.get("https://man4jkt.simakonline.com/siswa/kuesioner")
        driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/section/div/ol/li[' + str(i) + ']/a').click()
        for j in range(1, 7):
            driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div/section/div/table[1]/tbody/tr[' + str(j) + ']/td[5]/input').click()
        for k in range(1, 18):
            driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div/section/div/table[2]/tbody/tr[' + str(k) + ']/td[5]/input').click()
        for l in range(1, 16):
            driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div/section/div/table[3]/tbody/tr[' + str(l) + ']/td[5]/input').click()
        for m in range(1, 8):
            driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div/section/div/table[4]/tbody/tr[' + str(m) + ']/td[5]/input').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div/section/div/textarea').send_keys(" ")
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div/div/div/section/div/input').click()
    except:
        pass
driver.close()