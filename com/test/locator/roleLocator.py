from selenium.webdriver.common.by import By
from .mainLocator import MainPageLocator

class RoleLocator(MainPageLocator):
    IFRAME = 'jumpIframe' # iframe
    ROLE_NAME = (By.NAME,'roleName')  #角色名称
    ROLE_TYPE_VALUE = (By.NAME,'roleTypeValue') #角色code
    SEARCH_BUTTON = (By.XPATH,'/html/body/div/div[1]/div/div[3]/button[1]') #查询按键
    ADD_ROLE_BUTTON = (By.ID,'btnAdd')  # 新增角色
    ROLE_DATA_TR = (By.XPATH,'//*[@id="tableRole"]/tbody/tr') # 每个角色数据行
    TR_TD_ROLE_NAME = (By.XPATH,'//td[1]') # 角色名称
    TR_TD_ROLE_CODE = (By.XPATH, '//td[2]')  # 角色CODE


    ROLE_USER_MANAGE = (By.CLASS_NAME,'roleUser') #管理用户角色
    ROLE_EDIT = (By.CLASS_NAME,'btnEdit') # 修改权限
    ROLE_DELETE = (By.CLASS_NAME,'btnDel') #删除角色
    REFRESH_BUTTON = (By.ID,'refresh')  # 右上角的刷新

    ### 新建角色
    ADD_ROLE_NAME = (By.NAME,'roleName')  #角色名称
    ADD_ROLE_TYPE_VALUE = (By.NAME,'roleTypeValue') #角色code
    ADD_ROLE_APART_INPUT = (By.XPATH,'/html/body/div/div/div/div[3]/div/div/div/div/div/input') #角色部门
    SELECT_QS_MENU = (By.XPATH,'//*[@id="menuList"]/div[1]/table/tbody/tr[1]/td[1]/div/span')   # 菜单中的最左边第一个
    SAVE_SUBMIT = (By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]')  #新建角色页面中的 保存
    APART_OPTIONS = (By.XPATH,'/html/body/div/div/div/div[3]/div/div/div/div/dl/dd')  ## 部门
    MENU_ALL_CHECKBOX = (By.XPATH,'//*[@id="menuList"]/div[1]/table/tbody/tr')  ## 确认所有权限菜单展示完成

    MENU_LIST_DIV = (By.CLASS_NAME,'layui-form-checkbox')
    MENU_LIST_DIV_SPAN = (By.XPATH,'//div[@lay-skin="primary"]span')
    MENU_LIST_SPAN = (By.XPATH,'span')
    MENU_LIST_I = (By.TAG_NAME, 'i')

    MENU_LIST_A = (By.LINK_TEXT,'%s')

    MENU_LIST_TITLE = (By.XPATH,'/html/body/div/div/div/div[5]/ul/li')



    ### 管理角色用户
    INNTER_IRFAME = "layui-layer-iframe1"
    FIRST_USER = (By.XPATH,'/html/body/div/div/div[1]/span')
    HAVE_NOT_USER = (By.XPATH,'/html/body/div/div')  ## text为 此角色没有绑定用户！
    CANCEL_BITTON_USER = (By.LINK_TEXT,'取消')
    DELETE_BITTON_USER = (By.LINK_TEXT,'删除')
    ROLE_USER_SPAN = (By.TAG_NAME, 'span')

    ### 修改权限
    EDIT_ROLE_NAME = (By.NAME,'roleName')  #角色名称
    EDIT_ROLE_TYPE_VALUE = (By.NAME,'roleTypeValue') #角色code
    EDIT_ROLE_APART = (By.XPATH,'/html/body/div/div/div[1]/div[3]/div/div/div/div/div/input')
    EDIT_SAVE_BUTTON = (By.LINK_TEXT,"确定")
    EDIT_CANCEL_BUTTON = (By.LINK_TEXT,'取消')

    ### 删除
    DELETE_ALERT = (By.XPATH,'//*[@id="layui-layer1"]/div[1]')  ## text:  确定要删除？
    DELETE_CONFIRM = (By.LINK_TEXT,"确定")
    DELETE_CANCLE = (By.LINK_TEXT,"取消")



    # LOADING = (By.ID,'layui-layer1') ## loading