from selenium.webdriver.common.by import By


class HomePage:
    def __int__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopitem(self):
        return self.driver.find_element(*HomePage.shop)

