from .basePage import BasePage
from ..locator.logLocator import LogLocator as LL



class LogManagePage(BasePage):
    def is_right_page(self):
        return super(LogManagePage,self).is_right_page(LL.LOG_MANAGE_BUTTION,"<title>日志管理</title>")

    def searchByName(self,name,snapshot_name):
        self.frameOutIn()
        self.findElement(LL.NAME_INPUT).clear()
        self.findElement(LL.USERID_INPUT).clear()
        self.findElement(LL.NAME_INPUT).send_keys(name)
        if self.waitElementClick(LL.SEARCH_BUTTON):
            if self.waitLoading():
                data_eles = self.findElements(LL.DATA)
                if data_eles:
                    for ele in data_eles:
                        assert name in self.findElementFromEle(ele,LL.DATA_TD_NAME).text
                    self.saveScreenshot(snapshot_name+'1')
                    return 1  #有查询结果
                else:
                    self.saveScreenshot(snapshot_name+'2')
                    return 2 #没有检索出结果
        return 0 # 其他情况

    def searchByUserid(self,userid,snapshot_name):
        self.frameOutIn()
        self.findElement(LL.NAME_INPUT).clear()
        self.findElement(LL.USERID_INPUT).clear()
        self.findElement(LL.USERID_INPUT).send_keys(userid)
        if self.waitElementClick(LL.SEARCH_BUTTON):
            if self.waitLoading():
                data_eles = self.findElements(LL.DATA)
                if data_eles:
                    for ele in data_eles:
                        assert userid in self.findElementFromEle(ele,LL.DATA_TD_UDERID).text
                    self.saveScreenshot(snapshot_name+'1')
                    return 1  #有查询结果
                else:
                    self.saveScreenshot(snapshot_name+'2')
                    return 2 #没有检索出结果
        return 0 # 其他情况