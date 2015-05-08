#encoding:utf-8

from selenium import webdriver
import time
from resultlog import ResultLog
class Produ():

    def tt1(self):
        log=ResultLog.ResultLog()
        try:
            br=webdriver.Firefox()
            br.find_element_by_id("wwg").click()
            raise NameError()
        except:
            print "except捕获异常"


pp=Produ()
pp.tt1()