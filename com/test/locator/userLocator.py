from selenium.webdriver.common.by import By
from .mainLocator import MainPageLocator

class UserLocator(MainPageLocator):

    IFRAME = (By.ID,'jumpIframe')   #主页面的iframe
    LOGIN_NAME_INPUT = (By.NAME,'loginName')  # 检索框，登录名
    NAME_INPUT = (By.NAME,'name') #检索框，姓名
    SEARCH_BUTTON = (By.XPATH,'/html/body/div/div[1]/div/div[3]/button[1]')  #查询
    ADD_BUTTON = (By.ID,'btnUserAdd')  # 新增用户

    REFRESH_BUTTON =(By.ID,'refresh') #  右上角刷新
    TABLE_TR = (By.XPATH,'//*[@id="tableUser"]/tbody/tr')  #用户数据所在行
    TR_TD_NAME = (By.XPATH,'//td[2]')
    TR_TD_LOGIN_NAME = (By.XPATH, '//td[1]')
    TR_TD_DELETE = (By.XPATH, '//td[6]/button[1]')  ## 删除
    TR_TD_PM = (By.XPATH, '//td[6]/button[2]')  ## 权限管理
    TR_TD_CS = (By.XPATH,'//td[6]/button[3]')  ##  修改登录状态


    INNER_IFRAME = "layui-layer-iframe1"

    ADD_NAME_INPUT =(By.NAME,'name')    # 姓名
    ADD_LOGIN_NAME_INPUT = (By.NAME,'loginName') # 登录名
    ADD_PASSWD_INPUT = (By.NAME,'passwd') # 密码
    ADD_REPASSWD_INPUT =(By.NAME,'repasswd') #确认密码
    ADD_MAIL_INPUT = (By.NAME,'email') #邮箱
    ADD_MOBILE_INPUT = (By.NAME,'mobile') # 手机号
    ADD_APART_INPUT = (By.NAME,'departmentids') #部门
    ADD_APART_INPUT_CLICK = (By.XPATH,'/html/body/div/div/div[7]/div/div/div/input') ##点击部门
    ADD_APART_INPUT_CLASS = (By.CLASS_NAME,'layui-select-title') ## 部门输入的div的class
    ADD_APART_INPUT_TRIANGLE_CLASS  = (By.CLASS_NAME,'layui-edge') ## 那个三角
    ADD_APART_INPUT_DD = (By.XPATH,'/html/body/div/div/div[7]/div/div/dl/dd')  ## 可选的部门
    ADD_APART_INPUT_SCRIPT = (By.XPATH,'/html/body/div/div/div[7]/div/div')  ## 需要用script改变class
    ADD_BTN_CONFIRM = (By.CLASS_NAME,"layui-layer-btn0") #确认
    ADD_BTN_CANCEL = (By.CLASS_NAME,"layui-layer-btn1")   ###取消
    MAX_WINDOW = (By.XPATH,'//*[@id="layui-layer1"]/span[1]/a[2]')  ##放大
    MAX_WINDOW_CLASS = (By.CLASS_NAME,'layui-layer-max')  ## 放大

    ## 角色分配

    ROLE_APPLY_DATA =(By.XPATH,'//*[@id="userallotPage"]/div/div')  ## 角色名称数据
    ROLE_APPLY_DATA_SPAN = (By.TAG_NAME,'span')
    ROLE_APPLY_DATA_CHECKBOX = (By.XPATH,"//input[@type='checkbox']")
    ROLE_APPLY_DATA_DIV = (By.TAG_NAME,'div')  ##
    ROLE_APPLY_SAVE_CONFIRM = (By.LINK_TEXT,"保存")
    ROLE_APPLY_SAVE_CLASS = (By.CLASS_NAME,'layui-layer-btn0') ## 保存
    ROLE_APPLY_SAVE_CANCEL = (By.LINK_TEXT,"取消")   ###

    # LOADING = (By.ID,'layui-layer1') ## loading

    FIRST_USER_DATA_PM= (By.XPATH,'//*[@id="tableUser"]/tbody/tr/td[6]/button[2]')  ## 第一条数据的，权限编辑
    FIRST_USER_DATA_CS= (By.XPATH,'//*[@id="tableUser"]/tbody/tr/td[6]/button[3]')  ## 第一条数据的，登录状态修改
    FIRST_USER_DATA_ST= (By.XPATH,'//*[@id="tableUser"]/tbody/tr/td[4]')  ## 第一条数据的，登录状态


    VIEW_SHADE = (By.CLASS_NAME,'layui-layer-shade')
