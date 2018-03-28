from .basePage import BasePage
from ..locator.roleLocator import RoleLocator as RL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class RoleManagePage(BasePage):
    def is_right_page(self):
        assert "麦子金服管理后台" == self.driver.title
        self.getInQXXT()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(RL.ROLE_MANAGE_BUTTON)).click()
        self.driver.switch_to.frame(RL.IFRAME)
        try:
            WebDriverWait(self.driver,10).until(lambda x:"<title>角色列表</title>" in x.page_source)
            self.driver.switch_to.default_content()
            return True
        except Exception as e:
            print(e)
            return False

    def addRole(self,role_name='',role_code='',role_apart='',snapshot_name='',pathname='',menu_list={}):     ## menu_list = {'权限系统':[],'贷后系统':[]}
        self.switchToOuterFrame()
        self.switchToIfame()

        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(RL.ADD_ROLE_BUTTON)).click()
        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x : '<title>添加角色</title>' in x.page_source)
        self.driver.find_element(*RL.ADD_ROLE_NAME).clear()
        self.driver.find_element(*RL.ADD_ROLE_NAME).send_keys(role_name)   ## role  name
        self.driver.find_element(*RL.ADD_ROLE_TYPE_VALUE).clear()
        self.driver.find_element(*RL.ADD_ROLE_TYPE_VALUE).send_keys(role_code) ## role  code
        aos = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(RL.APART_OPTIONS))

        self.driver.find_element(*RL.ADD_ROLE_APART_INPUT).click()
        for ao in aos:
            if role_apart == ao.text:
                ao.click()
        if menu_list:
            for key,values in menu_list.items():
                self.driver.find_element(RL.MENU_LIST_A[0], RL.MENU_LIST_A[1] % key).click()
                for value in values:
                    divs = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(RL.MENU_LIST_DIV))
                    for div in divs:
                        span = div.find_element(*RL.ROLE_USER_SPAN)
                        if span.text == value:
                            # print(span.text,'###')
                            self.driver.execute_script('arguments[0].click()',span)
                            # span.click()
                            break

        self.switchToParentFrame()
        self.driver.find_element(*RL.SAVE_SUBMIT).click()
        self.switchToOuterFrame()
        WebDriverWait(self.driver,20).until(lambda x:'角色添加成功！' in x.page_source)
        self.saveScreenshot(pathname+snapshot_name)
        WebDriverWait(self.driver,20).until(lambda x:'角色添加成功！' not in x.page_source)

        return True



    def queryRoleByName(self,role_name='',pathname='',snapshot_name=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        self.driver.find_element(*RL.ROLE_NAME).clear()
        self.driver.find_element(*RL.ROLE_NAME).send_keys(role_name)
        WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(RL.LOADING))
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(RL.SEARCH_BUTTON)).click()
        WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(RL.LOADING))
        datas = self.driver.find_elements(*RL.ROLE_DATA_TR)
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
        self.switchToOuterFrame()
        self.switchToIfame()
        self.driver.find_element(*RL.ROLE_TYPE_VALUE).clear()
        self.driver.find_element(*RL.ROLE_TYPE_VALUE).send_keys(role_code)
        WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(RL.LOADING))
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(RL.SEARCH_BUTTON)).click()
        WebDriverWait(self.driver,20).until_not(EC.presence_of_element_located(RL.LOADING))
        datas = self.driver.find_elements(*RL.ROLE_DATA_TR)
        if datas:
            try:
                for data in datas:
                    assert role_code in data.find_element(*RL.TR_TD_ROLE_CODE).text

                return 1 ## 查询结果正确
            except AssertionError as e:
                print(e)
                return 0 ## 查询结果断言错误
        else:
            return 2 ## 查询不到数据，无该数据


    def modifyRole(self,snapshot_name='',pathname='',menu_list={}):       ## menu_list = {'权限系统':[],'贷后系统':[]}
        self.switchToOuterFrame()
        self.switchToIfame()
        # WebDriverWait(self.driver,20).until(EC.presence_of_element_located(RL.ROLE_DATA_TR))
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(RL.ROLE_EDIT)).click()
        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x: '' in x.page_source)
        if menu_list:
            for key,values in menu_list.items():
                self.driver.find_element(RL.MENU_LIST_A[0], RL.MENU_LIST_A[1] % key).click()
                for value in values:
                    divs = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(RL.MENU_LIST_DIV))
                    for div in divs:
                        span = div.find_element(*RL.ROLE_USER_SPAN)
                        if span.text == value:
                            # print(span.text,'###')
                            self.driver.execute_script('arguments[0].click()',span)
                            # span.click()
                            break

        self.switchToParentFrame()
        self.driver.find_element(*RL.SAVE_SUBMIT).click()
        self.switchToOuterFrame()
        WebDriverWait(self.driver,20).until(lambda x:'角色修改成功！' in x.page_source)
        self.saveScreenshot(pathname+snapshot_name)
        WebDriverWait(self.driver, 20).until(lambda x: '角色修改成功！' not in x.page_source)
        return True



    def manageRoleUser(self,check_text='',delete_user='',pathname='',snapshot_name=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(RL.ROLE_USER_MANAGE)).click()
        self.switchToInnerFrame()
        WebDriverWait(self.driver,20).until(lambda x : '<title>管理角色用户</title>' in x.page_source)
        if check_text:
            assert check_text in self.driver.page_source
            self.saveScreenshot(pathname+snapshot_name+check_text)
            self.switchToParentFrame()
            self.driver.find_element(*RL.CANCEL_BITTON_USER).click()

        if delete_user:
            users = self.driver.find_elements(*RL.ROLE_USER_SPAN)
            for user in users:
                if delete_user in user.text:
                    user.click()
            self.switchToParentFrame()
            self.driver.find_element(*RL.DELETE_BITTON_USER).click()
            self.switchToOuterFrame()
            WebDriverWait(self.driver,20).until(lambda x: '删除成功' in x.page_source)
            self.saveScreenshot(pathname+snapshot_name+'删除成功')


    def deleteRole(self,pathname='',snapshot_name=''):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(RL.ROLE_DELETE)).click()

        WebDriverWait(self.driver,20).until(lambda x:'确定要删除？' in x.page_source)
        self.saveScreenshot(pathname+snapshot_name+'确定要删除？')
        self.driver.find_element(*RL.DELETE_CONFIRM).click()
        self.switchToOuterFrame()
        WebDriverWait(self.driver,20).until(lambda x:'角色删除成功！' in x.page_source)
        self.saveScreenshot(pathname+snapshot_name+'角色删除成功！')


    def refreshData(self):
        self.switchToOuterFrame()
        self.switchToIfame()
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(RL.REFRESH_BUTTON)).click()


