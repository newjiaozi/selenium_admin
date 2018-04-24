from .basePage import BasePage
from ..locator.apartmentLocator import ApartmentLocator as AL
from ..locator.apartmentLocator import AddApartmentLocator as AAL
from ..locator.apartmentLocator import ModifyApartmentLocator as MAL
from selenium.common.exceptions import NoSuchElementException,TimeoutException


class ApartmentManagePage(BasePage):

    def is_right_page(self):
        return super(ApartmentManagePage,self).is_right_page(AL.APARTMENT_MANAGE_BUTTION,'<title>部门管理</title>')

    def openTopAddPage(self,apart_name="",apart_chairman="",apart_type=0,apart_comment="",operation=3,alert_window=0,snapshot_name=''):
        ## operation 需要执行的操作，有三种，关闭页面，点击取消，点击确定
        ## 分别定义为  关闭页面：1，点击取消：2，点击确定：3,进行添加操作
        self.refreshPage()
        self.waitElementClick(AL.APARTMENT_MANAGE_BUTTION)  # 点击部门管理
        self.switchToIfame()
        self.waitAllElementPresent(AL.APARTMENT_NAME_TR)  # 点击  添加部门
        self.waitAllElementPresent(AL.ADD_CLASS)
        self.waitElementClick(AL.TOP_ADD) # 点击  添加部门
        self.waitLoading() ##
        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>添加部门/岗位 </title>')
        self.waitElementVisibility(AAL.NAME_LABEL)  ## 确定frame加载完成
        if operation == 1:  #点击取消
            self.switchToParentFrame()
            return self.waitElementClick(AAL.CLOSE_PAGE)

        elif operation == 2:  #点击确定
            self.switchToParentFrame()
            return self.waitElementClick(AAL.CANCLE_BUTTON)
        elif operation == 3:  #进行添加操作
            self.waitElementPresent(AAL.NAME_INPUT).send_keys(apart_name)  # 名字输入
            if apart_type == 0:
                self.waitElementClick(AAL.TYPE_RADIO_INNTER)
            else:
                self.waitElementClick(AAL.TYPE_RADIO_OUTER)
            self.waitElementVisibility(AAL.COMMENT_INPUT).send_keys(apart_comment)
            self.switchToParentFrame()
            self.waitElementClick(AAL.CONFIRM_BUTTON)

            if alert_window == 1:
                self.switchToInnerFrame()  # 切换到添加部门frame
                if self.waitStringinPagesource("必填项不能为空"):
                    self.saveScreenshot(snapshot_name+apart_name)
                    return True
                else:
                    return False
            return True
        else:
            return False

    def findApartmentsByNameAction(self,element,apart_name='',to_parent_name='',toParentApart='',operation=1,alert_window =0,snapshot_name='',selectList=[],addUser=False):
        elements_td = self.findElementsFromEle(element,AL.TD)
        elements_button = self.findElementsFromEle(element,AL.BUTTON)
        if elements_td[0].text == apart_name:
            result = self.clickButton1_5(elements_button[operation-1],apart_name=apart_name,to_parent_name=to_parent_name,toParentApart=toParentApart,operation=operation,alert_window = alert_window,snapshot_name=snapshot_name,selectList=selectList,addUser=addUser)
            return result
        else:
            return False

    def deleteEveryOne(self,apart_name_list,snapshot_name=''):
        self.frameOutIn()
        menu_elements = self.waitAllElementPresent(AL.APARTMENT_NAME_TR)
        for i in range(len(menu_elements),0,-1):
            menu_elements = self.expandAllApartments()
            elements_td = self.findElementsFromEle(menu_elements[i-1],AL.TD)
            if elements_td[0].text in apart_name_list:
                elements_button = self.findElementsFromEle(menu_elements[i-1],AL.BUTTON)
                self.clickButton1_5(elements_button[5],operation=6,snapshot_name=snapshot_name+str(i))

    def clickButton1_5(self,element,apart_name="",to_parent_name='',toParentApart='',operation=1,alert_window = 0,snapshot_name='',selectList=[],addUser=False):
        self.driver.execute_script('arguments[0].scrollIntoView()',element)
        element.click()
        if operation == 6: ## 删除操作
            self.waitStringinPagesource("确定要删除吗？")
            self.saveScreenshot(snapshot_name+'确定要删除吗')
            self.waitElementClick(AL.DELETE_CONFIRM)
            self.switchToOuterFrame()
            self.waitStringinPagesource('删除成功')
            self.saveScreenshot(snapshot_name+'删除成功')
            return self.waitStringNotinPagesource('删除成功')

        elif operation == 1:  ## 添加部门操作
            self.waitLoading()
            self.switchToInnerFrame()  # 切换到添加部门frame
            if self.waitStringinPagesource('<title>添加部门/岗位 </title>'):
                self.findElement(AAL.NAME_INPUT).send_keys(to_parent_name)  # '一二三四五六七八九十'*5
                self.findElement(AAL.COMMENT_INPUT).send_keys(to_parent_name)
                self.switchToParentFrame()
                return self.waitElementClick(AAL.CONFIRM_BUTTON)
            else:
                return False
        elif operation == 5: ## 修改部门
            self.waitLoading()
            self.switchToInnerFrame()  # 切换到添加部门frame
            dds = self.waitAllElementPresent(MAL.APART_OPTIONS)  ## 确定frame加载完成
            if self.waitStringinPagesource('<title>编辑部门 </title>'):
                self.saveScreenshot(snapshot_name+apart_name)
                if alert_window == 1:
                    assert self.findElement(MAL.NAME_INPUT).get_attribute("value") == apart_name  # '一二三四五六七八九十'*5
                    assert self.findElement(MAL.COMMENT_INPUT).get_attribute("value") == apart_name
                    assert self.findElement(MAL.APART_INPUT).get_attribute("value") == toParentApart
                    assert self.findElement(MAL.TYPE_RADIO_OUTER_CHECK).is_selected() is True
                    self.switchToParentFrame()
                    return self.waitElementClick(MAL.CLOSE_PAGE)
                self.findElement(MAL.NAME_INPUT).clear()
                self.findElement(MAL.NAME_INPUT).send_keys(to_parent_name)  # '一二三四五六七八九十'*5
                self.findElement(MAL.TYPE_RADIO_OUTER).click()
                self.findElement(MAL.COMMENT_INPUT).clear()
                self.findElement(MAL.COMMENT_INPUT).send_keys(to_parent_name)
                current_apart = self.findElement(MAL.APART_INPUT)
                if current_apart.get_attribute('value') == toParentApart:
                    self.switchToParentFrame()
                    return self.waitElementClick(MAL.CONFIRM_BUTTON)
                elif toParentApart:
                    dds = self.waitAllElementPresent(MAL.APART_OPTIONS)
                    current_apart.click()
                    for dd in dds:
                        if dd.text == toParentApart:
                            dd.click()
                            break
                    self.switchToParentFrame()
                    return self.waitElementClick(MAL.CONFIRM_BUTTON)
                else:
                    self.switchToParentFrame()
                    return self.waitElementClick(MAL.CONFIRM_BUTTON)
            else:
                return False
        elif operation == 3:## 分配角色
            # print('## 分配角色')
            self.waitLoading()
            self.switchToInnerFrame()
            self.waitStringinPagesource('<title>分配角色</title>')
            data_eles = self.waitAllElementPresent(AL.ROLE_APPLY_DATA)
            class_no = 'layui-unselect layui-form-checkbox'
            class_yes = 'layui-unselect layui-form-checkbox layui-form-checked'
            for ele in data_eles:
                try:
                    ele_span = self.findElementFromEle(ele,AL.ROLE_APPLY_DATA_SPAN)
                    ele_div = self.findElementFromEle(ele,AL.ROLE_APPLY_DATA_DIV)
                except NoSuchElementException as e:
                    print(e.stacktrace)
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
            self.saveScreenshot(snapshot_name+'修改后角色勾选情况')
            self.switchToParentFrame()
            self.waitElementClick(AL.ROLE_APPLY_CONFIRM)
            self.switchToOuterFrame()
            self.waitStringinPagesource("角色分配成功")
            self.saveScreenshot(snapshot_name + "角色分配成功")
            return True

        elif operation == 4:## 查询用户
            # print('## 查询用户')
            self.waitLoading()
            self.switchToInnerFrame()  ## 查询用户
            self.waitStringinPagesource('<title>查询用户</title>')
            if not addUser:
                if not selectList:  ##addUser 为False，如果user_list也为空，则当前没有用户;
                    return self.waitStringinPagesource('此部门没有绑定用户！')
                else:  ##如果addUser为False，user_List不为空，把list中用户删除;
                    datas = self.waitAllElementPresent(AL.CHECK_USER_DATA)
                    class_no = 'layui-unselect layui-form-checkbox'
                    # class_yes = 'layui-unselect layui-form-checkbox layui-form-checked'
                    for data in datas:
                        data_div = self.findElementFromEle(data,AL.CHECK_USER_DIV)
                        div_span = self.findElementFromEle(data,AL.CHECK_USER_SPAN)
                        if div_span.text.split('/')[1] in selectList:
                            if data_div.get_attribute('class') == class_no:
                                div_span.click()
                            else:
                                pass
                        else:
                            if data_div.get_attribute('class') == class_no:
                                pass
                            else:
                                div_span.click()
                    self.switchToParentFrame()
                    self.saveScreenshot(snapshot_name+'删除勾选')
                    self.waitElementClick(AL.CHECK_USER_DELETE)
                    self.switchToOuterFrame()
                    self.waitStringinPagesource('删除成功！')
                    self.saveScreenshot(snapshot_name+'删除成功！')
                    return self.waitStringNotinPagesource('删除成功！')

            else:
                if selectList:  ##addUser为True、user_list不为空，则将user_list用户添加上;
                    for user_data in selectList:
                        self.waitElementVisibility(AL.CHECK_USER_ADD_USRE_INPUT).send_keys(user_data)
                        self.waitElementClick(AL.CHECK_USER_SEARCH_USER)
                        if self.waitStringinPagesource('未查询到此用户，请确认后查询！'):
                            return self.saveScreenshot(snapshot_name+'未查询到此用户')

                        else:
                            self.saveScreenshot(snapshot_name+"查询用户成功")
                            self.waitElementClick(AL.CHECK_USER_ADD_USER_COMMIT)
                            self.saveScreenshot(snapshot_name+"添加用户成功")
                            self.switchToParentFrame()
                            return self.waitElementClick(AL.CHECK_USER_CANCEL)


                else:
                    return False


        else:
            return False

    def clickTopApartment(self):
        self.waitElementVisibility(AL.TOP_APARTMENT).click()

    def ifApartmentNameInPage(self,apart_name,snapshot_name=''):
        self.expandAllApartments()
        if apart_name in self.driver.page_source:
            self.saveScreenshot(snapshot_name+'ifApartmentNameInPage')
            return True
        else:
            return False

    def addTestData(self,apart_name='',toName='',snapshot_name=''):
        menu_elements = self.expandAllApartments()
        for element in menu_elements:  #
            result = self.findApartmentsByNameAction(element=element,apart_name=apart_name,to_parent_name=toName,operation=1,snapshot_name=snapshot_name)
            if result:
                break
            else:
                continue

    ## 展示出所有的部门！
    def expandAllApartments(self):
        self.refreshPage()
        self.waitElementClick(AL.APARTMENT_MANAGE_BUTTION)
        self.switchToIfame()
        menu_elements = self.waitAllElementPresent(AL.APARTMENT_NAME_TR)
        for ele in menu_elements:
            old_class = ele.get_attribute("class")
            self.driver.execute_script('arguments[0].style = "display: table-row;"',ele)
            new_class = old_class.replace("treegrid-collapse","treegrid-expanded")
            self.driver.execute_script('arguments[0].className = arguments[1]',ele,new_class)
        return menu_elements

    def modifyApartment(self,apart_name,to_parent_name='',toParentApart='',snapshot_name=''):
        menu_elements = self.expandAllApartments()
        for element in menu_elements:  #
            result = self.findApartmentsByNameAction(element,apart_name=apart_name,to_parent_name=to_parent_name,toParentApart=toParentApart,operation=5,snapshot_name=snapshot_name)
            if result:
                break
            else:
                continue

    def ifModifySucceed(self,apart_name,toParentApart,snapshot_name=''):
        menu_elements = self.expandAllApartments()
        for element in menu_elements:  #
            result = self.findApartmentsByNameAction(element,apart_name,to_parent_name='',toParentApart=toParentApart,operation=5,alert_window=1,snapshot_name=snapshot_name)
            if result:
                break
            else:
                continue
        return result

    def applyRole(self,apartment_name='',role_list=[],snapshot_name=''):
        apart_elements = self.expandAllApartments()
        for element in apart_elements:
            result = self.findApartmentsByNameAction(element,apart_name = apartment_name,operation=3,selectList=role_list,snapshot_name=snapshot_name)
            if result:
                break
            else:
                continue

    def checkApplyUser(self,apartment_name='',user_list=[],addUser=False,snapshot_name=''): ## 1.addUser 为False，如果user_list也为空，则当前没有用户;
                                                                            # 2.addUser为True、user_list不为空，则将user_list用户添加上;
                                                                            # 3.如果addUser为False，user_List不为空，把list中用户删除;
        apart_elements = self.expandAllApartments()
        for element in apart_elements:
            result = self.findApartmentsByNameAction(element,apart_name = apartment_name,operation=4,selectList=user_list,addUser=addUser,snapshot_name=snapshot_name)
            if result:
                break
            else:
                continue
