from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/form")

driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("John")
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("Smith")
driver.find_element(By.XPATH, '//*[@id="job-title"]').send_keys("QA")
driver.find_element(By.XPATH, '//*[@id="radio-button-2"]').click()
driver.find_element(By.XPATH, '//*[@id="checkbox-2"]').click()
driver.find_element(By.XPATH, '//*[@id="select-menu"]').click()
driver.find_element(By.XPATH, '//*[@id="select-menu"]/option[2]').click()
driver.find_element(By.XPATH, '//*[@id="datepicker"]').send_keys("01/01/2020")

submit_button = driver.find_element(By.XPATH, "/html/body/div/form/div/div[8]/a")
submit_button.click()

sleep(5)
driver.quit()