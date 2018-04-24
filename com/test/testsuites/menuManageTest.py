from com.test.testsuites.baseTestCase import BaseTestCase
import sys


class MenuManageTest(BaseTestCase):
    case_name = '菜单管理'
    # firefox = True


    def test_01_isRightPage(self):
        self.assertTrue(self.MMP.is_right_page())


    def test_02_addSystem(self):
        self.MMP.refreshToMenuManage()
        self.assertTrue(self.MMP.addSystem(name='测试--系统',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name))

    def test_03_addSystemNameBlank(self):
        self.MMP.refreshToMenuManage()

        self.assertTrue(self.MMP.addSystem(alert='必填项不能为空',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name))

    def test_06_addMenu(self):
        self.MMP.refreshToMenuManage()
        self.MMP.addMenu(system_name='测试--系统',name='测试--菜单',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_07_addMenuNameBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.addMenu(alert='必填项不能为空',system_name='测试--系统',name='',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)


    def test_12_addPage(self):
        self.MMP.refreshToMenuManage()
        self.MMP.addPage(system_name='测试--系统',menu_name='测试--菜单',name='测试--页面',target='http://www.baidu.com',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_13_addPageNameBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.addPage(alert='必填项不能为空',system_name='测试--系统',menu_name='测试--菜单',name='',target='http://www.baidu.com',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_14_addPageTargetBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.addPage(alert='必填项不能为空',system_name='测试--系统',menu_name='测试--菜单',name='测试--页面',target='',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_18_addInterface(self):
        self.MMP.refreshToMenuManage()
        self.MMP.addInterface(system_name='测试--系统',menu_name='测试--菜单',page_name='测试--页面',name='测试--接口',target='http://www.baidu.com',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_19_addInterfaceNameBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.addInterface(alert='必填项不能为空',system_name='测试--系统',menu_name='测试--菜单',page_name='测试--页面',name='',target='http://www.baidu.com',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_20_addInterfaceTargetBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.addInterface(alert='必填项不能为空',system_name='测试--系统',menu_name='测试--菜单',page_name='测试--页面',name='测试--接口',target='',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_30_modifySystem(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifySystem(system_name='测试--系统',name='测试--系统--修改',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_31_modifySystemNameBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifySystem(alert='必填项不能为空',system_name='测试--系统--修改',name='',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_32_modifySystemDeleteAddApart(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifySystem(system_name='测试--系统--修改',name='测试--系统--修改',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_33_modifySystemDeleteApart(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifySystem(system_name='测试--系统--修改',name='测试--系统--修改',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_35_modifyMenu(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifyMenu(system_name='测试--系统--修改',menu_name='测试--菜单',name='测试--菜单--修改',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_36_modifyMenuNameBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifyMenu(alert='必填项不能为空',system_name='测试--系统--修改',menu_name='测试--菜单--修改',name='',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_40_modifyPage(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifyPage(system_name='测试--系统--修改',menu_name='测试--菜单--修改',page_name='测试--页面',name='测试--页面--修改',target='http://www.baidu.com',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_41_modifyPageNameBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifyPage(alert='必填项不能为空',system_name='测试--系统--修改',menu_name='测试--菜单--修改',page_name='测试--页面--修改',name='',target='http://www.baidu.com',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_42_modifyPageTargetBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifyPage(alert='必填项不能为空',system_name='测试--系统--修改',menu_name='测试--菜单--修改',page_name='测试--页面--修改',name='测试--页面--修改',target='',remark='备注',apartment='麦子金服-麦子金服',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_45_modifyInterface(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifyInterface(system_name='测试--系统--修改',menu_name='测试--菜单--修改',page_name='测试--页面--修改',interface_name='测试--接口',name='测试--接口--修改',target='http://www.baidu.com',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_46_modifyInterfaceNameBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifyInterface(alert='必填项不能为空',system_name='测试--系统--修改',menu_name='测试--菜单--修改',page_name='测试--页面--修改',interface_name='测试--接口--修改',name='',target='http://www.baidu.com',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_47_modifyInterfaceTargetBlank(self):
        self.MMP.refreshToMenuManage()
        self.MMP.modifyInterface(alert='必填项不能为空',system_name='测试--系统--修改',menu_name='测试--菜单--修改',page_name='测试--页面--修改',interface_name='测试--接口--修改',name='测试--接口--修改',target='',remark='备注',apartment='',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_50_deleteInterface(self):
        self.MMP.refreshToMenuManage()
        self.MMP.deleteInterface(system_name='测试--系统--修改',menu_name='测试--菜单--修改',page_name='测试--页面--修改',interface_name='测试--接口--修改',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_51_deletePage(self):
        self.MMP.refreshToMenuManage()
        self.MMP.deletePage(system_name='测试--系统--修改',menu_name='测试--菜单--修改',page_name='测试--页面--修改',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_52_deleteMenu(self):
        self.MMP.refreshToMenuManage()
        self.MMP.deleteMenu(system_name='测试--系统--修改',menu_name='测试--菜单--修改',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

    def test_53_deleteSystem(self):
        self.MMP.refreshToMenuManage()
        self.MMP.deleteSystem(system_name='测试--系统--修改',snapshot_name=self.__class__.__name__ + sys._getframe().f_code.co_name)

if __name__ == "__main__":
    MenuManageTest.action('菜单管理',MenuManageTest)
