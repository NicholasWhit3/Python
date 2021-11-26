import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


urls = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

@pytest.mark.parametrize('url', urls)
def test_Openlink(browser, url):
    link = url
    browser.get(link)

    textarea = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[required]")))
    textarea.send_keys(str(math.log(int(time.time()))))

    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()

    banner = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
    result = banner.text

    assert "Correct!" == result, "Result is not as expected"
