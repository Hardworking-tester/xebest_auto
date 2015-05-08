#encoding:utf-8
from Data import ReadExcel,get_number_by_data
import time
from selenium import webdriver
class OperateQuotePriceObject():

    def opermateQuotePriceElement(self,browser,located_element,locate_object,send_data):
        browser=browser
        located_element=located_element
        locate_object=locate_object
        send_data_list=send_data

        excel=ReadExcel.ReadExcel()
        operate_method_excelpath="F:\\pytest\\xebest-autotest\\Data\\quoteprice_data.xls"
        operate_method_sheet=excel.getTableBySheetName(operate_method_excelpath,"operate_method")
        #得到操作方式所在的列
        operateData_key=u"操作方式"
        opreatemethod_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operate_method_excelpath,"operate_method",operateData_key)[1]

        #得到操作方式所在的行
        opreatemethod_rowNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operate_method_excelpath,"operate_method",locate_object)[0]

        #得到操作方式
        operate_method=operate_method_sheet.cell_value(opreatemethod_rowNumber,opreatemethod_colNumber)

        if operate_method=="click":
            located_element.click()
            time.sleep(2)
        elif operate_method=="sendkey" and locate_object==u'首页搜索输入框':
            located_element.clear()
            # print send_data_list[0]
            located_element.send_keys(send_data_list[0])
        elif operate_method=="sendkey" and locate_object==u"产品单价":
            located_element.clear()
            located_element.send_keys(int(send_data_list[1]))
        elif operate_method=="sendkey" and locate_object==u"产品数量":
            located_element.clear()
            located_element.send_keys(int(send_data_list[2]))
        elif operate_method=="sendkey" and locate_object==u"报价描述":
            located_element.clear()
            located_element.send_keys(send_data_list[3])

