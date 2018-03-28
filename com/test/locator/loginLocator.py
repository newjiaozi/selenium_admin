from selenium.webdriver.common.by import By
from .mainLocator import MainPageLocator

class LoginLocator(MainPageLocator):
    OUTER_LOGIN = (By.XPATH,'/html/body/form/div[2]/ul/li[2]')  ## 切换到账号登录
    USERNAME = (By.XPATH,'//*[@id="username"]')
    PASSWORD = (By.XPATH,'//*[@id="password"]')
    IMAGECODE = (By.XPATH, '//*[@id="code"]')
    SUBMIT = (By.XPATH,'//*[@id="login"]')