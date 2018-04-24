from .basePage import BasePage
from ..locator.loginLogLocator import LoginLogLocator as LLL


class LoginLogManagePage(BasePage):
    def is_right_page(self):
        return super(LoginLogManagePage,self).is_right_page(LLL.LOGIN_LOG_MANAGE_BUTTION,'<title>日志管理</title>')

    def searchByName(self,name,snapshot_name):
        self.frameOutIn()
        self.findElement(LLL.NAME_INPUT).clear()
        self.findElement(LLL.MAIL_INPUT).clear()
        self.findElement(LLL.NAME_INPUT).send_keys(name)
        if self.waitElementClick(LLL.SEARCH_BUTTON):
            if self.waitLoading():
                data_eles = self.findElements(LLL.DATA)
                if data_eles:
                    for ele in data_eles:
                        assert name in self.findElementFromEle(ele,LLL.DATA_TD_NAME).text
                    self.saveScreenshot(snapshot_name + '1')
                    return 1  #有查询结果
                else:
                    self.saveScreenshot(snapshot_name + '2')
                    return 2  # 没有查询结果
        return 0 # 其他未知错误

    def searchByMail(self,mail_name,snapshot_name):
        self.frameOutIn()
        self.findElement(LLL.NAME_INPUT).clear()
        self.findElement(LLL.MAIL_INPUT).clear()
        self.findElement(LLL.MAIL_INPUT).send_keys(mail_name)
        if self.waitElementClick(LLL.SEARCH_BUTTON):
            if self.waitLoading():
                data_eles = self.findElements(LLL.DATA)
                if data_eles:
                    for ele in data_eles:
                        assert mail_name in self.findElementFromEle(ele,LLL.DATA_TD_MAIL).text
                    self.saveScreenshot(snapshot_name + '1')
                    return 1  # 有查询结果
                else:
                    self.saveScreenshot(snapshot_name + '2')
                    return 2  # 没有查询结果
        return 0 # 其他未知错误




