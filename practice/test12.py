#encoding:utf-8
from selenium import webdriver
from Action.PublicLogin import PublicLogin
from selenium.webdriver.support.wait import WebDriverWait
import time
import cx_Oracle
class Tt1():
    def Dingdanchengjiao(self):
        br=PublicLogin().publicLoginByCustomerCenter()
        time.sleep(5)
        # br.find_element_by_link_text(u"订单管理").click()
        br.find_element_by_css_selector("i.icon.icon-order").click()
        br.find_element_by_link_text(u"我的订单").click()
        br.find_element_by_xpath("//*[@id='buyOrder']/div/div[3]/table/tbody/tr[3]/td[6]/a[1]").click()
        br.find_element_by_css_selector("label.radio.radio-inline.f-left>input[type='radio']").click()
        time.sleep(3)
        br.find_element_by_id("cuSubBtn").click()
        time.sleep(4)
        br.find_element_by_css_selector("a.orange.sms-link").click()
        time.sleep(3)



        checkcode=self.getcheckcode()
        br.find_element_by_id("smsPwd").send_keys(checkcode)
        time.sleep(3)
        br.find_element_by_id("payPwd").send_keys("wwg123456")
        time.sleep(3)
        br.find_element_by_css_selector("input.btn_pay").click()
    def getcheckcode(self):
        con=cx_Oracle.connect('yydscs','yycs_123','192.168.2.63/chinapay')
        cr=con.cursor()
        sql="select mq.send_content from yydscs.csm_msg_sms_send mq where mq.send_to_user_id='3738017' order by mq.send_add_time desc"
        cr.execute(sql)
        rs=cr.fetchone()
        for m in rs:
            mv=m.decode('gbk')
            checkcode=mv[13:19]
            return checkcode



pp=Tt1()
pp.Dingdanchengjiao()