from .basePage import BasePage
from ..locator.menuLocator import MenuLocator as ML
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuManagePage(BasePage):
    def is_right_page(self):
        assert "麦子金服管理后台" == self.driver.title
        self.getInQXXT()

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(ML.MENU_MANAGE_BUTTION)).click()
        self.switchToIfame()
        try :
            WebDriverWait(self.driver, 20).until_not(EC.visibility_of_element_located(ML.LOADING))
            WebDriverWait(self.driver,20).until(lambda x: "<title>菜单管理</title>" in x.page_source)
            self.switchToOuterFrame()
            return True
        except Exception as e:
            ##print(e)
            return False


    def refresh(self):
        # self.switchToOuterFrame()
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(ML.ROLE_MANAGE_BUTTON)).click() # 点击用户管理
        # WebDriverWait(self.driver,10).until_not(EC.visibility_of_element_located(ML.LOADING))
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(ML.MENU_MANAGE_BUTTION)).click() # 点击用户管理
        # self.switchToIfame()
        # WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        self.driver.refresh()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(ML.MENU_MANAGE_BUTTION)).click() # 点击菜单管理


    def addSystem(self,name='',remark='',apartment='',snapshot_name='',alert=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(ML.MENU_DATA_FIRST_LINE_ADD)).click()
        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x:'<title>添加菜单 </title>' in x.page_source)
        self.driver.find_element(*ML.ADD_SYSTEM_NAME).clear()
        self.driver.find_element(*ML.ADD_SYSTEM_NAME).send_keys(name)
        self.driver.find_element(*ML.ADD_SYSTEM_REMARK).clear()
        self.driver.find_element(*ML.ADD_SYSTEM_REMARK).send_keys(remark)

        if apartment:
            dds = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(ML.ADD_SYSTEM_APART_DD))
            self.driver.find_element(*ML.ADD_SYSTEM_APART).click()
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break
        if alert:
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CONFIRM).click()
            self.switchToInnerFrame()
            WebDriverWait(self.driver,20).until(lambda x : alert in x.page_source)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CANCEL).click()
            return True


        else:
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CONFIRM).click()
            self.switchToOuterFrame()

            WebDriverWait(self.driver,20).until(lambda x:'数据添加成功' in x.page_source)
            self.saveScreenshot(snapshot_name)
            WebDriverWait(self.driver, 20).until(lambda x: '数据添加成功' not in x.page_source)
            return True

    def addMenu(self,system_name='',name='',remark='',apartment='',snapshot_name='',alert=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            tds = tr.find_elements(*ML.TR_TD)
            ##print(td1.text,'####',len(tds))
            if td1.text == system_name:
                tr.find_element(*ML.TR_TD_BTN).click()
                break

        self.switchToInnerFrame()

        WebDriverWait(self.driver,20).until(lambda x:'<title>添加菜单 </title>' in x.page_source)
        self.driver.find_element(*ML.ADD_MENU_NAME).clear()
        self.driver.find_element(*ML.ADD_MENU_NAME).send_keys(name)
        self.driver.find_element(*ML.ADD_MENU_REMARK).clear()
        self.driver.find_element(*ML.ADD_MENU_REMARK).send_keys(remark)

        if apartment:
            dds = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(ML.ADD_MENU_APART_DD))
            self.driver.find_element(*ML.ADD_MENU_APART).click()
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break
        self.switchToParentFrame()
        self.driver.find_element(*ML.ADD_CONFIRM).click()
        if alert:
            self.switchToInnerFrame()
            WebDriverWait(self.driver,20).until(lambda x : alert in x.page_source)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CANCEL).click()

        else:
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x:'数据添加成功' in x.page_source)
            self.saveScreenshot(snapshot_name)
            WebDriverWait(self.driver, 20).until(lambda x: '数据添加成功' not in x.page_source)

    def addPage(self,system_name='',menu_name='',name='',target='',remark='',apartment='',snapshot_name='',alert=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == system_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == menu_name:
                tr.find_element(*ML.TR_TD_BTN).click()
                break
        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x:'<title>添加菜单 </title>' in x.page_source)
        self.driver.find_element(*ML.ADD_PAGE_NAME).clear()
        self.driver.find_element(*ML.ADD_PAGE_NAME).send_keys(name)
        self.driver.find_element(*ML.ADD_PAGE_TARGET).clear()
        self.driver.find_element(*ML.ADD_PAGE_TARGET).send_keys(target)
        self.driver.find_element(*ML.ADD_PAGE_REMARK).clear()
        self.driver.find_element(*ML.ADD_PAGE_REMARK).send_keys(remark)

        if apartment:
            dds = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(ML.ADD_PAGE_APART_DD))
            self.driver.find_element(*ML.ADD_PAGE_APART).click()
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break
        self.switchToParentFrame()
        self.driver.find_element(*ML.ADD_CONFIRM).click()
        if alert:
            self.switchToInnerFrame()
            WebDriverWait(self.driver,20).until(lambda x : alert in x.page_source)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CANCEL).click()
        else:
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x:'数据添加成功' in x.page_source)
            self.saveScreenshot(snapshot_name)
            WebDriverWait(self.driver, 20).until(lambda x: '数据添加成功' not in x.page_source)

    def addInterface(self,system_name='',menu_name='',page_name='',name='',target='',remark='',apartment='',snapshot_name='',alert=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == system_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == menu_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == page_name:
                tr.find_element(*ML.TR_TD_BTN).click()
                break

        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x:'<title>添加菜单 </title>' in x.page_source)
        self.driver.find_element(*ML.ADD_INTERFACE_NAME).clear()
        self.driver.find_element(*ML.ADD_INTERFACE_NAME).send_keys(name)
        self.driver.find_element(*ML.ADD_INTERFACE_TARGET).clear()
        self.driver.find_element(*ML.ADD_INTERFACE_TARGET).send_keys(target)
        self.driver.find_element(*ML.ADD_INTERFACE_REMARK).clear()
        self.driver.find_element(*ML.ADD_INTERFACE_REMARK).send_keys(remark)

        if apartment:
            dds = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(ML.ADD_INTERFACE_APART_DD))
            self.driver.find_element(*ML.ADD_INTERFACE_APART).click()
            for dd in dds:
                if dd.text == apartment:
                    dd.click()
                    break
        self.switchToParentFrame()
        self.driver.find_element(*ML.ADD_CONFIRM).click()
        if alert:
            self.switchToInnerFrame()
            WebDriverWait(self.driver,20).until(lambda x : alert in x.page_source)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CANCEL).click()
        else:
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x:'数据添加成功' in x.page_source)
            self.saveScreenshot(snapshot_name)
            WebDriverWait(self.driver, 20).until(lambda x: '数据添加成功' not in x.page_source)

    def modifySystem(self,system_name='',name='',remark='',apartment='',snapshot_name='',alert=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == system_name:
                tr.find_elements(*ML.TR_TD_BTN)[1].click()
                break

        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x:'<title>编辑菜单 </title>' in x.page_source)
        self.driver.find_element(*ML.ADD_SYSTEM_NAME).clear()
        self.driver.find_element(*ML.ADD_SYSTEM_NAME).send_keys(name)
        self.driver.find_element(*ML.ADD_SYSTEM_REMARK).clear()
        self.driver.find_element(*ML.ADD_SYSTEM_REMARK).send_keys(remark)

        if apartment:
            try:
                aparts = self.driver.find_elements(*ML.DELETE_APART)
                re_aparts = reversed(aparts)
                for apart in re_aparts:
                    apart.click()
                self.driver.find_element(*ML.ADD_APART).click()
                dds = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.ADD_SYSTEM_APART_DD))
                self.driver.find_element(*ML.ADD_SYSTEM_APART).click()
                for dd in dds:
                    if dd.text == apartment:
                        dd.click()
                        break

            except Exception as e:
                print(e)

        else:
            try:
                aparts = self.driver.find_elements(*ML.DELETE_APART)
                re_aparts = reversed(aparts)
                for apart in re_aparts:
                    apart.click()

            except Exception as e:
                print(e)

        self.switchToParentFrame()
        self.driver.find_element(*ML.ADD_CONFIRM).click()
        if alert:
            self.switchToInnerFrame()
            WebDriverWait(self.driver,20).until(lambda x : alert in x.page_source)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CANCEL).click()
        else:
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x:'修改成功' in x.page_source)
            self.saveScreenshot(snapshot_name)
            WebDriverWait(self.driver, 20).until(lambda x: '修改成功' not in x.page_source)

    def modifyMenu(self,system_name='',menu_name='',name='',remark='',apartment='',snapshot_name='',alert=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            print(td1.text,'####')
            if td1.text == system_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            print(td1.text,'####')
            if td1.text == menu_name:
                tr.find_elements(*ML.TR_TD_BTN)[1].click()
                break
        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x:'<title>编辑菜单 </title>' in x.page_source)

        self.driver.find_element(*ML.ADD_MENU_NAME).clear()
        self.driver.find_element(*ML.ADD_MENU_NAME).send_keys(name)
        self.driver.find_element(*ML.ADD_MENU_REMARK).clear()
        self.driver.find_element(*ML.ADD_MENU_REMARK).send_keys(remark)

        if apartment:
            try:
                aparts = self.driver.find_elements(*ML.DELETE_APART)
                re_aparts = reversed(aparts)
                for apart in re_aparts:
                    apart.click()
                self.driver.find_element(*ML.ADD_APART).click()
                dds = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.ADD_MENU_APART_DD))
                self.driver.find_element(*ML.ADD_MENU_APART).click()
                for dd in dds:
                    if dd.text == apartment:
                        dd.click()
                        break

            except Exception as e:
                print(e)
        else:
            try:
                aparts = self.driver.find_elements(*ML.DELETE_APART)
                re_aparts = reversed(aparts)
                for apart in re_aparts:
                    apart.click()

            except Exception as e:
                print(e)
        self.switchToParentFrame()
        self.driver.find_element(*ML.ADD_CONFIRM).click()
        if alert:
            self.switchToInnerFrame()
            WebDriverWait(self.driver,20).until(lambda x : alert in x.page_source)
            self.saveScreenshot(snapshot_name+alert)
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CANCEL).click()
        else:
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x:'修改成功' in x.page_source)
            self.saveScreenshot(snapshot_name)
            WebDriverWait(self.driver, 20).until(lambda x: '修改成功' not in x.page_source)

    def modifyPage(self,system_name='',menu_name='',page_name='',name='',target='',remark='',apartment='',snapshot_name='',alert=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == system_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == menu_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == page_name:
                tr.find_elements(*ML.TR_TD_BTN)[1].click()
                break

        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x:'<title>编辑菜单 </title>' in x.page_source)

        self.driver.find_element(*ML.ADD_PAGE_NAME).clear()
        self.driver.find_element(*ML.ADD_PAGE_NAME).send_keys(name)
        self.driver.find_element(*ML.ADD_PAGE_TARGET).clear()
        self.driver.find_element(*ML.ADD_PAGE_TARGET).send_keys(target)
        self.driver.find_element(*ML.ADD_PAGE_REMARK).clear()
        self.driver.find_element(*ML.ADD_PAGE_REMARK).send_keys(remark)

        if apartment:
            try:
                aparts = self.driver.find_elements(*ML.DELETE_APART)
                re_aparts = reversed(aparts)
                for apart in re_aparts:
                    apart.click()
                self.driver.find_element(*ML.ADD_APART).click()
                dds = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.ADD_PAGE_APART_DD))
                self.driver.find_element(*ML.ADD_PAGE_APART).click()
                for dd in dds:
                    if dd.text == apartment:
                        dd.click()
                        break

            except Exception as e:
                print(e)
        else:
            try:
                aparts = self.driver.find_elements(*ML.DELETE_APART)
                re_aparts = reversed(aparts)
                for apart in re_aparts:
                    apart.click()

            except Exception as e:
                print(e)
        self.switchToParentFrame()
        self.driver.find_element(*ML.ADD_CONFIRM).click()

        if alert:
            self.switchToInnerFrame()
            WebDriverWait(self.driver, 20).until(lambda x: alert in x.page_source)
            self.saveScreenshot(snapshot_name + alert)
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CANCEL).click()
        else:
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x:'修改成功' in x.page_source)
            self.saveScreenshot(snapshot_name)
            WebDriverWait(self.driver, 20).until(lambda x: '修改成功' not in x.page_source)

    def modifyInterface(self,system_name='',menu_name='',page_name='',interface_name='',name='',target='',remark='',apartment='',snapshot_name='',alert=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == system_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == menu_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == page_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == interface_name:
                tr.find_elements(*ML.TR_TD_BTN)[1].click()
                break

        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x:'<title>编辑菜单 </title>' in x.page_source)

        self.driver.find_element(*ML.ADD_PAGE_NAME).clear()
        self.driver.find_element(*ML.ADD_PAGE_NAME).send_keys(name)
        self.driver.find_element(*ML.ADD_PAGE_TARGET).clear()
        self.driver.find_element(*ML.ADD_PAGE_TARGET).send_keys(target)
        self.driver.find_element(*ML.ADD_PAGE_REMARK).clear()
        self.driver.find_element(*ML.ADD_PAGE_REMARK).send_keys(remark)

        if apartment:
            try:
                aparts = self.driver.find_elements(*ML.DELETE_APART)
                re_aparts = reversed(aparts)
                for apart in re_aparts:
                    apart.click()
                self.driver.find_element(*ML.ADD_APART).click()
                dds = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.ADD_INTERFACE_APART_DD))
                self.driver.find_element(*ML.ADD_INTERFACE_APART).click()
                for dd in dds:
                    if dd.text == apartment:
                        dd.click()
                        break

            except Exception as e:
                print(e)
        else:
            try:
                aparts = self.driver.find_elements(*ML.DELETE_APART)
                re_aparts = reversed(aparts)
                for apart in re_aparts:
                    apart.click()

            except Exception as e:
                print(e)
        self.switchToParentFrame()
        self.driver.find_element(*ML.ADD_CONFIRM).click()
        if alert:
            self.switchToInnerFrame()
            WebDriverWait(self.driver, 20).until(lambda x: alert in x.page_source)
            self.saveScreenshot(snapshot_name + alert)
            self.switchToParentFrame()
            self.driver.find_element(*ML.ADD_CANCEL).click()
        else:
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x:'修改成功' in x.page_source)
            self.saveScreenshot(snapshot_name)
            WebDriverWait(self.driver, 20).until(lambda x: '修改成功' not in x.page_source)

    def deleteInterface(self,system_name='',menu_name='',page_name='',interface_name='',snapshot_name=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == system_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == menu_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == page_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == interface_name:
                tr.find_elements(*ML.TR_TD_BTN)[2].click()
                break

        WebDriverWait(self.driver,20).until(lambda x:'确定要删除吗？' in x.page_source)
        self.driver.find_element(*ML.DELETE_CONFIRM).click()
        self.switchToOuterFrame()

        WebDriverWait(self.driver,20).until(lambda x:'删除成功' in x.page_source)
        self.saveScreenshot(snapshot_name)
        WebDriverWait(self.driver, 20).until(lambda x: '删除成功' not in x.page_source)

    def deletePage(self,system_name='',menu_name='',page_name='',snapshot_name=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == system_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == menu_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == page_name:
                tr.find_elements(*ML.TR_TD_BTN)[2].click()
                break

        WebDriverWait(self.driver,20).until(lambda x:'确定要删除吗？' in x.page_source)
        self.driver.find_element(*ML.DELETE_CONFIRM).click()
        self.switchToOuterFrame()

        WebDriverWait(self.driver,20).until(lambda x:'删除成功' in x.page_source)
        self.saveScreenshot(snapshot_name)
        WebDriverWait(self.driver, 20).until(lambda x: '删除成功' not in x.page_source)

    def deleteMenu(self,system_name='',menu_name='',snapshot_name=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == system_name:
                tr.click()
                break

        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == menu_name:
                tr.find_elements(*ML.TR_TD_BTN)[2].click()
                break

        WebDriverWait(self.driver,20).until(lambda x:'确定要删除吗？' in x.page_source)
        self.driver.find_element(*ML.DELETE_CONFIRM).click()
        self.switchToOuterFrame()

        WebDriverWait(self.driver,20).until(lambda x:'删除成功' in x.page_source)
        self.saveScreenshot(snapshot_name)
        WebDriverWait(self.driver, 20).until(lambda x: '删除成功' not in x.page_source)

    def deleteSystem(self,system_name='',snapshot_name=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(ML.LOADING))
        WebDriverWait(self.driver, 10).until(lambda x: "<title>菜单管理</title>" in x.page_source)
        trs = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(ML.MENU_DATA_TR))
        for tr in reversed(trs):
            td1 = tr.find_element(*ML.TR_TD)
            ##print(td1.text,'####')
            if td1.text == system_name:
                tr.find_elements(*ML.TR_TD_BTN)[2].click()
                break

        WebDriverWait(self.driver,20).until(lambda x:'确定要删除吗？' in x.page_source)
        self.driver.find_element(*ML.DELETE_CONFIRM).click()
        self.switchToOuterFrame()

        WebDriverWait(self.driver,20).until(lambda x:'删除成功' in x.page_source)
        self.saveScreenshot(snapshot_name)
        WebDriverWait(self.driver, 20).until(lambda x: '删除成功' not in x.page_source)


