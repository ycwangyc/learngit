from selenium.webdriver.common.by import By
from page.page import Page
from time import sleep
from modle.log1 import Logger

#添加一行备注信息
mylogger = Logger(logger='测试标题').getlog()

class The_login(Page):
    """登录页面"""

    #登录首页URL地址
    base_url="test2018env.huawa.com/login"

    login1_loc = (By.ID,"user_name")
    # 登录会员名
    login2_loc = (By.ID,"password")
    #登录密码
    login3_loc = (By.ID, "captcha")
    #登录验证码
    login4_loc = (By.NAME, "dosubmit")
    #登录按钮
    home_page_loc = (By.LINK_TEXT,"花娃首页")
    #花娃首页A标签

    loginname_loc = (By.ID,"user_name")
    #花娃首页登录信息
    loginpassword_loc = (By.ID,"password")
    #登录密码输入框
    logindenglu_loc = (By.CLASS_NAME,"land_submit")
    #登录按钮



    def login_1(self,text):
        """会员名输入"""
        self.sendKeys(self.login1_loc,text)

    def login_2(self,text):
        """密码输入"""
        self.sendKeys(self.login2_loc,text)
    def login_3(self,text):
        """验证码输入"""
        self.sendKeys(self.login3_loc,text)

    def login_4(self):
        """登录按钮"""
        self.click(self.login4_loc)

    def login_5(self,text1,text2,text3):
        """输入账号、密码、验证码、登录操作,万能验证码方式"""
        self.login_1(text1)
        # sleep(2)
        self.login_2(text2)
        # sleep(2)
        self.login_3(text3)
        # sleep(2)
        self.login_4()
        #sleep(2)

    def login_cookie(self,name,value):
        """通过addcookID方法绕过验证码登录页面"""
        self.driver.delete_all_cookies()
        mylogger.info("删除原本的cookies")
        #删除原本的cookies
        self.driver.add_cookie({"name": name, "value": value})
        mylogger.info("输入当前用户的有效cookie" + name + ":" + value)
        #输入当前用户的有效cookie
        self.driver.refresh()
        mylogger.info("刷新页面")
        #刷新页面

    def login_send(self,name,password):
        """通过花娃首页页面，输入账号，密码登录"""
        self.sendKeys(self.loginname_loc,name)
        # 账号输入
        self.sendKeys(self.loginpassword_loc,password)
        # 输入密码
        self.click(self.logindenglu_loc)
        # 点击登录

    def home_pages(self):
        """会员首页"""
        self.click(self.home_page_loc)
        #点击会员首页