from selenium.webdriver.common.by import By
from .mainLocator import MainPageLocator

class LogLocator(MainPageLocator):

    IFRAME = (By.ID,'jumpIframe')   #主页面的iframe
    NAME_INPUT = (By.ID,'search1')  # 检索框，姓名
    USERID_INPUT = (By.ID,'search2') #检索框，userid
    SEARCH_BUTTON = (By.XPATH,'/html/body/div[1]/div[1]/div/div[3]/button')  #查询
    DATA = (By.XPATH,'//*[@id="tableUser"]/tbody/tr')  #数据所在行
    DATA_NAME = (By.XPATH,'//*[@id="tableUser"]/tbody/tr[%d]/td[2]')  #数据所在行的，姓名
    DATA_USERID = (By.XPATH,'//*[@id="tableUser"]/tbody/tr[%d]/td[3]')  #数据所在行的，userid
    DATA_TD_NAME = (By.XPATH,'//td[2]')
    DATA_TD_UDERID = (By.XPATH,'//td[4]')
    PAGE_USER = (By.ID,'pagerUser')  ##翻页
