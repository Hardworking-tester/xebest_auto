#encoding:utf-8
from PublicMethod import LocateElementCommonClass
from selenium import webdriver
import PublicLogin
import time,unittest
from Data import ReadExcel,get_number_by_data
from object import LocateQuotePriceObject
from resultlog.ResultLog import ResultLog


class QuotePrice(unittest.TestCase):

    def setUp(self):
        self.browser=PublicLogin.PublicLogin().publicLoginByCustomer()


    def getQuotePriceDataByTestcaseId(self,testcaseId):

        excel=ReadExcel.ReadExcel()
        testcase_excelpath="F:\\pytest\\xebest-autotest\\Data\\quoteprice_data.xls"
        testcase_sheet=excel.getTableBySheetName(testcase_excelpath,"quoteprice_data")
        send_data_list=[]
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(testcase_excelpath,"quoteprice_data",testcaseId)
        cols=testcase_sheet.ncols
        for i in range(2,cols):
            send_data_list.append(testcase_sheet.cell_value(row_col_number_list[0],i))

        return send_data_list


    def testQuotePriceSuccess(self):
        u"""测试正常报价功能"""
        testcaseId='case_0008'
        print testcaseId
        log=ResultLog()
        log.info("本次操作的测试用例的ID为%s" %testcaseId)
        data_list=self.getQuotePriceDataByTestcaseId(testcaseId)
        LocateQuotePriceObject.LocateQuotePriceObject().getLocateObject(testcaseId,self.browser,data_list)

        LocateElementCommonClass.CommonClass().dealAlert(self.browser)
        self.browser.get_screenshot_as_file("F:\\testresult\\image_SUCCESSquoteprice.png")
        print("image_SUCCESSquoteprice.png ")


    def tearDown(self):
        self.browser.close()
        self.browser.switch_to_window(self.browser.window_handles[0])
        self.browser.close()


