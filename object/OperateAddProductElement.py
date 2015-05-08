# encoding:utf-8
from selenium import webdriver
from Data import  ReadExcel,get_number_by_data
import time
class OperateElement():


    def opermateAddProductElement(self,br,object_name,located_element,data_list):
        br=br
        object_name=object_name
        located_element=located_element

        excel=ReadExcel.ReadExcel()
        operate_method_excelpath="F:\\pytest\\xebest-autotest\\Data\\addProduct_data.xls"
        operate_method_sheet=excel.getTableBySheetName(operate_method_excelpath,"operate_method")
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operate_method_excelpath,"operate_method",object_name)
        operate_method=operate_method_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+1)

        print object_name
        if operate_method=='click':
            located_element.click()
            time.sleep(2)
        elif operate_method=='sendkey' and object_name==u'产品标题':
            located_element.clear()
            located_element.send_keys(data_list[0])
        elif operate_method=='sendkey' and object_name==u'关键词':
            located_element.clear()
            located_element.send_keys(data_list[1])
        elif operate_method=='sendkey' and object_name==u'产品规格':
            located_element.clear()
            located_element.send_keys(data_list[2])

        elif operate_method=='sendkey' and object_name==u'生产厂家':
            located_element.clear()
            located_element.send_keys(data_list[3])

        elif operate_method=='sendkey' and object_name==u'保质期':
            located_element.clear()
            located_element.send_keys(int(data_list[4]))

        elif operate_method=='sendkey' and object_name==u'存储条件':
            located_element.clear()
            located_element.send_keys(data_list[5])

        elif operate_method=='sendkey' and object_name==u'生产许可证号':
            located_element.clear()
            located_element.send_keys(data_list[6])

        elif operate_method=='sendkey' and object_name==u'产品标准号':
            located_element.clear()
            located_element.send_keys(data_list[7])

        elif operate_method=='sendkey' and object_name==u'批发价':
            located_element.clear()
            located_element.send_keys(int(data_list[8]))

        elif operate_method=='sendkey' and object_name==u'零售价':
            located_element.clear()
            located_element.send_keys(int(data_list[9]))

        elif operate_method=='sendkey' and object_name==u'供货量':
            located_element.clear()
            located_element.send_keys(int(data_list[10]))

        elif operate_method=='sendkey' and object_name==u'最小起订量':
            located_element.clear()
            located_element.send_keys(int(data_list[11]))

        elif operate_method=='sendkey' and object_name==u'发货期限':
            located_element.clear()
            located_element.send_keys(int(data_list[12]))

        elif operate_method=='sendkey' and object_name==u'图片上传弹出框的浏览按钮':

            located_element.send_keys(data_list[13])

        elif operate_method=='sendkey' and object_name==u'产品简介':
            located_element.clear()
            located_element.send_keys(data_list[14])

        elif operate_method=='sendkey' and object_name==u'验证码':
            located_element.clear()
            located_element.send_keys(int(data_list[15]))
        elif operate_method=='submit':
            located_element.submit()

        elif operate_method=='Gettext':
            print located_element.text


