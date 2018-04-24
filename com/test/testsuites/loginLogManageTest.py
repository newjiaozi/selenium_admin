import sys
from com.test.testsuites.baseTestCase import BaseTestCase


class LoginLogManageTest(BaseTestCase):
    case_name = '登录日志管理'
    # firefox = True

    def test_01_isRightPage(self):
        self.assertTrue(self.LLMP.is_right_page())

    def test_02_searchNameHaveData(self):
        self.assertEqual(self.LLMP.searchByName("liudonglin",snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name),1)

    def test_03_searchNameHaveNotData(self):
        self.assertEqual(self.LLMP.searchByName("大队胜多负少",snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name),2)

    def test_04_searchMailHaveData(self):
        self.assertEqual(self.LLMP.searchByMail("liudonglin@maizijf.com",snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name),1)

    def test_05_searchMailHaveNotData(self):
        self.assertEqual(self.LLMP.searchByMail("liudonglin@11.com",snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name),2)


if __name__ == "__main__":
    LoginLogManageTest.action('登录日志管理',LoginLogManageTest)

