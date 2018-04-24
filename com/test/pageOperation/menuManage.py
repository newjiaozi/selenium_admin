from .basePage import BasePage
from ..locator.menuLocator import MenuLocator as ML

class MenuManagePage(BasePage):

    def is_right_page(self):
        return super(MenuManagePage,self).is_right_page(ML.MENU_MANAGE_BUTTION,"<title>菜单管理</title>")

    def addSystem(self,name='',remark='',apartment='',snapshot_name='',alert=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        self.waitAllElementPresent(ML.MENU_DATA_TR)
        self.waitElementClick(ML.MENU_DATA_FIRST_LINE_ADD)
        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>添加菜单 </title>')
        self.findElement(ML.ADD_SYSTEM_NAME).clear()
        self.findElement(ML.ADD_SYSTEM_REMARK).clear()
        self.findElement(ML.ADD_SYSTEM_NAME).send_keys(name)
        self.findElement(ML.ADD_SYSTEM_REMARK).send_keys(remark)
        if apartment:
            dds = self.waitAllElementPresent(ML.ADD_SYSTEM_APART_DD)
            self.waitElementClick(ML.ADD_SYSTEM_APART)
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break
        if alert:
            self.switchToParentFrame()
            self.waitElementClick(ML.ADD_CONFIRM)
            self.switchToInnerFrame()
            self.waitStringinPagesource(alert)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            return self.waitElementClick(ML.ADD_CANCEL)

        else:
            self.switchToParentFrame()
            self.waitElementClick(ML.ADD_CONFIRM)
            self.switchToOuterFrame()
            self.waitStringinPagesource('数据添加成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('数据添加成功')

    def addMenu(self,system_name='',name='',remark='',apartment='',snapshot_name='',alert=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs =self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                self.findElementFromEle(tr,ML.TR_TD_BTN).click()
                break

        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>添加菜单 </title>')
        self.findElement(ML.ADD_SYSTEM_NAME).clear()
        self.findElement(ML.ADD_SYSTEM_REMARK).clear()
        self.findElement(ML.ADD_SYSTEM_NAME).send_keys(name)
        self.findElement(ML.ADD_SYSTEM_REMARK).send_keys(remark)

        if apartment:
            dds = self.waitAllElementPresent(ML.ADD_MENU_APART_DD)
            self.waitElementClick(ML.ADD_MENU_APART)
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break
        self.switchToParentFrame()
        self.waitElementClick(ML.ADD_CONFIRM)
        if alert:
            self.switchToInnerFrame()
            self.waitStringinPagesource(alert)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            return self.waitElementClick(ML.ADD_CANCEL)

        else:
            self.switchToOuterFrame()
            self.waitStringinPagesource('数据添加成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('数据添加成功')

    def addPage(self,system_name='',menu_name='',name='',target='',remark='',apartment='',snapshot_name='',alert=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == menu_name:
                self.findElementFromEle(tr,ML.TR_TD_BTN).click()
                break
        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>添加菜单 </title>')
        self.findElement(ML.ADD_PAGE_NAME).clear()
        self.findElement(ML.ADD_PAGE_NAME).send_keys(name)
        self.findElement(ML.ADD_PAGE_TARGET).clear()
        self.findElement(ML.ADD_PAGE_TARGET).send_keys(target)
        self.findElement(ML.ADD_PAGE_REMARK).clear()
        self.findElement(ML.ADD_PAGE_REMARK).send_keys(remark)

        if apartment:
            dds = self.waitAllElementPresent(ML.ADD_PAGE_APART_DD)
            self.waitElementClick(ML.ADD_PAGE_APART)
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break
        self.switchToParentFrame()
        self.waitElementClick(ML.ADD_CONFIRM)
        if alert:
            self.switchToInnerFrame()
            self.waitStringinPagesource(alert)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            return self.waitElementClick(ML.ADD_CANCEL)
        else:
            self.switchToOuterFrame()
            self.waitStringinPagesource('数据添加成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('数据添加成功')

    def addInterface(self,system_name='',menu_name='',page_name='',name='',target='',remark='',apartment='',snapshot_name='',alert=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == menu_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == page_name:
                self.findElementFromEle(tr,ML.TR_TD_BTN).click()
                break

        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>添加菜单 </title>')
        self.findElement(ML.ADD_INTERFACE_NAME).clear()
        self.findElement(ML.ADD_INTERFACE_NAME).send_keys(name)
        self.findElement(ML.ADD_INTERFACE_TARGET).clear()
        self.findElement(ML.ADD_INTERFACE_TARGET).send_keys(target)
        self.findElement(ML.ADD_INTERFACE_REMARK).clear()
        self.findElement(ML.ADD_INTERFACE_REMARK).send_keys(remark)

        if apartment:
            dds = self.waitAllElementPresent(ML.ADD_INTERFACE_APART_DD)
            self.waitElementClick(ML.ADD_INTERFACE_APART)
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break
        self.switchToParentFrame()
        self.waitElementClick(ML.ADD_CONFIRM)
        if alert:
            self.switchToInnerFrame()
            self.waitStringinPagesource(alert)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            return self.waitElementClick(ML.ADD_CANCEL)
        else:
            self.switchToOuterFrame()
            self.waitStringinPagesource('数据添加成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('数据添加成功')

    def modifySystem(self,system_name='',name='',remark='',apartment='',snapshot_name='',alert=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                self.findElementsFromEle(tr,ML.TR_TD_BTN)[1].click()
                break

        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>编辑菜单 </title>')
        self.findElement(ML.ADD_SYSTEM_NAME).clear()
        self.findElement(ML.ADD_SYSTEM_NAME).send_keys(name)
        self.findElement(ML.ADD_SYSTEM_REMARK).clear()
        self.findElement(ML.ADD_SYSTEM_REMARK).send_keys(remark)

        if apartment:
            aparts = self.findElements(ML.DELETE_APART)
            re_aparts = reversed(aparts)
            for apart in re_aparts:
                apart.click()
            self.findElement(ML.ADD_APART).click()
            dds = self.waitAllElementPresent(ML.ADD_SYSTEM_APART_DD)
            self.waitElementClick(ML.ADD_SYSTEM_APART)
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break
        else:

            aparts = self.findElements(ML.DELETE_APART)
            re_aparts = reversed(aparts)
            for apart in re_aparts:
                apart.click()

        self.switchToParentFrame()
        self.waitElementClick(ML.ADD_CONFIRM)
        if alert:
            self.switchToInnerFrame()
            self.waitStringinPagesource(alert)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            return self.waitElementClick(ML.ADD_CANCEL)
        else:
            self.switchToOuterFrame()
            self.waitStringinPagesource('修改成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('修改成功')

    def modifyMenu(self,system_name='',menu_name='',name='',remark='',apartment='',snapshot_name='',alert=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == menu_name:
                self.findElementsFromEle(tr,ML.TR_TD_BTN)[1].click()
                break
        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>编辑菜单 </title>')

        self.findElement(ML.ADD_MENU_NAME).clear()
        self.findElement(ML.ADD_MENU_NAME).send_keys(name)
        self.findElement(ML.ADD_MENU_REMARK).clear()
        self.findElement(ML.ADD_MENU_REMARK).send_keys(remark)

        if apartment:
            aparts = self.findElements(ML.DELETE_APART)
            re_aparts = reversed(aparts)
            for apart in re_aparts:
                apart.click()
            self.waitElementClick(ML.ADD_APART)
            self.switchToInnerFrame()
            dds = self.waitAllElementPresent(ML.ADD_MENU_APART_DD)
            self.waitElementClick(ML.ADD_MENU_APART)
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break

        else:
            aparts = self.findElements(ML.DELETE_APART)
            re_aparts = reversed(aparts)
            for apart in re_aparts:
                apart.click()

        self.switchToParentFrame()
        self.waitElementClick(ML.ADD_CONFIRM)
        if alert:
            self.switchToInnerFrame()
            self.waitStringinPagesource(alert)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            return self.waitElementClick(ML.ADD_CANCEL)
        else:
            self.switchToOuterFrame()
            self.waitStringinPagesource('修改成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('修改成功')

    def modifyPage(self,system_name='',menu_name='',page_name='',name='',target='',remark='',apartment='',snapshot_name='',alert=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == menu_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == page_name:
                self.findElementsFromEle(tr,ML.TR_TD_BTN)[1].click()
                break

        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>编辑菜单 </title>')

        self.findElement(ML.ADD_PAGE_NAME).clear()
        self.findElement(ML.ADD_PAGE_NAME).send_keys(name)
        self.findElement(ML.ADD_PAGE_TARGET).clear()
        self.findElement(ML.ADD_PAGE_TARGET).send_keys(target)
        self.findElement(ML.ADD_PAGE_REMARK).clear()
        self.findElement(ML.ADD_PAGE_REMARK).send_keys(remark)

        if apartment:
            aparts = self.findElements(ML.DELETE_APART)
            re_aparts = reversed(aparts)
            for apart in re_aparts:
                apart.click()
            self.waitElementClick(ML.ADD_APART)
            dds = self.waitAllElementPresent(ML.ADD_PAGE_APART_DD)
            self.waitElementClick(ML.ADD_PAGE_APART)
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break

        else:
            aparts = self.findElements(ML.DELETE_APART)
            re_aparts = reversed(aparts)
            for apart in re_aparts:
                apart.click()

        self.switchToParentFrame()
        self.waitElementClick(ML.ADD_CONFIRM)

        if alert:
            self.switchToInnerFrame()
            self.waitStringinPagesource(alert)
            self.saveScreenshot(snapshot_name + alert)
            self.switchToParentFrame()
            return self.waitElementClick(ML.ADD_CANCEL)
        else:
            self.switchToOuterFrame()
            self.waitStringinPagesource('修改成功')
            self.saveScreenshot(snapshot_name)
            self.waitStringNotinPagesource('修改成功')

    def modifyInterface(self,system_name='',menu_name='',page_name='',interface_name='',name='',target='',remark='',apartment='',snapshot_name='',alert=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == menu_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == page_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            tr1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == interface_name:
                self.findElementsFromEle(tr,ML.TR_TD_BTN)[1].click()
                break

        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>编辑菜单 </title>')

        self.findElement(ML.ADD_PAGE_NAME).clear()
        self.findElement(ML.ADD_PAGE_NAME).send_keys(name)
        self.findElement(ML.ADD_PAGE_TARGET).clear()
        self.findElement(ML.ADD_PAGE_TARGET).send_keys(target)
        self.findElement(ML.ADD_PAGE_REMARK).clear()
        self.findElement(ML.ADD_PAGE_REMARK).send_keys(remark)

        if apartment:
            aparts = self.findElements(ML.DELETE_APART)
            re_aparts = reversed(aparts)
            for apart in re_aparts:
                apart.click()
            self.waitElementClick(ML.ADD_APART)
            dds = self.waitAllElementPresent(ML.ADD_INTERFACE_APART_DD)
            self.waitElementClick(ML.ADD_INTERFACE_APART)
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break

        else:
            aparts = self.findElements(ML.DELETE_APART)
            re_aparts = reversed(aparts)
            for apart in re_aparts:
                apart.click()

        self.switchToParentFrame()
        self.waitElementClick(ML.ADD_CONFIRM)
        if alert:
            self.switchToInnerFrame()
            self.waitStringinPagesource(alert)
            self.saveScreenshot(snapshot_name + alert)
            self.switchToParentFrame()
            return self.waitElementClick(ML.ADD_CANCEL)
        else:
            self.switchToOuterFrame()
            self.waitStringinPagesource('修改成功')
            self.saveScreenshot(snapshot_name)
            self.waitStringNotinPagesource('修改成功')

    def deleteInterface(self,system_name='',menu_name='',page_name='',interface_name='',snapshot_name=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == menu_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == page_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == interface_name:
                self.findElementsFromEle(tr,ML.TR_TD_BTN)[2].click()
                break

        if self.waitStringinPagesource('确定要删除吗？'):
            self.waitElementClick(ML.DELETE_CONFIRM)
            self.switchToOuterFrame()

            self.waitStringinPagesource('删除成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('删除成功')

    def deletePage(self,system_name='',menu_name='',page_name='',snapshot_name=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)

        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == menu_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == page_name:
                self.findElementsFromEle(tr,ML.TR_TD_BTN)[2].click()
                break

        if self.waitStringinPagesource('确定要删除吗？'):
            self.waitElementClick(ML.DELETE_CONFIRM)
            self.switchToOuterFrame()

            self.waitStringinPagesource('删除成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('删除成功')


    def deleteMenu(self,system_name='',menu_name='',snapshot_name=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                tr.click()
                break

        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == menu_name:
                self.findElementsFromEle(tr,ML.TR_TD_BTN)[2].click()
                break

        if self.waitStringinPagesource('确定要删除吗？'):
            self.waitElementClick(ML.DELETE_CONFIRM)
            self.switchToOuterFrame()

            self.waitStringinPagesource('删除成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('删除成功')

    def deleteSystem(self,system_name='',snapshot_name=''):
        self.frameOutIn()
        self.waitStringinPagesource("<title>菜单管理</title>")
        trs = self.waitAllElementPresent(ML.MENU_DATA_TR)
        for tr in reversed(trs):
            td1 = self.findElementFromEle(tr,ML.TR_TD)
            if td1.text == system_name:
                self.findElementsFromEle(tr,ML.TR_TD_BTN)[2].click()
                break

        if self.waitStringinPagesource('确定要删除吗？'):
            self.waitElementClick(ML.DELETE_CONFIRM)
            self.switchToOuterFrame()
            self.waitStringinPagesource('删除成功')
            self.saveScreenshot(snapshot_name)
            return self.waitStringNotinPagesource('删除成功')


    def refreshToMenuManage(self):
        self.refreshPage()
        self.waitElementClick(ML.MENU_MANAGE_BUTTION)
        self.waitLoading()

