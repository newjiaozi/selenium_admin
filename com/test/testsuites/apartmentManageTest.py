from com.test.testsuites.baseTestCase import BaseTestCase
import sys


class ApartmentManageTest(BaseTestCase):

    nameTen = "一二三四五六七八九十"
    apartmentName = "oo自动创建部门oo"
    innerName = "-公司内部部门-"
    outerName = "-公司外部部门-"
    modifyName = "测试修改"
    case_name = '部门管理'

    def test_01_defaultDisaplay(self):
        self.assertTrue(self.AMP.is_right_page())

    def test_02_close_page_x(self):
        self.assertTrue(self.AMP.openTopAddPage(operation=1,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_03_close_page_cancle(self):
        self.assertTrue(self.AMP.openTopAddPage(operation=2,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_04input_blank(self):
        result1 = self.AMP.openTopAddPage(operation=3,alert_window=1,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(result1)
        result2 = self.AMP.openTopAddPage(operation=3,apart_name=self.apartmentName,alert_window=1,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(result2)

    def test_05input_maxsize(self):
        result = self.AMP.openTopAddPage(apart_name=self.apartmentName*10,apart_chairman=self.nameTen*10,apart_comment=self.nameTen*50,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(result)
        self.assertFalse(self.AMP.ifApartmentNameInPage(self.apartmentName*10,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_06create_inner_apart(self):
        result = self.AMP.openTopAddPage(apart_name=self.innerName,apart_comment=self.nameTen*2,apart_type=0,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(result)
        self.assertTrue(self.AMP.ifApartmentNameInPage(self.innerName,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_07create_outer_apart(self):
        result = self.AMP.openTopAddPage(apart_name=self.outerName,apart_comment=self.nameTen*2,apart_type=1,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(result)
        self.assertTrue(self.AMP.ifApartmentNameInPage(self.outerName,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_08create_lowwer_apart(self):
        result = self.AMP.openTopAddPage(apart_name=self.innerName*2,apart_comment=self.nameTen*2,apart_type=1,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(result)
        self.AMP.addTestData(self.innerName*2,toName=self.innerName*2,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)

    def test_20modify_Apartment(self):
        result = self.AMP.openTopAddPage(apart_name=self.modifyName,apart_comment=self.modifyName*2,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(result)
        self.AMP.modifyApartment(apart_name=self.modifyName,to_parent_name=self.modifyName*2,toParentApart='-公司外部部门--一二三四五六七八九十一二三四五六七八九十',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(self.AMP.ifModifySucceed(apart_name=self.modifyName*2,toParentApart='-公司外部部门--一二三四五六七八九十一二三四五六七八九十',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_30_ApplyRoleADD(self):
        self.AMP.applyRole(apartment_name=self.outerName,role_list=['刘东林-测试','刘东林-贷后角色'],snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)

    def test_31_ApplyRoleDel(self):
        self.AMP.applyRole(apartment_name=self.outerName,role_list=[],snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)

    def test_40_checkUserHaveNotUser(self):
        self.AMP.checkApplyUser(apartment_name=self.outerName,user_list=[],addUser=False,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)

    def test_41_checkUserAdd(self):
        self.AMP.checkApplyUser(apartment_name=self.outerName,user_list=['liudonglin@maizijf.com'],addUser=True,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)

    def test_42_checkUserDel(self):
        self.AMP.checkApplyUser(apartment_name=self.outerName,user_list=['liudonglin@maizijf.com'],addUser=False,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)

    def test_50_DeleteApart(self):
        self.AMP.deleteEveryOne([self.apartmentName,self.innerName,self.apartmentName*5,self.outerName,self.innerName*2,self.modifyName,self.modifyName*2],snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)


if __name__ == "__main__":
    ApartmentManageTest.action('部门管理',ApartmentManageTest)

