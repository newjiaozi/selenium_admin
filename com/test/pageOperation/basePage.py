from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from ..locator.mainLocator import MainPageLocator as MPL
import time




class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def getInQXXT(self):
        # self.pause4Seconds()
        # ele_ul = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(MPL.SYSTEM_UL))
        # ele_div = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(MPL.SYSTEM_DIV))
        # ele_ul_old_class = ele_ul.get_attribute("class")
        # ele_div_old_class = ele_div.get_attribute("class")
        # ele_ul_new_class = ele_ul_old_class + " all"
        # ele_div_new_class = ele_div_old_class + " all"
        # self.driver.execute_script('arguments[0].className = arguments[1]',ele_ul,ele_ul_new_class)
        # self.driver.execute_script('arguments[0].className = arguments[1]',ele_div,ele_div_new_class)
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(MPL.QXXT_SYSTEM)).click()
        # self.driver.execute_script('arguments[0].className = arguments[1]',ele_ul,ele_ul_old_class)
        # self.driver.execute_script('arguments[0].className = arguments[1]',ele_div,ele_div_old_class)
        # self.pause4Seconds()
        pass

    def pause4Seconds(self):
        time.sleep(4)

    def switchToIfame(self):
        try:
            return WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it('jumpIframe'),message='跳转到iframe< jumpIframe >失败')
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def switchToOuterFrame(self):
        time.sleep(2)
        self.driver.switch_to.default_content()

    def switchToParentFrame(self):
        time.sleep(2)
        self.driver.switch_to.parent_frame()

    def switchToInnerFrame(self):
        try:
            return WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it('layui-layer-iframe1'),message='跳转到iframe< layui-layer-iframe1 >失败')
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def waitElementVisibility(self,locate):
        try:
            return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locate),message='等待元素visibility失败')
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def waitElementPresent(self,locate):
        try:
            return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locate),message='等待元素presence失败')
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def waitAllElementPresent(self,locate):
        try:
            return WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(locate),message='等待元素所有元素presence失败')
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def waitElementClick(self,locate):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locate),message='等待元素click失败').click()
            return True
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def waitElementClickEle(self,locate):
        try:
            return WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locate),message='等待元素click失败')
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def waitStringinPagesource(self,str):
        try:
            return WebDriverWait(self.driver,10).until(lambda x:str in x.page_source,message='等待<%s>出现在pagesource失败' % str)
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def waitStringNotinPagesource(self,str):
        try:
            return WebDriverWait(self.driver,10).until(lambda x:str not in x.page_source,message='等待<%s>消失在pagesource失败' % str)
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def waitLoading(self):
        try:
            WebDriverWait(self.driver,60).until_not(EC.presence_of_element_located(MPL.LOADING),message='等待laoding消失失败') ## 等待
            return True
        except TimeoutException as e:
            print(e.msg,e.stacktrace)
            return False

    def findElement(self,locator):
        return self.driver.find_element(*locator)

    def findElementFromEle(self,ele,loactor):
        return ele.find_element(*loactor)

    def findElements(self,locator):
        return self.driver.find_elements(*locator)

    def findElementsFromEle(self,ele,loactor):
        return ele.find_elements(*loactor)

    def saveScreenshot(self,filename,printPng=True):
        self.driver.get_screenshot_as_file("/Users/liudonglin/PycharmProjects/selenium_admin/com/test/Screenshot/%s.png" %  filename)
        if printPng:
            print(
                r'''<img src="/selenium_admin/com/test/Screenshot/%(filename)s.png"  alt="%(filename)s"  title="%(filename)s" width="30" height="20"  onclick="window.open('/selenium_admin/com/test/Screenshot/%(filename)s.png')"/>%(filename)s''' %
                {'filename':filename})

    def printPng(self,filename):
        print(
            r'''<img src="/selenium_admin/com/test/Screenshot/%(filename)s.png"  alt="%(filename)s"  title="%(filename)s" width="30" height="20"  onclick="window.open('/selenium_admin/com/test/Screenshot/%(filename)s.png')"/>%(filename)s''' %
            {'filename': filename})

    def refreshPage(self):
        self.driver.refresh()
        self.switchToOuterFrame()

    def getInNCLB(self,snapshot_name=''): ##进入  内催列表  （贷后系统）
        # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(MPL.NCLB_A)).click()
        self.waitElementClick(MPL.NCLB_A)
        # WebDriverWait(self.driver,30).until_not(EC.presence_of_element_located(MPL.LOADING))
        self.waitLoading()
        self.switchToIfame()
        # WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located(MPL.NC_LIST))
        self.waitAllElementPresent(MPL.NC_LIST)
        cur_handle = self.driver.current_window_handle
        # WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(MPL.EXPORT_DATA)).click()
        self.waitElementClick(MPL.EXPORT_DATA)
        handles = self.driver.window_handles
        for handle in handles:
            if handle != cur_handle:
                self.driver.switch_to.window(handle)
                # WebDriverWait(self.driver,20).until(lambda x:'您没有权限访问该数据，请联系管理员为您分配相应权限！' in x.page_source)
                if self.waitStringinPagesource('您没有权限访问该数据，请联系管理员为您分配相应权限！'):
                    self.saveScreenshot(filename=snapshot_name+'您没有权限访问该数据')
                    self.driver.close()
                    break
        self.driver.switch_to.window(cur_handle)

    def haveNotPermission(self,snapshot_name=''):
        # WebDriverWait(self.driver,20).until(lambda x: '您没有任何权限，请联系管理员为您分配相应权限后重新登录!' in x.page_source)
        self.waitStringinPagesource('您没有任何权限，请联系管理员为您分配相应权限后重新登录!')
        self.saveScreenshot(snapshot_name+'您没有任何权限')
        # WebDriverWait(self.driver,20).until(lambda x: '您没有任何权限，请联系管理员为您分配相应权限后重新登录!' not in x.page_source)
        self.waitStringNotinPagesource('您没有任何权限，请联系管理员为您分配相应权限后重新登录!')

    def frameOutIn(self):
        self.switchToOuterFrame()
        self.switchToIfame()

    def is_right_page(self,lacate,title_data):
        # self.switchToOuterFrame()
        # self.waitElementPresent(MPL.LAYUI_LAYOUT_ADMIN)
        # self.getInQXXT()
        self.refreshPage()
        self.waitElementClick(lacate)
        self.waitLoading()
        self.switchToIfame()
        return self.waitStringinPagesource(title_data)