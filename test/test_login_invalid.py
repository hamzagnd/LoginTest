import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_login_invalid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_invalid_login(self):
        driver = self.driver
        # Login sayfasına git
        driver.get("https://the-internet.herokuapp.com/login")

        # Yanlış kullanıcı adı ve şifre gir
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.send_keys("wronguser")
        password.send_keys("wrongpass")

        # Submit butonuna tıkla
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # mesajını doğrula
        error = driver.find_element(By.ID, "flash")
        self.assertIn("invalid", error.text.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
