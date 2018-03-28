from .basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from ..locator.loginLogLocator import LoginLogLocator as LLL
from selenium.webdriver.support import expected_conditions as EC



class LoginLogManagePage(BasePage):
    def is_right_page(self):
        assert self.driver.title == "麦子金服管理后台"
        self.getInQXXT()
        self.driver.find_element(*LLL.LOGIN_LOG_MANAGE_BUTTION).click()  # 点击
        self.driver.switch_to.frame("jumpIframe")
        try:
            WebDriverWait(self.driver,20).until(lambda x: "<title>日志管理</title>" in x.page_source)
            self.driver.switch_to.default_content()
            return True
        except Exception as e:
            print(e)
            return False

    def searchByName(self,name):
        self.switchToIfame()
        self.driver.find_element(*LLL.NAME_INPUT).clear()
        self.driver.find_element(*LLL.MAIL_INPUT).clear()
        self.driver.find_element(*LLL.NAME_INPUT).send_keys(name)
        try:
            WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(LLL.LOADING))
            WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(LLL.SEARCH_BUTTON)).click()
            WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(LLL.LOADING))
            data_eles = self.driver.find_elements(*LLL.DATA)
            if data_eles:
                for ele in data_eles:
                    assert name in ele.find_element(*LLL.DATA_TD_NAME).text
                return 1  #有查询结果
            else:
                return 2  # 没有查询结果
        except Exception as e:
            print(e)
            return 0   # 与预期结果不符，直接失败
        finally:
            self.switchToOuterFrame()

    def searchByMail(self,mail_name):
        self.switchToIfame()
        self.driver.find_element(*LLL.NAME_INPUT).clear()
        self.driver.find_element(*LLL.MAIL_INPUT).clear()
        self.driver.find_element(*LLL.MAIL_INPUT).send_keys(mail_name)
        try:
            WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(LLL.LOADING))
            WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(LLL.SEARCH_BUTTON)).click()
            WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(LLL.LOADING))
            data_eles = self.driver.find_elements(*LLL.DATA)
            print('查询的总数:',len(data_eles))
            if data_eles:
                for ele in data_eles:
                    assert mail_name in ele.find_element(*LLL.DATA_TD_MAIL).text
                return 1  #有查询结果
            else:
                return 2  # 没有查询结果
        except Exception as e:
            print(e)
            return 0   ## 与预期结果不符，直接失败
        finally:
            self.switchToOuterFrame()




