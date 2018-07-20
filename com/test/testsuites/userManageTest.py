from com.test.testsuites.baseTestCase import BaseTestCase
import sys

class UserManageTest(BaseTestCase):
    case_name = '用户管理'
    # firefox = True

    def test_01_isRightPage(self):
        self.assertTrue(self.UMP.is_right_page())

    def test_02_SearchByNameHaveData(self):
        self.assertEqual(self.UMP.searchByName('刘东林'),1)

    def test_03_SearchByLoginNameHaveData(self):
        self.assertEqual(self.UMP.searchByLoginName('liudonglin@maizijf.com'),1)

    def test_04_SearchByNameHaveNotData(self):
        self.assertEqual(self.UMP.searchByName('刘东林0000'),2)

    def test_05_SearchByLoginNameHaveNotData(self):
        self.assertEqual(self.UMP.searchByLoginName('liudonglin1@maizijf.com'),2)

    def test_06_AddUserNameBlank(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(alert='必填项不能为空',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_07_AddUserLoginNameBlank(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',alert='必填项不能为空',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_08_AddUserPasswdBlank(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',alert='必填项不能为空',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_09_AddUserRepasswdBlank(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',alert='必填项不能为空',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_10_AddUserMailBlank(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',alert='必填项不能为空',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_11_AddUserMobileBlank(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',alert='必填项不能为空',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_12_AddUserApartBlank(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='13612341234',alert='必填项不能为空',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_13_AddUserName2Short(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',alert='姓名长度2-20',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_14_AddUserName2Long(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅'*21,loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',long_size={"name":20},close=False,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_15_AddUserLoginName2Short(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guoba',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',alert='登录名长度6-20',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_16_AddUserLoginName2Long(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='g'*21,passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',long_size={"loginname":20},close=False,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_17_AddUserPasswd2Short(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guoba',repasswd='guoba',mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',alert='密码必须6到10位字母或数字或字母数字组合！',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))


    def test_18_AddUserPasswd2Long(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='g'*21,repasswd='g'*21,mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',alert='密码必须6到10位字母或数字或字母数字组合！',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))


    def test_19_AddUserMailInvalid(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorougbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',alert='邮箱格式不正确',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))


    def test_20_AddUserMobileInvalid(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='1361234123',apartment='麦子金服-麦子金服',alert='请输入正确的手机号',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_21_AddUserMobile2Long(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='136123412345',apartment='麦子金服-麦子金服',long_size={'mobile':11},close=False,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_22_AddUserMail2Long(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorouguobaorouguobaorouguobaorouguobaor@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',long_size={'mail':50},close=False,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_23_AddUserPasswdDiff(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaoroo',mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',alert='两次密码不一致，请确认后重新输入！',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_24_AddUserSuccess(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',alert='添加用户成功',close=False,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_25_AddUserLoginNameExist(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',alert='登录名重复',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    def test_26_AddUserMailExist(self):
        self.UMP.refreshData()
        self.assertTrue(self.UMP.addUser(name='锅包肉',loginname='guobaorou1',passwd='guobaorou',repasswd='guobaorou',mail='guobaorou@gbr.com',mobile='13612341234',apartment='麦子金服-麦子金服',alert='用户邮箱重复',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    # 修改权限
    def test_40_PMModify(self):
        self.UMP.refreshData()
        if self.UMP.searchByLoginName('guobaorou') == 1:
            self.assertTrue(self.UMP.permissionManage(['超级管理员角色','催收员'],snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    ## 修改登录禁止状态
    def test_51_LoginState2Deny(self):
        self.UMP.refreshData()
        if self.UMP.searchByLoginName('guobaorou') == 1:
            self.assertTrue(self.UMP.changeLoginStatus('0',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))
            self.assertTrue(self.UMP.checkStatus('禁止登录',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))
            # self.UMP.getNewWindowLogin(BaseTestCase.URL_LOGIN,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)

    def test_52_LoginState2Allow(self):
        self.UMP.refreshData()
        if self.UMP.searchByLoginName('guobaorou') == 1:
            self.assertTrue(self.UMP.changeLoginStatus('1',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))
            self.assertTrue(self.UMP.checkStatus('可登录',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))

    ## 删除用户

    def test_61_DeleteUser(self):
        self.UMP.refreshData()
        if self.UMP.searchByLoginName('guobaorou') == 1:
            self.assertTrue(self.UMP.deleteUserAll(snapshot_name=self.__class__.__name__+sys._getframe().f_code.co_name))
        self.assertEqual(self.UMP.searchByLoginName('guobaorou'),2)

if __name__ == "__main__":
    UserManageTest.action('用户管理',UserManageTest)
