import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

book = driver.find_element(By.ID, "book")
book.click()

sum_of_x = driver.find_element(By.ID, 'input_value')
x = sum_of_x.text
x = calc(x)

input_field = driver.find_element(By.XPATH, "//input[@class='form-control']")
input_field.send_keys(x)

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
