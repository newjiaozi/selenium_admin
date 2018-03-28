from selenium.webdriver.common.by import By
from .mainLocator import MainPageLocator

class ApartmentLocator(MainPageLocator):

    TOP_APARTMENT = (By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[1]/td[1]')  # 顶级部门
    TOP_APARTMENT_TR1_CLASS = "treegrid-1 selected focus treegrid-collapse"
    TOP_APARTMENT_TR1 = (By.XPATH, '//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[1]')  # 顶级部门
    TOP_ADD =(By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[1]/td[2]/button[1]') # 顶级部门的添加部门  按键
    TOP_ROLE =(By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[1]/td[2]/button[2]')# 顶级部门的分配角色  按键
    TOP_USER = (By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[1]/td[2]/button[3]')# 顶级部门的查看用户 按键
    TOP_MODIFY = (By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[1]/td[2]/button[4]')# 顶级部门的修改 按键
    TOP_DELETE = (By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[1]/td[2]/button[5]')# 顶级部门的删除 按键
    TOP_WINDOW = (By.XPATH,'//*[@id="jumpIframe"]')  # 顶级iframe
    MENU_NAME_TBODY = (By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody') # 所有部门所在行外层tbody
    MENU_NAME_TR = (By.XPATH,'//tr/td[1]')  # 每个部门所在行，用来获取行数
    MENU_NAME_TD = (By.XPATH, '//td[1]')  # 每个部门所在行，用来获取文本
    MENU_NAME_SPAN = (By.XPATH, '//td[1]/span[2]')  # 每个部门的文本
    MENU_NAME_BUTTON = [By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[%s]/td[2]/button[%s]'] # 每个部门的button1  #添加部门
    # MENU_NAME_BUTTON2 = (By.XPATH, '//td[2]/button[1]')  # 每个部门的button2#分配角色
    # MENU_NAME_BUTTON3 = (By.XPATH, '//td[2]/button[1]')  # 每个部门的button3#查询用户
    # MENU_NAME_BUTTON4 = (By.XPATH, '//td[2]/button[1]')  # 每个部门的button4#修改
    # MENU_NAME_BUTTON5 = (By.XPATH, '//td[2]/button[1]')  # 每个部门的button5#删除
    APARTMENT_NAME = (By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr/td[1]')  # 部门名称所在行
    APARTMENT_NAME_X = [By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[%s]/td[1]']  # 部门名称所在行
    APARTMENT_NAME_TR = (By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr')  # 部门名称所在行

    DELETE_CONFIRM = (By.LINK_TEXT,"确定")
    DELETE_CONFIRM_XPATH = (By.XPATH,'//*[@id="layui-layer1"]/div[2]/a[1]')
    DELETE_CANCLE = (By.LINK_TEXT,"取消")
    DELETE_ALERT = (By.XPATH,'//*[@id="layui-layer1"]/div[1]')
    TD = (By.TAG_NAME,"td")
    BUTTON = (By.TAG_NAME,"button")

    ADD_CLASS = (By.CLASS_NAME,"department-add")




class AddApartmentLocator(ApartmentLocator):

    MAIN_PAGE =(By.XPATH,'//*[@id="layui-layer1"]')   # 整个页面 id会变
    MAIN_PAGE_IFRAME = (By.XPATH,'//*[@id="layui-layer1"]')  #弹出框的iframe  id会变
    NAME_LABEL= (By.XPATH,'/html/body/div/div/div[1]/label') # 名字label
    NAME_INPUT = (By.XPATH,'/html/body/div/div/div[1]/div/input[3]') # 名称输入
    # CHAIRMAN_LABEL = (By.XPATH, '/html/body/div/div/div[2]/label')# 负责人label
    # CHAIRMAN_INPUT = (By.XPATH, '/html/body/div/div/div[2]/div/input')# 负责人输入
    TYPE_LABEL = (By.XPATH, '/html/body/div/div/div[2]/label')# 类型label
    # TYPE_RADIO_INNTER = (By.XPATH, '/html/body/div/div/div[3]/div/input[1]')# 内部部门，radio选中
    TYPE_RADIO_INNTER = (By.XPATH,'/html/body/div/div/div[2]/div/div[1]/span')
    # TYPE_RADIO_OUTER = (By.XPATH, '/html/body/div/div/div[3]/div/input[2]')#外部部门，radio选中
    TYPE_RADIO_OUTER = (By.XPATH,'/html/body/div/div/div[2]/div/div[2]/span')
    COMMENT_LABEL = (By.XPATH, '/html/body/div/div/div[3]/label')# 备注label
    COMMENT_INPUT = (By.XPATH, '/html/body/div/div/div[3]/div/textarea')# 备注输入
    CLOSE_PAGE = (By.XPATH,'//*[@id="layui-layer1"]/span[1]/a[3]')# 关闭的 ✘
    CONFIRM_BUTTON = (By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]')# 确认按键
    CANCLE_BUTTON = (By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[2]')# 取消按键


class ModifyApartmentLocator(ApartmentLocator):
    MAIN_PAGE =(By.XPATH,'//*[@id="layui-layer1"]')   # 整个页面 id会变
    MAIN_PAGE_IFRAME = (By.XPATH,'//*[@id="layui-layer1"]')  #弹出框的iframe  id会变
    NAME_INPUT = (By.NAME,'name') # 名称输入
    CHAIRMAN_INPUT = (By.XPATH, '/html/body/div/div/div[2]/div/input')# 负责人输入
    TYPE_RADIO_INNTER = (By.XPATH,'/html/body/div/div/div[2]/div/div[1]/span')
    TYPE_RADIO_OUTER = (By.XPATH,'//*[@id="radioType"]/div[2]/span')
    TYPE_RADIO_OUTER_CHECK = (By.XPATH,'//*[@id="radioType"]/input[2]')
    COMMENT_INPUT = (By.NAME, 'remark')# 备注输入
    CLOSE_PAGE = (By.XPATH, '//*[@id="layui-layer1"]/span[1]/a[3]')  # 关闭的 ✘
    CONFIRM_BUTTON = (By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]')# 确认按键
    CANCLE_BUTTON = (By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[2]')# 取消按键
    APART_INPUT = (By.XPATH,'/html/body/div/div/div[3]/div/div/div/div/input')
    APART_OPTIONS = (By.XPATH,'/html/body/div/div/div[3]/div/div/div/dl/dd')