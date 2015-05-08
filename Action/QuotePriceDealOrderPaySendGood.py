#encoding:utf-8
from PublicMethod import LocateElementCommonClass
from selenium import webdriver
import PublicLogin
import time,unittest
from Data import ReadExcel,get_number_by_data
from object import LocateQuotePriceObject
from resultlog.ResultLog import ResultLog


class QuotePriceDealOrderSendGood():

    # def setUp(self):
    #
    #     self.browser=webdriver.Firefox()
    #     self.browser.get("http://www.sina.com.cn")

    def getSendDataList(self,testcaseId):
        excel=ReadExcel.ReadExcel()
        sendGoods_excel_path="F:\\pytest\\xebest-autotest\\Data\\send_goods.xls"
        sendGoods_sheet=excel.getTableBySheetName(sendGoods_excel_path,"send_goods")
        sendGoods_data_list=[]
        #得到测试用例编号所在行号
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(sendGoods_excel_path,"send_goods",testcaseId)[0]
        cols=sendGoods_sheet.ncols
        for i in range(2,cols):
            sendGoods_data_list.append(sendGoods_sheet.cell_value(row_index,i))

        return sendGoods_data_list




    def sendGood(self):
        u"""测试正常发货功能"""
        testcaseId='case_0011'
        print testcaseId
        send_data_list=self.getSendDataList(testcaseId)
        for m in send_data_list:
            print m


    # def tearDown(self):
    #     self.browser.close()

pp=QuotePriceDealOrderSendGood()
pp.sendGood()
# if __name__=="__main__":
#     unittest.main()
