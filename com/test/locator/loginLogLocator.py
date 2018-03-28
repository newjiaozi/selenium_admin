from selenium.webdriver.common.by import By
from .mainLocator import MainPageLocator

class LoginLogLocator(MainPageLocator):

    IFRAME = (By.ID,'jumpIframe')   #主页面的iframe
    NAME_INPUT = (By.ID,'search1')  # 检索框，姓名
    MAIL_INPUT = (By.ID,'search2') #检索框，userid
    SEARCH_BUTTON = (By.XPATH,'/html/body/div[1]/div[1]/div/div[3]/button')  #查询
    DATA = (By.XPATH,'//*[@id="tableUser"]/tbody/tr')  #数据所在行
    DATA_NAME = (By.XPATH,'//*[@id="tableUser"]/tbody/tr[%d]/td[4]')  #数据所在行的，登录名
    DATA_MAIL = (By.XPATH,'//*[@id="tableUser"]/tbody/tr[%d]/td[5]')  #数据所在行的，邮箱
    DATA_TD_NAME = (By.XPATH,'//td[4]')
    DATA_TD_MAIL = (By.XPATH,'//td[5]')

    # LOADING = (By.XPATH,'//*[@id="layui-layer1"]/div')
    PAGE_USER = (By.ID,'pagerUser')  ##翻页
