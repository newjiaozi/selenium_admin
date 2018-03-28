from .basePage import BasePage
from ..locator.apartmentLocator import ApartmentLocator as AL
from ..locator.apartmentLocator import AddApartmentLocator as AAL
from ..locator.apartmentLocator import ModifyApartmentLocator as MAL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ApartmentManagePage(BasePage):

    def is_right_page(self):
        result1 =  self.driver.title == "麦子金服管理后台"
        self.getInQXXT()
        self.driver.find_element(*AL.APARTMENT_MANAGE_BUTTION).click()  # 点击部门管理
        self.driver.switch_to.frame("jumpIframe")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(AL.TOP_APARTMENT))
        result2 = "<title>部门管理</title>" in self.driver.page_source
        self.driver.switch_to.default_content()
        return result2 & result1

    def openTopAddPage(self,apart_name="",apart_chairman="",apart_type=0,apart_comment="",operation=3,alert_window=0,snapshot_name=''):

        ## operation 需要执行的操作，有三种，关闭页面，点击取消，点击确定
        ## 分别定义为  关闭页面：1，点击取消：2，点击确定：3,进行添加操作
        self.driver.refresh()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AL.APARTMENT_MANAGE_BUTTION)).click()  # 点击部门管理
        # self.driver.switch_to.frame("jumpIframe")
        self.switchToIfame()
        # WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it("jumpIframe"))
        WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(AL.APARTMENT_NAME_TR))  # 点击  添加部门
        # print("即将点击添加部门")
        WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(AL.ADD_CLASS))
        ##self.pause4Seconds()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(AL.TOP_ADD)).click() # 点击  添加部门
        # WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it("layui-layer-iframe1"))
        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x:'<title>添加部门/岗位 </title>' in x.page_source)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(AAL.NAME_LABEL))  ## 确定frame加载完成
        if operation == 1:
            self.switchToParentFrame()
            self.driver.find_element(*AAL.CLOSE_PAGE).click()
            return True
        elif operation == 2:
            self.switchToParentFrame()
            self.driver.find_element(*AAL.CANCLE_BUTTON).click()
            return True
        elif operation == 3:
            self.driver.find_element(*AAL.NAME_INPUT).send_keys(apart_name)  # 名字输入
            # self.driver.find_element(*AAL.CHAIRMAN_INPUT).send_keys(apart_chairman) #负责人输入
            if apart_type == 0:
                self.driver.find_element(*AAL.TYPE_RADIO_INNTER).click()
            else:
                self.driver.find_element(*AAL.TYPE_RADIO_OUTER).click()
            self.driver.find_element(*AAL.COMMENT_INPUT).send_keys(apart_comment)
            self.driver.switch_to.parent_frame()
            self.driver.find_element(*AAL.CONFIRM_BUTTON).click()
            if alert_window == 1:
                self.driver.switch_to.frame("layui-layer-iframe1")  # 切换到添加部门frame
                assert "必填项不能为空" in self.driver.page_source
                self.saveScreenshot(snapshot_name+apart_name)
            return True
        else:
            return False

    def findApartmentsByNameAction(self,element,apart_name,to_parent_name,operation,alert_window =0,snapshot_name=''):
        elements_td = element.find_elements(*AL.TD)
        elements_button = element.find_elements(*AL.BUTTON)
        if elements_td[0].text == apart_name:
            result = self.clickButton1_5(elements_button[operation-1],apart_name,to_parent_name,operation,alert_window = alert_window,snapshot_name=snapshot_name)
            return result
        else:
            return False

    def deleteEveryOne(self,apart_name_list,snapshot_name=''):
        menu_elements = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(AL.APARTMENT_NAME_TR))
        for i in range(len(menu_elements),0,-1):
            menu_elements = self.expandAllApartments()
            elements_td = menu_elements[i-1].find_elements(*AL.TD)
            if elements_td[0].text in apart_name_list:
                elements_button = menu_elements[i - 1].find_elements(*AL.BUTTON)
                self.clickButton1_5(elements_button[5],operation=6,snapshot_name=snapshot_name)

    def clickButton1_5(self,element,apart_name="",to_parent_name='',operation=1,alert_window = 0,snapshot_name=''):
        ##self.pause4Seconds()
        element.click()
        if operation == 6: ## 删除操作
            WebDriverWait(self.driver,10).until(lambda x: "确定要删除吗？" in x.page_source)
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(AL.DELETE_CONFIRM)).click()
            return True
        elif operation == 1:  ## 添加部门操作
            self.driver.switch_to.frame("layui-layer-iframe1")  # 切换到添加部门frame
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AAL.NAME_LABEL))  ## 确定frame加载完成
            assert '<title>添加部门/岗位 </title>' in self.driver.page_source
            self.driver.find_element(*AAL.NAME_INPUT).send_keys(apart_name)  # '一二三四五六七八九十'*5
            self.driver.find_element(*AAL.COMMENT_INPUT).send_keys(apart_name)
            self.driver.switch_to.parent_frame()
            self.driver.find_element(*AAL.CONFIRM_BUTTON).click()
            return True
        elif operation == 5: ## 修改部门
            self.driver.switch_to.frame("layui-layer-iframe1")  # 切换到添加部门frame
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(AAL.NAME_LABEL))  ## 确定frame加载完成
            assert '<title>编辑部门 </title>' in self.driver.page_source
            self.saveScreenshot(snapshot_name+apart_name)
            if alert_window == 1:
                assert self.driver.find_element(*MAL.NAME_INPUT).get_attribute("value") == apart_name  # '一二三四五六七八九十'*5
                assert self.driver.find_element(*MAL.COMMENT_INPUT).get_attribute("value") == apart_name
                assert self.driver.find_element(*MAL.TYPE_RADIO_OUTER_CHECK).is_selected() is True
                self.driver.switch_to.parent_frame()
                self.driver.find_element(*MAL.CLOSE_PAGE).click()
                return True
            self.driver.find_element(*MAL.NAME_INPUT).send_keys(apart_name)  # '一二三四五六七八九十'*5
            # self.driver.find_element(*MAL.CHAIRMAN_INPUT).send_keys(apart_name)
            self.driver.find_element(*MAL.TYPE_RADIO_OUTER).click()
            self.driver.find_element(*MAL.COMMENT_INPUT).send_keys(apart_name)

            current_apart = self.driver.find_element(*MAL.APART_INPUT)
            if current_apart.get_attribute('value') == to_parent_name:

                self.driver.switch_to.parent_frame()
                self.driver.find_element(*MAL.CONFIRM_BUTTON).click()
                return True
            elif to_parent_name:
                dds = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(MAL.APART_OPTIONS))
                for dd in dds:
                    if dd.text == to_parent_name:
                        dd.click()
                        break
                self.driver.switch_to.parent_frame()
                self.driver.find_element(*MAL.CONFIRM_BUTTON).click()
                return True
            else:
                self.driver.switch_to.parent_frame()
                self.driver.find_element(*MAL.CONFIRM_BUTTON).click()
                return True

        else:
            return False

    def clickTopApartment(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(AL.TOP_APARTMENT)).click()

    def webdriverWait10Click(self,locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator)).click()  # 点击  添加部门

    def ifApartmentNameInPage(self,apart_name,snapshot_name=''):
        self.expandAllApartments()
        if apart_name in self.driver.page_source:
            self.saveScreenshot(snapshot_name+'ifApartmentNameInPage')
            return True
        else:
            return False

    def addTestData(self,apart_name,snapshot_name=''):
        menu_elements = self.expandAllApartments()
        ##self.pause4Seconds()
        for element in menu_elements:  #
            result = self.findApartmentsByNameAction(element,apart_name,to_parent_name='',operation=1,snapshot_name=snapshot_name)
            if result:
                break
            else:
                continue

    ## 展示出所有的部门！
    def expandAllApartments(self):
        self.driver.refresh()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(AL.APARTMENT_MANAGE_BUTTION)).click()  # 点击部门管理
        self.switchToIfame()
        menu_elements = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(AL.APARTMENT_NAME_TR))
        for ele in menu_elements:
            old_class = ele.get_attribute("class")
            self.driver.execute_script('arguments[0].style = "display: table-row;"',ele)
            new_class = old_class.replace("treegrid-collapse","treegrid-expanded")
            self.driver.execute_script('arguments[0].className = arguments[1]',ele,new_class)
        return menu_elements

    def modifyApartment(self,apart_name,to_parent_name='',snapshot_name=''):
        menu_elements = self.expandAllApartments()
        ##self.pause4Seconds()
        for element in menu_elements:  #
            result = self.findApartmentsByNameAction(element,apart_name,to_parent_name,operation=5,snapshot_name=snapshot_name)
            if result:
                break
            else:
                continue

    def ifModifySucceed(self,apart_name,snapshot_name=''):
        menu_elements = self.expandAllApartments()
        ##self.pause4Seconds()
        for element in menu_elements:  #
            result = self.findApartmentsByNameAction(element,apart_name,to_parent_name='',operation=5,alert_window=1,snapshot_name=snapshot_name)
            if result:
                break
            else:
                continue
        return result

    def applyRole(self):
        pass

    def checkApplyUser(self):
        pass

