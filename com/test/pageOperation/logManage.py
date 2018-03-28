from .basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from ..locator.logLocator import LogLocator as LL
from selenium.webdriver.support import expected_conditions as EC



class LogManagePage(BasePage):
    def is_right_page(self):
        assert self.driver.title == "麦子金服管理后台"
        self.getInQXXT()
        self.driver.find_element(*LL.LOG_MANAGE_BUTTION).click()  # 点击
        WebDriverWait(self.driver, 20).until_not(EC.presence_of_element_located(LL.LOADING))
        self.driver.switch_to.frame("jumpIframe")
        try:
            WebDriverWait(self.driver,10).until(lambda x: "<title>日志管理</title>" in x.page_source)
            self.driver.switch_to.default_content()
            return True
        except Exception as e:
            print(e)
            return False

    def searchByName(self,name):
        self.switchToOuterFrame()
        self.switchToIfame()
        self.driver.find_element(*LL.NAME_INPUT).clear()
        self.driver.find_element(*LL.USERID_INPUT).clear()
        self.driver.find_element(*LL.NAME_INPUT).send_keys(name)
        try:
            WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(LL.SEARCH_BUTTON)).click()
            WebDriverWait(self.driver, 20).until_not(EC.presence_of_element_located(LL.LOADING))
            data_eles = self.driver.find_elements(*LL.DATA)
            # self.saveScreenshot('------')
            if data_eles:
                for ele in data_eles:
                    assert name in ele.find_element(*LL.DATA_TD_NAME).text
                return 1  #有查询结果
            else:
                return 2 #没有检索出结果
        except Exception as e:
            print(e)
            return 0

    def searchByUserid(self,userid):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until(lambda x:'<title>日志管理</title>' in x.page_source)
        self.driver.find_element(*LL.NAME_INPUT).clear()
        self.driver.find_element(*LL.USERID_INPUT).clear()
        self.driver.find_element(*LL.USERID_INPUT).send_keys(userid)
        try:
            WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(LL.SEARCH_BUTTON)).click()
            WebDriverWait(self.driver, 20).until_not(EC.presence_of_element_located(LL.LOADING))
            data_eles = self.driver.find_elements(*LL.DATA)
            # print("@@@@",len(data_eles),data_eles)
            if data_eles:
                for ele in data_eles:
                    assert userid in ele.find_element(*LL.DATA_TD_UDERID).text
                return 1  #有查询结果
            else:
                return 2 #没有检索出结果
        except Exception as e:
            print(e)
            return 0
