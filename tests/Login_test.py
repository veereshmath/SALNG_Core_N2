from selenium import webdriver
import pytest
import allure
import time
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from pages.logoutpage import LogoutPage
from utils import utils as util
@pytest.mark.usefixtures("test_setup")

class TestLogin():

    def test_login(self):
        try:
            self.driver.get(util.SALCORE_URL)
            Titile = self.driver.title
            assert Titile == 'Secure Access Concentrator Server'
        except AssertionError as error:
            print("Asserstion error occured")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise

    def test_logout(self):
        driver = self.driver
        self.driver.get(util.SALCORE_URL)
        time.sleep(10)
        logoutpage1=LogoutPage(driver)
        logoutpage1.click_logout()
        # homepage=HomePage(driver)
        # homepage.click_welcome()
        # time.sleep(30)
        # homepage.click_Logout()
