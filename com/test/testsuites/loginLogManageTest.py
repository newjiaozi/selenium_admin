import unittest
from com.test.testsuites.baseTestCase import BaseTestCase
from selenium import webdriver
from com.test.pageOperation.loginPage import Login
from com.test.pageOperation.loginLogManage import LoginLogManagePage as LLMP

class LoginLogManageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(cls.URL)
        cls.driver.implicitly_wait(10)
        cls.LLMP = LLMP(cls.driver)
        Login(cls.driver).login('liudonglin', '1988@ooOO')

    def test_01_isRightPage(self):
        self.assertTrue(self.LLMP.is_right_page())

    def test_02_searchNameHaveData(self):
        self.assertEqual(self.LLMP.searchByName("liudonglin"),1)

    def test_03_searchNameHaveNotData(self):
        self.assertEqual(self.LLMP.searchByName("大队胜多负少"),2)

    def test_04_searchMailHaveData(self):
        self.assertEqual(self.LLMP.searchByMail("liudonglin@maizijf.com"),1)

    def test_05_searchMailHaveNotData(self):
        self.assertEqual(self.LLMP.searchByMail("liudonglin@11.com"),2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()