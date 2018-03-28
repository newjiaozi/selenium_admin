
from ..locator.loginLocator import LoginLocator as LL

from .basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait

class Login(BasePage):
    def __init__(self,driver):
        self.driver = driver

    def login(self,name='',passwd=''):
        self.driver.find_element(*LL.USERNAME).send_keys(name)
        self.driver.find_element(*LL.PASSWORD).send_keys(passwd)
        self.driver.find_element(*LL.SUBMIT).click()

    def login2(self,name,passwd,snapshot_name=''):
        self.driver.find_element(*LL.OUTER_LOGIN).click()
        self.driver.find_element(*LL.USERNAME).clear()
        self.driver.find_element(*LL.PASSWORD).clear()
        self.driver.find_element(*LL.USERNAME).send_keys(name)
        self.driver.find_element(*LL.PASSWORD).send_keys(passwd)

        self.driver.find_element(*LL.SUBMIT).click()
        WebDriverWait(self.driver,20).until(lambda x : '登录失败次数过多，请联系管理员' in x.page_source)
        self.saveScreenshot(snapshot_name)