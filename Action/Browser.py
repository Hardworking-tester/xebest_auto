#encoding:utf-8
from selenium import webdriver
from resultlog import ResultLog
class Browser():
    def init_browser(self):

        """
        该函数主要是初始化浏览器对象并返回一个webdriver对象
        """
        log=ResultLog.ResultLog()
        try:
            br=webdriver.Firefox()
        except:
            log.info("浏览器初始化失败了")
        br.get("http://www.xebest.com:8000")
        return br


    def init_browserByCustomerCenter(self):

        """
        该函数主要是初始化浏览器对象并返回一个webdriver对象
        """
        log=ResultLog.ResultLog()
        try:
            br=webdriver.Firefox()
        except:
            log.info("浏览器初始化失败了")
        br.get("https://user.xebest.com:8443/loginAction!init.action")
        return br

    def init_browserByRegister(self):
        """
        该函数主要是初始化浏览器对象并返回一个webdriver对象
        """
        log=ResultLog.ResultLog()
        try:
            br=webdriver.Firefox()
        except:
            log.info("浏览器初始化失败了")
        br.get("https://user.xebest.com:8443/reg.action")
        return br

