from .basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from ..locator.userLocator import UserLocator as UL
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from com.test.pageOperation.loginPage import Login




class UserManagePage(BasePage):

    def is_right_page(self):
        return super(UserManagePage,self).is_right_page(UL.USER_MANAGE_BUTTON,"<title>用户管理</title>")

    def searchByName(self,name):
        self.frameOutIn()
        self.findElement(UL.NAME_INPUT).clear()
        self.findElement(UL.LOGIN_NAME_INPUT).clear()
        self.findElement(UL.NAME_INPUT).send_keys(name)
        try:
            self.waitElementClick(UL.SEARCH_BUTTON)
            self.waitLoading()
            data_eles = self.findElements(UL.TABLE_TR)
            if data_eles:
                for ele in data_eles:
                    assert name in self.findElementFromEle(ele,UL.TR_TD_NAME).text
                return 1 # 检索出的数据都含有 name，校验通过
            else:
                return 2 # 没有根据name检索到数据
        except Exception as e:
            print(e)
            return 0 # 报错检测失败

    def searchByLoginName(self,loginname):
        self.frameOutIn()
        self.findElement(UL.NAME_INPUT).clear()
        self.findElement(UL.LOGIN_NAME_INPUT).clear()
        self.findElement(UL.LOGIN_NAME_INPUT).send_keys(loginname)

        try:
            self.waitElementClick(UL.SEARCH_BUTTON)
            self.waitLoading()
            data_eles = self.findElements(UL.TABLE_TR)
            if data_eles:
                for ele in data_eles:
                    assert loginname in self.findElementFromEle(ele,UL.TR_TD_LOGIN_NAME).text
                return 1 # 检索出的数据都含有 loginname，校验通过
            else:

                return 2 # 没有根据loginname检索到数据
        except Exception as e:
            print(e)
            return 0 # 报错检测失败

    def addUser(self,name='',loginname='',passwd='',repasswd='',mail='',mobile='',apartment='',alert='',close = True,long_size={},snapshot_name=''):
        self.frameOutIn()
        self.waitAllElementPresent(UL.TABLE_TR)
        self.waitElementClick(UL.ADD_BUTTON)
        self.waitLoading()
        self.switchToInnerFrame()
        self.waitStringinPagesource("<title>添加用户 </title>")

        self.findElement(UL.ADD_NAME_INPUT).send_keys(name)
        self.findElement(UL.ADD_LOGIN_NAME_INPUT).send_keys(loginname)
        self.findElement(UL.ADD_PASSWD_INPUT).send_keys(passwd)
        self.findElement(UL.ADD_REPASSWD_INPUT).send_keys(repasswd)
        self.findElement(UL.ADD_MAIL_INPUT).send_keys(mail)
        self.findElement(UL.ADD_MOBILE_INPUT).send_keys(mobile)

        if apartment: ## 如果需要输入部门，根据部门的text进行选择
            dds = self.waitAllElementPresent(UL.ADD_APART_INPUT_DD)
            self.waitElementPresent(UL.ADD_APART_INPUT_TRIANGLE_CLASS)
            self.waitElementClick(UL.ADD_APART_INPUT_CLASS)
            for dd in dds:
                if apartment == dd.text:
                    dd.click()
                    break

        if long_size:  ## 字典中有的key是需要确认输入框实际输入的字符的 多少
            result = True
            if "name" in long_size:
                assert len(self.findElement(UL.ADD_NAME_INPUT).get_attribute('value')) == long_size['name']
            elif "loginname" in long_size:
                assert len(self.findElement(UL.ADD_LOGIN_NAME_INPUT).get_attribute('value')) == long_size['loginname']

            elif "passwd" in long_size:
                assert len(self.findElement(UL.ADD_PASSWD_INPUT).get_attribute('value')) == long_size['passwd']

            elif "mail" in long_size:
                assert len(self.findElement(UL.ADD_MAIL_INPUT).get_attribute('value')) == long_size['mail']

            elif "mobile" in long_size:
                assert len(self.findElement(UL.ADD_MOBILE_INPUT).get_attribute('value')) == long_size['mobile']
            else:
                result = False

            self.saveScreenshot(snapshot_name+alert)  #截图
            self.switchToParentFrame()
            self.waitElementClick(UL.ADD_BTN_CANCEL)
            return result

        self.switchToParentFrame() #切换到上级frame
        self.waitElementClick(UL.ADD_BTN_CONFIRM)

        if close:  # 预期需要关闭对话框的，需要在此关闭
            self.switchToInnerFrame()
            self.waitStringinPagesource(alert) ## 等待预期的alert的字符出现在pagesource
            self.saveScreenshot(snapshot_name+alert)  #截图
            self.switchToParentFrame()
            return self.waitElementClick(UL.ADD_BTN_CANCEL)#点击取消关闭对话框

        else:
            self.switchToOuterFrame()
            self.waitStringinPagesource(alert) ##等待预期的alert的字符出现在pagesource
            self.saveScreenshot(snapshot_name+alert)   #截图
            return self.waitStringNotinPagesource(alert)

    def refreshData(self):
        self.frameOutIn()
        self.waitElementClick(UL.REFRESH_BUTTON)

    def deleteUser(self,index,snapshot_name):
        data_eles = self.waitAllElementPresent(UL.TABLE_TR)
        if data_eles:
            for ele in data_eles:
                self.findElementFromEle(ele,UL.TR_TD_DELETE).click()
                self.switchToOuterFrame()
                self.waitStringinPagesource("删除成功")
                self.saveScreenshot("%s删除提示%s" % (snapshot_name,index))
                self.waitStringNotinPagesource("删除成功")
                break
        else:
            print('无查询结果可操作')

    def deleteUserAll(self,snapshot_name):
        self.frameOutIn()
        data_eles = self.findElements(UL.TABLE_TR)
        for i in range(0,len(data_eles)):
            self.deleteUser(index=i,snapshot_name=snapshot_name)
        return True

    def permissionManage(self,selectList,snapshot_name = ''):
        self.frameOutIn()
        class_no = 'layui-unselect layui-form-checkbox'
        class_yes = 'layui-unselect layui-form-checkbox layui-form-checked'
        self.waitElementClick(UL.FIRST_USER_DATA_PM)
        self.waitLoading()
        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>用户管理</title>')
        data_eles = self.findElements(UL.ROLE_APPLY_DATA)
        for ele in data_eles:
            try:
                ele_span = self.findElementFromEle(ele,UL.ROLE_APPLY_DATA_SPAN)
                ele_div = self.findElementFromEle(ele,UL.ROLE_APPLY_DATA_DIV)
            except NoSuchElementException as e:
                print(e)
                break
            ele_span_text = ele_span.text
            if ele_span_text in selectList:
                if ele_div.get_attribute('class') == class_no:
                    ele_span.click()
                else:
                    pass
            else:
                if ele_div.get_attribute('class') == class_yes:
                    ele_span.click()
                else:
                    pass
        self.saveScreenshot(snapshot_name)
        self.switchToParentFrame()
        self.waitElementClick(UL.ROLE_APPLY_SAVE_CONFIRM)
        self.switchToOuterFrame()
        self.waitStringinPagesource("修改权限成功")
        WebDriverWait(self.driver,20).until(lambda x : "修改权限成功" in x.page_source)
        self.saveScreenshot(snapshot_name+"修改权限成功")
        return self.waitStringNotinPagesource("修改权限成功")

    def changeLoginStatus(self,toStatus,snapshot_name=''):  ## toStatus ='1'时，可以登录；toStatus='0'时，禁止登录。
        self.frameOutIn()
        btn = self.waitElementClickEle(UL.FIRST_USER_DATA_CS)
        btn_status = btn.get_attribute('data-status')
        if toStatus == btn_status:
            return True
        else:
            btn.click()
            self.switchToOuterFrame()
            self.waitStringinPagesource('状态修改成功')
            self.saveScreenshot("%s%s" % (snapshot_name,"状态修改成功"))
            return self.waitStringNotinPagesource('状态修改成功')

    def checkStatus(self,status='禁止登录	',snapshot_name=''):
        self.frameOutIn()
        sta = self.waitElementPresent(UL.FIRST_USER_DATA_ST)
        if status in sta.text:
            self.saveScreenshot(snapshot_name)
            return True
        else:
            return False







