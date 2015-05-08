# encoding:utf-8
from selenium import webdriver
from Data import  ReadExcel,get_number_by_data
import time
class OperateElement():


    def operateElement(self,br,object_name,located_element,username,password,alertmessage):
        """该函数作用就是去操作已经定位到的元素，操作方式为sendkey或者click """
        br=br
        object_name=object_name
        located_element=located_element

        excel=ReadExcel.ReadExcel()
        operate_method_excelpath="F:\\pytest\\xebest-autotest\\Data\\login_data.xls"
        operate_method_sheet=excel.getTableBySheetName(operate_method_excelpath,"operate_method")
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operate_method_excelpath,"operate_method",object_name)
        operate_method=operate_method_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+1)

        print object_name
        if operate_method=='click':
            located_element.click()
            time.sleep(5)
        elif operate_method=='sendkey' and object_name=='username':
            located_element.clear()
            located_element.send_keys(username)

            print username
            time.sleep(5)
        elif operate_method=='sendkey' and object_name=='password':
            located_element.clear()
            located_element.send_keys(password)

            print password
            time.sleep(5)

