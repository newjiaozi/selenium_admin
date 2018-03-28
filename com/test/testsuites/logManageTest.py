import unittest
from com.test.testsuites.baseTestCase import BaseTestCase
from selenium import webdriver
from com.test.pageOperation.loginPage import Login
from com.test.pageOperation.logManage import LogManagePage as LMP

class LogManageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(cls.URL)
        cls.driver.implicitly_wait(10)
        cls.LMP = LMP(cls.driver)
        Login(cls.driver).login('liudonglin', '1988@ooOO')

    def test_01_isRightPage(self):
        self.assertTrue(self.LMP.is_right_page())

    def test_02_searchByNameHavaData(self):
        self.assertEqual(self.LMP.searchByName('刘东林'),1)

    def test_03_searchByNameHavaNotData(self):
        self.assertEqual(self.LMP.searchByName('无人机'),2)

    def test_04_searchByUseridHavaData(self):
        self.assertEqual(self.LMP.searchByUserid('343'),1)

    def test_05_searchByUseridHavaNotData(self):
        self.assertEqual(self.LMP.searchByUserid('1222222222'),2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()