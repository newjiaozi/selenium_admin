from selenium.webdriver.common.by import By
from .mainLocator import MainPageLocator

class MenuLocator(MainPageLocator):
    IFRAME = 'jumpIframe'
    MENU_DATA_TR = (By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr') # 每一行数据
    TR_TD1 = (By.XPATH,'//td[1]')
    TR_TD2 = (By.XPATH, '//td[2]')
    TR_TD3 = (By.XPATH, '//td[3]')
    TR_TD = (By.TAG_NAME,'td')
    TR_TD_BTN1 = (By.XPATH,'//td[3]/button[1]') # 添加
    TR_TD_BTN2 = (By.XPATH,'//td[3]/button[1]') # 修改
    TR_TD_BTN3 = (By.XPATH,'//td[3]/button[1]') # 删除
    TR_TD_BTN = (By.TAG_NAME,'button')

    MENU_DATA_TR_DATA = (By.TAG_NAME,'button') # 上面元素下方的button
    MENU_DATA_FIRST_LINE_ADD = (By.XPATH,'//*[@id="treeMenu"]/div/div[2]/table/tbody/tr[1]/td[3]/button[1]')  ##第一行添加
    ##添加系统
    ADD_SYSTEM_NAME = (By.NAME,'name')
    ADD_SYSTEM_REMARK = (By.NAME,'remark')
    ADD_SYSTEM_APART = (By.XPATH,'/html/body/div/div/div[3]/div/div/div/div/div/input')  ## 点击部门
    ADD_SYSTEM_APART_DD = (By.XPATH,'/html/body/div/div/div[3]/div/div/div/div/dl/dd')  ##部门的list
    ADD_CONFIRM = (By.LINK_TEXT,'确认')
    ADD_CANCEL = (By.LINK_TEXT, '取消')

    ##添加菜单
    ADD_MENU_NAME = (By.NAME,'name')
    ADD_MENU_REMARK = (By.NAME,'remark')
    ADD_MENU_APART = (By.XPATH,'/html/body/div/div/div[3]/div/div/div/div/div/input')  ## 点击部门
    ADD_MENU_APART_DD = (By.XPATH,'/html/body/div/div/div[3]/div/div/div/div/dl/dd')  ##部门的list
    # ADD_CONFIRM = (By.LINK_TEXT,'确认')
    # ADD_CANCEL = (By.LINK_TEXT, '取消')

    ##添加页面
    ADD_PAGE_NAME = (By.NAME,'name')
    ADD_PAGE_REMARK = (By.NAME,'remark')
    ADD_PAGE_TARGET = (By.NAME, 'target')
    ADD_PAGE_APART = (By.XPATH,'/html/body/div/div/div[4]/div/div/div/div/div/input')  ## 点击部门
    ADD_PAGE_APART_DD = (By.XPATH,'/html/body/div/div/div[4]/div/div/div/div/dl/dd')  ##部门的list
    # ADD_CONFIRM = (By.LINK_TEXT,'确认')
    # ADD_CANCEL = (By.LINK_TEXT, '取消')

    ##添加接口
    ADD_INTERFACE_NAME = (By.NAME,'name')
    ADD_INTERFACE_REMARK = (By.NAME,'remark')
    ADD_INTERFACE_TARGET = (By.NAME, 'target')
    ADD_INTERFACE_APART = (By.XPATH,'/html/body/div/div/div[4]/div/div/div/div/div/input')  ## 点击部门
    ADD_INTERFACE_APART_DD = (By.XPATH,'/html/body/div/div/div[4]/div/div/div/div/dl/dd')  ##部门的list
    # ADD_CONFIRM = (By.LINK_TEXT,'确认')
    # ADD_CANCEL = (By.LINK_TEXT, '取消')


    ##编辑页面
    EDIT_APART = (By.XPATH,'/html/body/div/div/div[3]/div/div/div/div/div/input')   ##部门有数据时才有的部门input
    DELETE_APART= (By.CLASS_NAME,'delDepartment')  ##删除的图标
    ADD_APART = (By.ID,'addDepartment')


    ##删除确认
    DELETE_CONFIRM = (By.LINK_TEXT,"确定")
    DELETE_CANCLE = (By.LINK_TEXT,"取消")


    ##laoding
    LAODING = (By.CLASS_NAME,'layui-layer-loading')
