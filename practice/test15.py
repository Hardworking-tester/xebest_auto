#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Action import PublicLogin
import time
class SendGood():


    def sendGood(self):
        br=PublicLogin.PublicLogin().publicLoginBySellerCenter()
        time.sleep(5)
        br.find_element_by_link_text(u"我是供应商").click()
        br.find_element_by_link_text(u"订单管理").click()
        br.find_element_by_link_text(u"我的订单").click()
        time.sleep(2)
        br.find_element_by_xpath("//table[@class='order-list-table zz-table']/tbody/tr[3]/td[8]/a").click()
        br.find_element_by_id("logisticsInfo").send_keys("wwg")
        br.find_element_by_id("remark").send_keys("wuliu")
        br.find_element_by_class_name("btn_affirm").click()
pp=SendGood()
pp.sendGood()