import sys
from com.test.testsuites.baseTestCase import BaseTestCase

class ProcedureTest(BaseTestCase):
    case_name = '流程测试'


    def test01_Pro1(self): ## 新建用户，部门，给部门分配权限，权限控制成功；
        ## 登录账户
        ## 1.创建一个机构三级机构，A业务-A部门-A组
        self.AMP.is_right_page()
        self.AMP.openTopAddPage(apart_name='A业务子公司',apart_comment='A业务子公司',apart_type=1,snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.AMP.addTestData(apart_name='A业务子公司',toName='A部门',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        self.AMP.addTestData(apart_name='A部门',toName='A小组',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        ## 2.创建一个用户A，分给A组
        self.UMP.is_right_page()
        self.UMP.addUser(name='测试用户A',loginname='testuser',passwd='testuser',repasswd='testuser',mail='testuser@test.com',mobile='13683581996',apartment='A小组-A小组',alert='添加用户成功',close=False,snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        ## 3.创建一个角色A，贷后的角色，角色分配给A组，没有内催列表导出权限
        self.RMP.is_right_page()
        self.RMP.addRole(role_name='测试角色A',role_code='testcode',role_apart='A小组-A小组',pathname=self.__class__.__name__,snapshot_name = sys._getframe().f_code.co_name,menu_list={'贷后系统':['内催列表','导出']})
        ## 退出登录，登录新建用户
        self.LOGIN.logout(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        self.LOGIN.loginOutside('testuser','testuser')
        ## 4.贷后内催列表，导出，权限控制成功
        self.UMP.getInNCLB(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        self.LOGIN.logout(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test02_Pro2(self): ## 密码错误五次，禁止登录，修改后登录成功；
        ## 登出用户
        for i in range(5):
            self.LOGIN.loginOutside('testuser','testuser1',alert='密码错误',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name+str(i))

        self.LOGIN.loginOutside('testuser', 'testuser1', alert='登录失败次数过多，请联系管理员',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        self.LOGIN.login('liudonglin', '1988@ooOO')
        self.UMP.is_right_page()
        if self.UMP.searchByLoginName('testuser') == 1:
            self.assertTrue(self.UMP.changeLoginStatus('1',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))
            self.assertTrue(self.UMP.checkStatus('可登录',snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name))
        self.LOGIN.logout(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        self.LOGIN.loginOutside('testuser','testuser',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        self.LOGIN.logout(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)




    def test03_Pro3(self):
        ## 进入小组，移除用户
        self.LOGIN.login('liudonglin','1988@ooOO')
        self.AMP.is_right_page()
        self.AMP.checkApplyUser(apartment_name='A小组',user_list=['testuser@test.com'],addUser=False,snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        ## 退出登录，登录新建用户
        self.LOGIN.logout(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        self.LOGIN.loginOutside('testuser','testuser')
        ## 提示
        self.AMP.haveNotPermission(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test04_Pro4(self):
        ## 进入小组，移除用户
        self.LOGIN.login('liudonglin', '1988@ooOO')
        self.AMP.is_right_page()
        self.AMP.checkApplyUser(apartment_name='A小组',user_list=['testuser'],addUser=True,snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        self.AMP.applyRole(apartment_name='A小组',role_list=[],snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        ## 退出登录，登录新建用户
        self.LOGIN.logout(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)
        self.LOGIN.loginOutside('testuser','testuser')
        ## 提示
        self.AMP.haveNotPermission(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test20_deleteTestData(self):
        self.LOGIN.login('liudonglin', '1988@ooOO')
        self.AMP.is_right_page()
        self.AMP.deleteEveryOne(['A业务子公司'],snapshot_name = self.__class__.__name__+sys._getframe().f_code.co_name)
        self.RMP.is_right_page()
        self.assertEqual(self.RMP.queryRoleByCode(role_code='testcode',snapshot_name=sys._getframe().f_code.co_name),1)
        self.RMP.deleteRole(snapshot_name=sys._getframe().f_code.co_name,pathname=self.__class__.__name__)
        self.UMP.is_right_page()
        self.assertEqual(self.UMP.searchByLoginName('testuser'),1)
        self.UMP.deleteUserAll(snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

if __name__ == "__main__":
    ProcedureTest.action('流程测试',ProcedureTest)