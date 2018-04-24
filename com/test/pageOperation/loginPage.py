
from ..locator.loginLocator import LoginLocator as LL
from .basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Login(BasePage):
    def __init__(self,driver):
        self.driver = driver

    def login(self,name='',passwd=''):
        self.waitElementPresent(LL.USERNAME).clear()
        self.waitElementPresent(LL.PASSWORD).clear()
        self.waitElementPresent(LL.USERNAME).send_keys(name)
        self.waitElementPresent(LL.PASSWORD).send_keys(passwd)
        self.waitElementClick(LL.SUBMIT)
        return self.waitElementPresent(LL.PERSON_LOGIN_SUCCESS)

    def loginOutside(self,name,passwd,alert='',snapshot_name=''):  ## 外部用户登录
        WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(LL.SHADE_CLASS))
        self.waitElementClick(LL.OUTER_LOGIN)
        self.waitElementPresent(LL.USERNAME).clear()
        self.waitElementPresent(LL.PASSWORD).clear()
        self.waitElementPresent(LL.USERNAME).send_keys(name)
        self.waitElementPresent(LL.PASSWORD).send_keys(passwd)
        self.waitElementClick(LL.SUBMIT)
        if alert:
            self.waitStringinPagesource(alert)
            self.saveScreenshot(snapshot_name+alert)
            return self.waitStringNotinPagesource(alert)
        else:
            return self.waitElementPresent(LL.PERSON_LOGIN_SUCCESS)

    def logout(self,snapshot_name=''):
        self.switchToOuterFrame()
        dl = self.waitElementPresent(LL.LOGOUT_DL)
        new_class = dl.get_attribute('class') + ' layui-show'
        self.driver.execute_script('arguments[0].className=arguments[1]',dl,new_class)
        self.findElement(LL.LOGOUT_BTN).click()
        self.waitStringinPagesource('确定要退出登录？')
        self.saveScreenshot(snapshot_name+'确定要退出登录')
        return self.waitElementClick(LL.LOGOUT_CONFIRM)
