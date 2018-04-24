from .basePage import BasePage
from ..locator.roleLocator import RoleLocator as RL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class RoleManagePage(BasePage):
    def is_right_page(self):
        return super(RoleManagePage,self).is_right_page(RL.ROLE_MANAGE_BUTTON,"<title>角色列表</title>")


    def addRole(self,role_name='',role_code='',role_apart='',snapshot_name='',pathname='',menu_list={}):     ## menu_list = {'权限系统':[],'贷后系统':[]}
        self.frameOutIn()
        self.waitAllElementPresent(RL.ROLE_DATA_TR)
        self.waitElementClick(RL.ADD_ROLE_BUTTON)
        self.waitLoading()
        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>添加角色</title>')
        self.waitAllElementPresent(RL.MENU_ALL_CHECKBOX)

        self.findElement(RL.ADD_ROLE_NAME).clear()
        self.findElement(RL.ADD_ROLE_NAME).send_keys(role_name)
        self.findElement(RL.ADD_ROLE_TYPE_VALUE).clear()
        self.findElement(RL.ADD_ROLE_TYPE_VALUE).send_keys(role_code)

        aos = self.waitAllElementPresent(RL.APART_OPTIONS)
        self.waitElementClick(RL.ADD_ROLE_APART_INPUT)

        for ao in aos:
            if role_apart == ao.text:
                ao.click()
                break
        if menu_list:
            for key,values in menu_list.items():
                self.waitAllElementPresent(RL.MENU_LIST_TITLE)
                self.waitElementClick((RL.MENU_LIST_A[0], RL.MENU_LIST_A[1] % key))
                for value in values:
                    divs = self.waitAllElementPresent(RL.MENU_LIST_DIV)
                    for div in divs:
                        span = self.findElementFromEle(div,RL.ROLE_USER_SPAN)
                        if span.text == value:
                            self.driver.execute_script('arguments[0].click()',span)
                            break

        self.switchToParentFrame()
        self.waitElementClick(RL.SAVE_SUBMIT)
        self.switchToOuterFrame()
        self.waitStringinPagesource('角色添加成功！')
        self.saveScreenshot(pathname+snapshot_name)
        return self.waitStringNotinPagesource('角色添加成功！')




    def queryRoleByName(self,role_name='',pathname='',snapshot_name=''):
        self.frameOutIn()
        self.findElement(RL.ROLE_NAME).clear()
        self.findElement(RL.ROLE_NAME).send_keys(role_name)
        self.waitElementClick(RL.SEARCH_BUTTON)
        self.waitLoading()
        datas = self.findElements(RL.ROLE_DATA_TR)
        if datas:
            try:
                for data in datas:
                    assert role_name in data.find_element(*RL.TR_TD_ROLE_NAME).text

                return 1 ## 查询结果正确
            except AssertionError as e:
                print(e)
                return 0 ## 查询结果断言错误
        else:
            return 2 ## 查询不到数据，无该数据

    def queryRoleByCode(self,role_code='',pathname='',snapshot_name=''):
        self.frameOutIn()
        self.findElement(RL.ROLE_TYPE_VALUE).clear()
        self.findElement(RL.ROLE_TYPE_VALUE).send_keys(role_code)
        self.waitElementClick(RL.SEARCH_BUTTON)
        self.waitLoading()
        datas = self.findElements(RL.ROLE_DATA_TR)
        if datas:
            try:
                for data in datas:
                    assert role_code in self.findElementFromEle(data,RL.TR_TD_ROLE_CODE).text

                return 1 ## 查询结果正确
            except AssertionError as e:
                print(e)
                return 0 ## 查询结果断言错误
        else:
            return 2 ## 查询不到数据，无该数据


    def modifyRole(self,snapshot_name='',pathname='',menu_list={}):       ## menu_list = {'权限系统':[],'贷后系统':[]}
        self.frameOutIn()
        self.waitElementClick(RL.ROLE_EDIT)
        self.waitLoading()
        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>编辑角色</title>')
        if menu_list:
            for key,values in menu_list.items():
                self.waitElementClick((RL.MENU_LIST_A[0], RL.MENU_LIST_A[1] % key))
                for value in values:
                    divs = self.waitAllElementPresent(RL.MENU_LIST_DIV)
                    for div in divs:
                        span = self.findElementFromEle(div,RL.ROLE_USER_SPAN)
                        if span.text == value:
                            self.driver.execute_script('arguments[0].click()',span)
                            break

        self.switchToParentFrame()
        self.waitElementClick(RL.SAVE_SUBMIT)
        self.switchToOuterFrame()
        self.waitStringinPagesource('角色修改成功！')
        self.saveScreenshot(pathname+snapshot_name)
        return self.waitStringNotinPagesource('角色修改成功！')




    def manageRoleUser(self,check_text='',delete_user='',pathname='',snapshot_name=''):
        self.frameOutIn()
        self.waitElementClick(RL.ROLE_USER_MANAGE)
        self.waitLoading()
        self.switchToInnerFrame()
        self.waitStringinPagesource('<title>管理角色用户</title>')
        if check_text:
            if self.waitStringinPagesource(check_text):
                self.saveScreenshot(pathname+snapshot_name+check_text)
                self.switchToParentFrame()
                self.waitElementClick(RL.CANCEL_BITTON_USER)

        if delete_user:
            users = self.findElements(RL.ROLE_USER_SPAN)
            for user in users:
                if delete_user in user.text:
                    user.click()
            self.switchToParentFrame()
            self.waitElementClick(RL.DELETE_BITTON_USER)
            self.switchToOuterFrame()
            self.waitStringinPagesource('删除成功')
            self.saveScreenshot(pathname+snapshot_name+'删除成功')
            self.waitStringNotinPagesource('删除成功')


    def deleteRole(self,pathname='',snapshot_name=''):
        self.frameOutIn()
        self.waitElementClick(RL.ROLE_DELETE)
        self.waitStringinPagesource('确定要删除？')
        self.saveScreenshot(pathname+snapshot_name+'确定要删除？')
        self.waitElementClick(RL.DELETE_CONFIRM)
        self.switchToOuterFrame()
        self.waitStringinPagesource('角色删除成功！')
        self.saveScreenshot(pathname+snapshot_name+'角色删除成功！')
        self.waitStringNotinPagesource('角色删除成功！')


    def refreshData(self):
        self.frameOutIn()
        self.waitElementClick(RL.REFRESH_BUTTON)


