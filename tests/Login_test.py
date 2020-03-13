from selenium import webdriver
import pytest
import time
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils import utils as util
@pytest.mark.usefixtures("test_setup")
class TestLogin():


    def test_login(self):
        driver=self.driver
        driver.get(util.URL)
        time.sleep(30)
        login=LoginPage(driver)
        login.enter_username(util.Username)
        login.enter_password(util.Password)
        login.click_login()


        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()


    def test_logout(self):
        driver = self.driver
        time.sleep(20)
        homepage=HomePage(driver)
        homepage.click_welcome()
        time.sleep(30)
        homepage.click_Logout()


