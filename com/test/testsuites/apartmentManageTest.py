import unittest
from selenium import webdriver
from com.test.pageOperation.apartmentManage import ApartmentManagePage as AMP
from com.test.pageOperation.loginPage import Login
from com.test.testsuites.baseTestCase import BaseTestCase
import sys


class ApartmentManageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(cls.URL)
        cls.driver.implicitly_wait(10)
        cls.nameTen = "一二三四五六七八九十"
        cls.apartmentName = "oo自动创建部门oo"
        cls.AMP = AMP(cls.driver)
        cls.innerName = "-公司内部部门-"
        cls.outerName = "-公司外部部门-"
        cls.modifyName = "测试修改"
        Login(cls.driver).login('liudonglin','1988@ooOO')

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
        result = self.AMP.openTopAddPage(apart_name=self.apartmentName*10,apart_chairman=self.nameTen*10,apart_comment=self.nameTen*50)
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
        self.AMP.addTestData(self.innerName*2,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)

    def test_20modify_Apartment(self):
        result =  self.AMP.openTopAddPage(apart_name=self.modifyName,apart_comment=self.modifyName,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(result)
        self.AMP.modifyApartment(apart_name=self.modifyName,to_parent_name=self.outerName,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(self.AMP.ifModifySucceed(apart_name=self.modifyName*2,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))


    def test_21modify_Apartment(self):

        self.AMP.modifyApartment(apart_name=self.modifyName,to_parent_name='',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.assertTrue(self.AMP.ifModifySucceed(apart_name=self.modifyName*2,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))


    def test_30_DeleteApart(self):
        self.AMP.deleteEveryOne([self.apartmentName,self.innerName,self.apartmentName*5,self.outerName,self.innerName*2,self.modifyName,self.modifyName*2])


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

