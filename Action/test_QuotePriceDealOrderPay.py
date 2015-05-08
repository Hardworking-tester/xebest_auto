#encoding:utf-8
from PublicMethod import LocateElementCommonClass
from selenium import webdriver
import PublicLogin
import time,unittest
from Data import ReadExcel,get_number_by_data
from object import LocatePayByBalanceObject
from PublicMethod import LocateElementCommonClass
from resultlog import ResultLog
from resultlog.ResultLog import ResultLog

#使用余额付款
class QuotePriceDealOrderPay(unittest.TestCase):

    def setUp(self):
        try:
            self.browser=PublicLogin.PublicLogin().publicLoginByCustomerCenter()
            time.sleep(5)
        except:
            print ("webdriver init error")
            raise NameError("webdriver init error")


    def getSendData(self,testcaseId):
        excel=ReadExcel.ReadExcel()
        send_data_path="F:\\pytest\\xebest-autotest\\Data\\pay_by_balance.xls"
        send_data_sheet=excel.getTableBySheetName(send_data_path,"pay_by_balance")
        cols=send_data_sheet.ncols
        #得到测试用例id所在的行号
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(send_data_path,"pay_by_balance",testcaseId)[0]
        send_data_list=[]
        for i in range(2,cols):
            send_data_list.append(send_data_sheet.cell_value(row_index,i))

        return send_data_list


    def testPayOrder(self):
        u"""测试使用余额正常付款功能"""
        testcaseId='case_0010'
        print testcaseId
        send_data_list=self.getSendData(testcaseId)
        LocatePayByBalanceObject.LocatePayByBalanceObject().getLocateElementList(self.browser,testcaseId,send_data_list)
        time.sleep(2)
        LocateElementCommonClass.CommonClass().dealAlert(self.browser)



    def tearDown(self):
        self.browser.close()



