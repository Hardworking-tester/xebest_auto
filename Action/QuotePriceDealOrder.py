#encoding:utf-8
from PublicMethod import LocateElementCommonClass
from selenium import webdriver
import PublicLogin
import time,unittest
from Data import ReadExcel,get_number_by_data
from object import LocateDealOrderObject
from resultlog.ResultLog import ResultLog

class DealOrder(unittest.TestCase):

    def setUp(self):

        self.browser=PublicLogin.PublicLogin().publicLoginBySellerCenter()


    def testDealOrder(self):
        u"""测试卖家正常成交订单功能"""
        testcaseId='case_0009'
        print testcaseId
        LocateDealOrderObject.LocateDealOrderObject().getElementList(self.browser,testcaseId)
        self.browser.get_screenshot_as_file("F:\\testresult\\image_SUCCESSdealorder.png")
        print("image_SUCCESSdealorder.png ")

    def tearDown(self):
        self.browser.close()

# pp=DealOrder()
# pp.DealOrder()
# if __name__=='__main__':
#     unittest.main()
