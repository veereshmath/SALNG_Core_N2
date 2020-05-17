from selenium.webdriver import ActionChains

class LogoutPage():

    def __init__(self, driver):
        self.driver=driver

        self.username_textbox_id ="txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.menu_icon_xpath ="//span[@class='icon-contact']"
        self.logout_link_id ="headerForm:logOutLink"
        self.logout_text_xpath ="//p[contains(text(),'You have successfully logged out from the applicat')]"

    def click_logout(self):
        self.action = ActionChains(self.driver)
        icon = self.driver.find_element_by_xpath(self.menu_icon_xpath)
        self.action.move_to_element(icon).perform()
        self.driver.find_element_by_id(self.logout_link_id).click()


    # def enter_password(self, password):
    #     self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    #
    # def click_login(self):
    #     self.driver.find_element_by_id(self.login_button_id).click()





