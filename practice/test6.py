# encoding:utf-8
from selenium import selenium
import unittest

class BauDu(unittest.TestCase):

    seleniumHost = 'localhost'
    seleniumPort = str(4444)
    #browserStartCommand = "c:\\program files\\internet explorer\\iexplore.exe"
    browserStartCommand = "*firefox"
    browserURL = "http://www.baidu.com"

    def setUp(self):
        # self.selenium=selenium(host="localhost",port=4444,browserStartCommand='*firefox',browserURL="http://localhost:4444",http_timeout=90)
        # print
        # self.selenium.start()
        print "准备调用"
        self.selenium = selenium("localhost",4444, "*firefox", "http://www.baidu.com")
        print "调用开始"
        self.selenium.start()
    def testsel(self):
        sel=self.selenium
        sel.open('/')


    def tearDown(self):
        # self.selenium.stop()
        pass

if __name__=="__main__":
    unittest.main()