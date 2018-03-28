import unittest
from com.test.testsuites.baseTestCase import BaseTestCase
from selenium import webdriver
from com.test.pageOperation.loginPage import Login
from com.test.pageOperation.roleManage import RoleManagePage as RMP
import  sys


class RoleManageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(cls.URL)
        cls.driver.implicitly_wait(10)
        cls.RMP = RMP(cls.driver)
        Login(cls.driver).login('liudonglin', '1988@ooOO')

    def test_01_is_rightPage(self):
        self.assertTrue(self.RMP.is_right_page())



    def test_02_AddRole(self):
        self.RMP.refreshData()
        self.assertTrue(self.RMP.addRole(role_name='测试角色007',role_code='00762600',role_apart='麦子金服-麦子金服',pathname=self.__class__.__name__,snapshot_name = sys._getframe().f_code.co_name,menu_list={'贷后系统':['内催列表','导出']}))


    def test_30_SearchByRoleNameHaveData(self):
        self.RMP.refreshData()
        self.assertEqual(self.RMP.queryRoleByName(role_name='测试角色007',pathname=self.__class__.__name__,snapshot_name=sys._getframe().f_code.co_name),1)


    def test_31_SearchByRoleNameHaveNoData(self):
        self.RMP.refreshData()
        self.assertEqual(self.RMP.queryRoleByName(role_name='测试角色008',pathname=self.__class__.__name__,snapshot_name=sys._getframe().f_code.co_name),2)


    def test_32_SearchByRoleCodeHaveData(self):
        self.RMP.refreshData()
        self.assertEqual(self.RMP.queryRoleByCode(role_code='00762600',pathname=self.__class__.__name__,snapshot_name=sys._getframe().f_code.co_name),1)


    def test_33_SearchByRoleCodeHaveNoData(self):
        self.RMP.refreshData()
        self.assertEqual(self.RMP.queryRoleByCode(role_code='00762601',pathname=self.__class__.__name__,snapshot_name=sys._getframe().f_code.co_name),2)



    def test_40_ManageRoleUserNoUser(self):
        self.RMP.refreshData()
        self.RMP.manageRoleUser(check_text='此角色没有绑定用户！',pathname=self.__class__.__name__,snapshot_name=sys._getframe().f_code.co_name)


    # def test_41_ManageRoleUserHaveUser(self):
    #     self.RMP.refreshData()
    #     self.RMP.manageRoleUser(delete_user='锅包肉',pathname=self.__class__.__name__,snapshot_name=sys._getframe().f_code.co_name)


    def test_50_ModifyPermissionMenu(self):
        self.RMP.refreshData()
        self.RMP.modifyRole(pathname=self.__class__.__name__,snapshot_name=sys._getframe().f_code.co_name,menu_list={'贷后系统':['内催列表'],'权限系统':['系统设置']})


    # def test_51_ModifuPermissionApart(self):
    #     self.RMP.refreshData()


    def test_60_deleteRole(self):
        self.RMP.refreshData()
        self.assertEqual(self.RMP.queryRoleByCode(role_code='00762600',snapshot_name=sys._getframe().f_code.co_name),1)
        self.RMP.deleteRole(snapshot_name=sys._getframe().f_code.co_name,pathname=self.__class__.__name__)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()