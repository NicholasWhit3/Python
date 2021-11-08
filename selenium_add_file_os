from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

current_dir = os.path.abspath(os.path.dirname("/home/mtimchenko/PycharmProjects/"))
filepath = os.path.join(current_dir, 'file.txt')


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

name = browser.find_element(By.XPATH, "//input[@name='firstname']")
name.send_keys("Name")

surname = browser.find_element(By.XPATH, "//input[@name='lastname']")
surname.send_keys("Surname")

email = browser.find_element(By.XPATH, "//input[@name='email']")
email.send_keys("email@mail.com")

choose_file_button = browser.find_element(By.XPATH, "//input[@type='file']")
choose_file_button.send_keys(filepath)

submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
