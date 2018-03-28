from .basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from ..locator.userLocator import UserLocator as UL
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from com.test.pageOperation.loginPage import Login




class UserManagePage(BasePage):
    def is_right_page(self):
        assert self.driver.title == "麦子金服管理后台"
        self.getInQXXT()
        self.driver.find_element(*UL.USER_MANAGE_BUTTON).click()  # 点击部门管理
        self.driver.switch_to.frame("jumpIframe")
        try:
            WebDriverWait(self.driver,10).until(lambda x: "<title>用户管理</title>" in x.page_source)
            self.driver.switch_to.default_content()
            return True
        except Exception as e:
            print(e)
            return False

    def searchByName(self,name):
        self.switchToOuterFrame()
        self.switchToIfame()
        self.driver.find_element(*UL.NAME_INPUT).clear()
        self.driver.find_element(*UL.LOGIN_NAME_INPUT).clear()
        self.driver.find_element(*UL.NAME_INPUT).send_keys(name)
        WebDriverWait(self.driver, 20).until_not(EC.visibility_of_element_located(UL.LOADING))
        self.driver.find_element(*UL.SEARCH_BUTTON).click()
        try:
            WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(UL.LOADING))
            data_eles = self.driver.find_elements(*UL.TABLE_TR)
            if data_eles:
                for ele in data_eles:
                    assert name in ele.find_element(*UL.TR_TD_NAME).text
                # WebDriverWait(self.driver, 20).until_not(EC.presence_of_all_elements_located(UL.VIEW_SHADE))

                return 1 # 检索出的数据都含有 name，校验通过

            else:
                # WebDriverWait(self.driver, 20).until_not(EC.presence_of_all_elements_located(UL.VIEW_SHADE))

                return 2 # 没有根据name检索到数据
        except Exception as e:
            print(e)
            # WebDriverWait(self.driver, 20).until_not(EC.presence_of_all_elements_located(UL.VIEW_SHADE))

            return 0 # 报错检测失败

    def searchByLoginName(self,loginname):
        self.switchToOuterFrame()
        self.switchToIfame()
        self.driver.find_element(*UL.NAME_INPUT).clear()
        self.driver.find_element(*UL.LOGIN_NAME_INPUT).clear()
        self.driver.find_element(*UL.LOGIN_NAME_INPUT).send_keys(loginname)
        try:
            WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(UL.LOADING))
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(UL.SEARCH_BUTTON)).click()
            WebDriverWait(self.driver,20).until_not(EC.visibility_of_element_located(UL.LOADING))
            data_eles = self.driver.find_elements(*UL.TABLE_TR)
            if data_eles:
                for ele in data_eles:
                    assert loginname in ele.find_element(*UL.TR_TD_LOGIN_NAME).text
                # WebDriverWait(self.driver, 20).until_not(EC.presence_of_all_elements_located(UL.VIEW_SHADE))
                return 1 # 检索出的数据都含有 loginname，校验通过

            else:

                # WebDriverWait(self.driver, 20).until_not(EC.presence_of_all_elements_located(UL.VIEW_SHADE))

                return 2 # 没有根据loginname检索到数据
        except Exception as e:
            print(e)
            # WebDriverWait(self.driver, 20).until_not(EC.presence_of_all_elements_located(UL.VIEW_SHADE))

            return 0 # 报错检测失败

    def addUser(self,name='',loginname='',passwd='',repasswd='',mail='',mobile='',apartment='',alert='',close = True,long_size={},snapshot_name=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        self.driver.find_element(*UL.ADD_BUTTON).click()
        # self.driver.find_element(*UL.MAX_WINDOW_CLASS).click()
        WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it(UL.INNER_IFRAME))
        WebDriverWait(self.driver,20).until(lambda x: "<title>添加用户 </title>" in x.page_source)
        self.driver.find_element(*UL.ADD_NAME_INPUT).send_keys(name)
        self.driver.find_element(*UL.ADD_LOGIN_NAME_INPUT).send_keys(loginname)
        self.driver.find_element(*UL.ADD_PASSWD_INPUT).send_keys(passwd)
        self.driver.find_element(*UL.ADD_REPASSWD_INPUT).send_keys(repasswd)
        self.driver.find_element(*UL.ADD_MAIL_INPUT).send_keys(mail)
        self.driver.find_element(*UL.ADD_MOBILE_INPUT).send_keys(mobile)

        if apartment: ## 如果需要输入部门，根据部门的text进行选择

            dds = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(UL.ADD_APART_INPUT_DD))
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(UL.ADD_APART_INPUT_TRIANGLE_CLASS))
            self.driver.find_element(*UL.ADD_APART_INPUT_CLASS).click()
            # import time;time.sleep(1)
            for dd in dds:
                if apartment == dd.text:
                    # self.driver.execute_script('arguments[0].className = arguments[1]',dd,'layui-this')
                    dd.click()
                    break


        if long_size:  ## 字典中有的key是需要确认输入框实际输入的字符的 多少
            result = True
            if "name" in long_size:
                assert len(self.driver.find_element(*UL.ADD_NAME_INPUT).get_attribute('value')) == long_size['name']
            elif "loginname" in long_size:
                assert len(self.driver.find_element(*UL.ADD_LOGIN_NAME_INPUT).get_attribute('value')) == long_size['loginname']

            elif "passwd" in long_size:
                assert len(self.driver.find_element(*UL.ADD_PASSWD_INPUT).get_attribute('value')) == long_size['passwd']

            elif "mail" in long_size:
                assert len(self.driver.find_element(*UL.ADD_MAIL_INPUT).get_attribute('value')) == long_size['mail']

            elif "mobile" in long_size:
                assert len(self.driver.find_element(*UL.ADD_MOBILE_INPUT).get_attribute('value')) == long_size['mobile']
            else:
                result = False

            self.saveScreenshot(snapshot_name+alert)  #截图
            self.switchToParentFrame()
            self.driver.find_element(*UL.ADD_BTN_CANCEL).click() #点击取消关闭对话框
            return result

        self.switchToParentFrame() #切换到上级frame
        # import time;time.sleep(10)
        self.driver.find_element(*UL.ADD_BTN_CONFIRM).click()  #点击提交保存
        if close:  # 预期需要关闭对话框的，需要在此关闭
            self.switchToInnerFrame()
            WebDriverWait(self.driver,20).until(lambda x : alert in x.page_source)  ## 等待预期的alert的字符出现在pagesource
            self.saveScreenshot(snapshot_name+alert)  #截图
            self.switchToParentFrame()
            self.driver.find_element(*UL.ADD_BTN_CANCEL).click() #点击取消关闭对话框
            return True

        else:
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x: alert in x.page_source)  ##等待预期的alert的字符出现在pagesource
            self.saveScreenshot(snapshot_name+alert)   #截图
            return True

    def refreshData(self):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(UL.REFRESH_BUTTON)).click()

    def deleteUser(self,index,snapshot_name):
        data_eles = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(UL.TABLE_TR))
        if data_eles:
            for ele in data_eles:
                ele.find_element(*UL.TR_TD_DELETE).click()
                self.switchToOuterFrame()
                WebDriverWait(self.driver,20).until(lambda x : "删除成功" in x.page_source)
                self.saveScreenshot("%s删除提示%s" % (snapshot_name,index))
                break
        else:
            print('无查询结果可操作')

    def deleteUserAll(self,snapshot_name):
        self.switchToOuterFrame()
        self.switchToIfame()
        data_eles = self.driver.find_elements(*UL.TABLE_TR)
        for i in range(0,len(data_eles)):
            self.deleteUser(index=i,snapshot_name=snapshot_name)

        return True

    def permissionManage(self,selectList,snapshot_name = ''):
        self.switchToOuterFrame()
        self.switchToIfame()
        class_no = 'layui-unselect layui-form-checkbox'
        class_yes = 'layui-unselect layui-form-checkbox layui-form-checked'
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(UL.FIRST_USER_DATA_PM)).click()
        WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it(UL.INNER_IFRAME))
        WebDriverWait(self.driver,20).until(lambda x : '<title>用户管理</title>' in x.page_source)
        data_eles = self.driver.find_elements(*UL.ROLE_APPLY_DATA)
        for ele in data_eles:
            try:
                ele_span = ele.find_element(*UL.ROLE_APPLY_DATA_SPAN)
                ele_div = ele.find_element(*UL.ROLE_APPLY_DATA_DIV)
            except NoSuchElementException as e:
                print(e)
                break
            ele_span_text = ele_span.text
            if ele_span_text in selectList:
                if ele_div.get_attribute('class') == class_no:
                    # print("@@@@@@",ele_span_text,selectList)
                    ele_span.click()
                else:
                    pass
            else:
                if ele_div.get_attribute('class') == class_yes:
                    # print("@@@@@@",ele_span_text,selectList)
                    ele_span.click()
                else:
                    pass
        self.saveScreenshot(snapshot_name)
        self.switchToParentFrame()
        self.driver.find_element(*UL.ROLE_APPLY_SAVE_CONFIRM).click()
        self.switchToOuterFrame()
        WebDriverWait(self.driver,20).until(lambda x : "修改权限成功" in x.page_source)
        self.saveScreenshot(snapshot_name+"修改权限成功")
        # WebDriverWait(self.driver,20).until(lambda x : "修改权限成功" not in x.page_source)

        return True



    def changeLoginStatus(self,toStatus,snapshot_name=''):  ## toStatus ='1'时，可以登录；toStatus='0'时，禁止登录。
        self.switchToOuterFrame()
        self.switchToIfame()
        btn = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(UL.FIRST_USER_DATA_CS))
        btn_status = btn.get_attribute('data-status')
        # print(toStatus,btn_status,len(btn_status))
        if toStatus == btn_status:
            return True
        else:
            btn.click()
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x : '状态修改成功' in x.page_source)
            self.saveScreenshot("%s%s" % (snapshot_name,"状态修改成功"))
            WebDriverWait(self.driver,20).until(lambda x : '状态修改成功' not in x.page_source)
            return True

    def checkStatus(self,status='禁止登录	',snapshot_name=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        sta = WebDriverWait(self.driver,20).until(EC.presence_of_element_located(UL.FIRST_USER_DATA_ST))
        # print(status,len(status),sta.text,len(sta.text))
        if status in sta.text:
            self.saveScreenshot(snapshot_name)
            return True
        else:
            return False

    def getNewWindowLogin(self,url_new,snapshot_name):
        cks = self.driver.get_cookies()
        print(cks)
        self.driver.delete_all_cookies()
        cur_handle = self.driver.current_window_handle
        import time;time.sleep(5)
        self.driver.execute_script('window.open("%s")' % url_new)
        import time;time.sleep(15)


        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                Login(self.driver).login2('guobaorou','guobaorou',snapshot_name)
                import time;
                time.sleep(5)

                break
        self.driver.close()
        self.driver.switch_to.window(cur_handle)






