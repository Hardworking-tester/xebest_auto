# encoding:utf-8
from selenium import webdriver
from time import sleep
class Business():

    def login(self,username,password):
        br=webdriver.Firefox()
        br.get("http://www.xebest.com:8000")
        br.find_element_by_link_text(u"请登录").click()
        br.find_element_by_id('userName').send_keys(username)
        sleep(2)
        br.find_element_by_id('password').send_keys(password)
        br.find_element_by_id('imgLogin').click()
        sleep(2)
        print br.switch_to.alert.text
        br.switch_to.alert.accept()
        sleep(3)
        return br

    def quotedPrice(self):
        """
        报价功能
        """
        br=self.login('wwg54421@163.com','wwg123456')
        br.find_element_by_css_selector("input.wenben").send_keys('dssd')
        br.find_element_by_css_selector("input.sousuo").click()
        sleep(4)
        br.find_element_by_xpath("//*/div[@class='p-photo']/a/img").click()
        br.switch_to.window(br.window_handles[1])
        br.find_element_by_xpath("//div[@class='row row-last p-quote']/a/img").click()
        sleep(5)
        br.find_element_by_id('orderPrice').send_keys('30')
        br.find_element_by_id('orderNum').send_keys('2')
        br.find_element_by_id('info').send_keys('wwg')
        sleep(5)
        br.find_element_by_id('orderButton').click()
        print br.switch_to.alert.text
        br.switch_to.alert.accept()

        self.successOrderForm()

    def successOrderForm(self):
        br=self.login('b_13103712371@126.com','123abc')
        br.find_element_by_css_selector('a.red').click()
        sleep(3)
        br.switch_to.window(br.window_handles[-1])
        br.find_element_by_link_text('我是供应商').click()
        sleep(3)
        br.find_element_by_link_text('订单管理').click()
        br.find_element_by_link_text('待处理订单').click()
        br.find_element_by_link_text('点击查看更多').click()
        br.find_element_by_id('dealButton_0').click()
        br.find_element_by_css_selector("input.btn_edit_info").click()

pp=Business()
pp.quotedPrice()