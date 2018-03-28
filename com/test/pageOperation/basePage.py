from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locator.mainLocator import MainPageLocator as MPL
import time

class BasePage():
    def __init__(self,driver):
        self.driver = driver



    def getInQXXT(self):
        self.pause4Seconds()
        ele_ul = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(MPL.SYSTEM_UL))
        ele_div = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(MPL.SYSTEM_DIV))
        ele_ul_old_class = ele_ul.get_attribute("class")
        ele_div_old_class = ele_div.get_attribute("class")
        ele_ul_new_class = ele_ul_old_class + " all"
        ele_div_new_class = ele_div_old_class + " all"
        self.driver.execute_script('arguments[0].className = arguments[1]',ele_ul,ele_ul_new_class)
        self.driver.execute_script('arguments[0].className = arguments[1]',ele_div,ele_div_new_class)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(MPL.QXXT_SYSTEM)).click()
        self.driver.execute_script('arguments[0].className = arguments[1]',ele_ul,ele_ul_old_class)
        self.driver.execute_script('arguments[0].className = arguments[1]',ele_div,ele_div_old_class)
        self.pause4Seconds()

    def pause4Seconds(self):
        time.sleep(2)

    def switchToIfame(self):
        self.driver.switch_to.frame('jumpIframe')

    def switchToOuterFrame(self):
        self.driver.switch_to.default_content()

    def switchToParentFrame(self):
        self.driver.switch_to.parent_frame()

    def switchToInnerFrame(self):
        self.driver.switch_to.frame('layui-layer-iframe1')

    def wait4ElementClick(self,locate):
        try:
            return WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(locate))
        except Exception as e:
            print(e)
            return False

    def wait4ElementPresent(self,locate):
        try:
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located(locate)).click()
            return True
        except Exception as e:
            print(e)
            return False

    def wait4ElementClick(self,locate):
        try:
            return WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(locate))
        except Exception as e:
            print(e)
            return False

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