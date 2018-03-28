import unittest
from com.test.testsuites.apartmentManageTest import ApartmentManageTest
from com.test.testsuites.loginLogManageTest import LoginLogManageTest
from com.test.testsuites.logManageTest import LogManageTest
from com.test.testsuites.menuManageTest import MenuManageTest
from com.test.testsuites.roleManageTest import RoleManageTest
from com.test.testsuites.userManageTest import UserManageTest
import datetime

import HTMLTestRunner

def action():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(ApartmentManageTest)  ##部门管理测试
    suite2 = unittest.TestLoader().loadTestsFromTestCase(LoginLogManageTest)   ##登录日志管理测试
    suite3 = unittest.TestLoader().loadTestsFromTestCase(LogManageTest)    ##日志管理测试

    suite4 = unittest.TestLoader().loadTestsFromTestCase(MenuManageTest)   ## 菜单管理测试

    suite5 = unittest.TestLoader().loadTestsFromTestCase(RoleManageTest)  ##角色管理测试

    suite6 = unittest.TestLoader().loadTestsFromTestCase(UserManageTest)   ##用户管理测试



    suite = unittest.TestSuite([
        suite1,
        suite2,
        suite3,
        suite4,
        suite5,
        suite6,
    ])

    date_now = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d-%H:%M:%S')
    with open('测试报告%s.html' % date_now,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='测试报告详细信息')
        runner.run(suite)

if __name__ == "__main__":
    action()