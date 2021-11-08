import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome()
url = "http://suninjuly.github.io/redirect_accept.html"
driver.get(url)

flying_button = driver.find_element(By.XPATH, "//button[@type='submit']")
flying_button.click()

switch_to_window = driver.window_handles[1]  
driver.switch_to.window(switch_to_window)

sum_of_x = driver.find_element(By.ID, 'input_value')
x = sum_of_x.text
x = calc(x)

input_field = driver.find_element(By.XPATH, "//input[@class='form-control']")
input_field.send_keys(x)

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
