import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRequiredInputs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def get_registration_result(self, link):
        self.driver.get(link)

        # fill the required fields
        list_of_required_fields = self.driver.find_elements(By.TAG_NAME, 'input')
        for elem in list_of_required_fields:
            if elem.get_attribute('required'):
                elem.send_keys("some text")
                
        # submit the form
        button = self.driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # wait for the page to render new element
        welcome_text_elt = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        welcome_text = welcome_text_elt.text
        return welcome_text


    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        result = self.get_registration_result(link)
        self.assertEqual("Congratulations! You have successfully registered!", result, "Registration failed")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        result = self.get_registration_result(link)
        self.assertEqual("Congratulations! You have successfully registered!", result, "Registration failed")


if __name__ == "__main__":
    unittest.main()
