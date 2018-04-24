import sys
from com.test.testsuites.baseTestCase import BaseTestCase

class LogManageTest(BaseTestCase):
    case_name = '日志管理'
    # firefox = True

    # command_executor = 'http://192.168.56.104:6666/wd/hub'

    def test_01_isRightPage(self):
        self.assertTrue(self.LMP.is_right_page())

    def test_02_searchByNameHavaData(self):
        self.assertEqual(self.LMP.searchByName('刘东林',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name),1)

    def test_03_searchByNameHavaNotData(self):
        self.assertEqual(self.LMP.searchByName('无人机',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name),2)

    def test_04_searchByUseridHavaData(self):
        self.assertEqual(self.LMP.searchByUserid('343',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name),1)

    def test_05_searchByUseridHavaNotData(self):
        self.assertEqual(self.LMP.searchByUserid('1222222222',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name),2)

if __name__ == "__main__":
    LogManageTest().action('日志管理',LogManageTest)