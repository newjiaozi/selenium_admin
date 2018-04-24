from selenium.webdriver.common.by import By
from .mainLocator import MainPageLocator

class LoginLocator(MainPageLocator):
    OUTER_LOGIN = (By.XPATH,'/html/body/form/div[2]/ul/li[2]')  ## 切换到账号登录
    USERNAME = (By.XPATH,'//*[@id="username"]')
    PASSWORD = (By.XPATH,'//*[@id="password"]')
    IMAGECODE = (By.XPATH, '//*[@id="code"]')
    SUBMIT = (By.XPATH,'//*[@id="login"]')
    CAPTCHAID = (By.ID,'captchaId')
    CODE = (By.ID,'globalCode')
    SLIDE = (By.ID,'isSlide')

    LOGOUT_DL = (By.XPATH,'/html/body/div[1]/div[1]/div[3]/div/dl')
    LOGOUT_BTN = (By.LINK_TEXT,'退出登录')
    LOGOUT_CONFIRM = (By.CLASS_NAME,'layui-layer-btn0')