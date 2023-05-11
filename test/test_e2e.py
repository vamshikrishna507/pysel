import time
from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjmodel.Homepage import HomePage
from utilities.BaseClass import baseclass


class TestOne(baseclass):
    def test_e2e(self):
        home_page = HomePage()
        home_page.shopitem().click()
        time.sleep(2)
        products = self.driver.find_elements(By.XPATH, "(//div[@class='card h-100'])")
        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_elelment(By.CSS_SELECTOR, "country").send_keys("Ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        stext = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in stext

        time.sleep(4)




