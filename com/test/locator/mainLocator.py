from selenium.webdriver.common.by import By

class MainPageLocator():
    USER_MANAGE_BUTTON = (By.PARTIAL_LINK_TEXT,"用户管理")
    MENU_MANAGE_BUTTION=(By.PARTIAL_LINK_TEXT,"菜单管理")
    ROLE_MANAGE_BUTTON=(By.PARTIAL_LINK_TEXT,"角色管理")
    APARTMENT_MANAGE_BUTTION = (By.PARTIAL_LINK_TEXT,"部门管理")
    LOG_MANAGE_BUTTION = (By.LINK_TEXT,"日志管理")
    LOGIN_LOG_MANAGE_BUTTION = (By.LINK_TEXT,"登录日志管理")

    LAYUI_LAYOUT_ADMIN = (By.CLASS_NAME,'layui-layout-admin')

    EXPEND_SYSTEM = (By.XPATH,'/html/body/div/div[1]/div[2]/i')  # 展开所有系统的三角
    QXXT_SYSTEM = (By.LINK_TEXT,'权限系统')   #权限系统
    SYSTEM_UL = (By.XPATH,'/html/body/div/div[1]/ul')
    SYSTEM_DIV = (By.XPATH,'/html/body/div/div[1]/div[2]')

    PERSON_LOGIN_SUCCESS = (By.CLASS_NAME,'ma-userinfo')
    SHADE_CLASS = (By.CLASS_NAME,'layui-layer-shade')


    # USER_MANAGE_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div/ul/li/dl/dd[1]/a")
    # MENU_MANAGE_BUTTION=(By.XPATH,"/html/body/div[1]/div[2]/div/ul/li/dl/dd[2]/a")
    # ROLE_MANAGE_BUTTON=(By.XPATH,"/html/body/div[1]/div[2]/div/ul/li/dl/dd[3]/a")
    # APARTMENT_MANAGE_BUTTION = (By.XPATH,"/html/body/div[1]/div[2]/div/ul/li/dl/dd[4]/a")




    INNER_IFRAME = "layui-layer-iframe1"  ## 内部iframe
    LOADING = (By.CLASS_NAME,'layui-layer-loading') ## loading


    ## 贷后系统-内催列表
    NCLB_A = (By.LINK_TEXT,'内催列表')
    EXPORT_DATA = (By.XPATH,'/html/body/div/div[1]/div/div[15]/button[2]')
    NC_LIST = (By.XPATH,'//*[@id="tableRole"]/tbody/tr')