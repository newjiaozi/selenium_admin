import unittest
from selenium import webdriver
from com.test.pageOperation.loginPage import Login
from com.test.pageOperation.apartmentManage import ApartmentManagePage as AMP
from com.test.pageOperation.loginLogManage import LoginLogManagePage as LLMP
from com.test.pageOperation.logManage import LogManagePage as LMP
from com.test.pageOperation.menuManage import MenuManagePage as MMP
from com.test.pageOperation.roleManage import RoleManagePage as RMP
from com.test.pageOperation.userManage import UserManagePage as UMP
import HTMLTestRunner



class BaseTestCase(unittest.TestCase):


    URL = "http://admin.sit.nonobank.com/admin-web/index"
    URL_LOGIN = "http://admin.sit.nonobank.com/admin-web/login"
    command_executor = ''
    chrome = False
    firefox = False

    @classmethod
    def setUpClass(cls):

        if cls.chrome == True:
            options = webdriver.ChromeOptions()
            options.add_argument("start-fullscreen")
            options.add_argument('disable-infobars')
            cls.driver = webdriver.Chrome(options=options)
        elif cls.firefox == True:
            cls.driver = webdriver.Firefox()
            cls.driver.set_window_position(3000,2000)
            cls.driver.maximize_window()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("start-fullscreen")
            options.add_argument('disable-infobars')
            cls.driver = webdriver.Chrome(options=options)

        cls.driver.get(cls.URL)
        cls.driver.implicitly_wait(10)
        cls.LOGIN = Login(cls.driver)
        cls.AMP = AMP(cls.driver)
        cls.LLMP = LLMP(cls.driver)
        cls.LMP = LMP(cls.driver)
        cls.MMP = MMP(cls.driver)
        cls.RMP = RMP(cls.driver)
        cls.UMP = UMP(cls.driver)
        cls.LOGIN.login('liudonglin','1988@ooOO')


    @classmethod
    def action(cls,result_name,testcase):
        print(testcase.__name__,'Start...')
        if isinstance(testcase,type(BaseTestCase)):
            suite = unittest.TestLoader().loadTestsFromTestCase(testcase)  ##
            with open('/Users/liudonglin/PycharmProjects/selenium_admin/com/test/report/%s-测试报告.html' % result_name,'wb') as f:
                runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='测试报告 详细信息')
                runner.run(suite)
                print(testcase.__name__,'End...',)
        else:
            print('*****************')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

