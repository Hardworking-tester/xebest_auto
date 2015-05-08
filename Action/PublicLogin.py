# encoding:utf-8
from login import Login
from object import LocateLoginObject
import Browser,time
from selenium import webdriver
class PublicLogin():
    """本类作为公共方法，简化了正确登录方法并在最后获得会员中心页面的句柄，最后返回一个webdriver对象"""



    #一般通用的登陆方法
    def publicLogin(self):
        br=Browser.Browser().init_browser()
        br.find_element_by_link_text(u"请登录").click()
        time.sleep(2)
        br.find_element_by_id('userName').send_keys('wwg54421@163.com')
        time.sleep(2)
        br.find_element_by_id('password').send_keys('wwg123456')
        br.find_element_by_id('imgLogin').click()
        time.sleep(2)
        br.switch_to.alert.accept()
        time.sleep(5)
        return br

    #从会员中心登陆
    def publicLoginByCustomerCenter(self):
        br=Browser.Browser().init_browserByCustomerCenter()
        time.sleep(3)
        br.find_element_by_id('userName').send_keys('wwg54421@163.com')
        br.find_element_by_id('passWord').send_keys('wwg123456')
        br.find_element_by_id("checkCode").send_keys('12345')
        br.find_element_by_id('submit-btn').click()
        return br

    #以卖家身份从会员中心登录
    def publicLoginBySellerCenter(self):
        br=Browser.Browser().init_browserByCustomerCenter()
        time.sleep(3)
        br.find_element_by_id('userName').send_keys('wwg88481@163.com')
        br.find_element_by_id('passWord').send_keys('wwg123456')
        br.find_element_by_id("checkCode").send_keys('12345')
        br.find_element_by_id('submit-btn').click()
        return br

    #个人身份认证者登陆，即买家登陆
    def publicLoginByCustomer(self):
        br=Browser.Browser().init_browser()
        br.find_element_by_link_text(u"请登录").click()
        time.sleep(2)
        br.find_element_by_id('userName').send_keys('wwg54421@163.com')
        time.sleep(2)
        br.find_element_by_id('password').send_keys('wwg123456')
        br.find_element_by_id('imgLogin').click()
        time.sleep(2)
        br.switch_to.alert.accept()
        time.sleep(5)
        return br


    #企业身份登陆，即卖家身份登陆
    def publicLoginBySeller(self):
        br=Browser.Browser().init_browser()
        br.find_element_by_link_text(u"请登录").click()
        time.sleep(2)
        br.find_element_by_id('userName').send_keys('wwg88481@163.com')
        time.sleep(2)
        br.find_element_by_id('password').send_keys('wwg123456')
        br.find_element_by_id('imgLogin').click()
        time.sleep(2)
        br.switch_to.alert.accept()
        time.sleep(5)
        return br
