#encoding:utf-8
import os
import sys,xlrd
from selenium.webdriver.common.by import By
from Data import ReadExcel,get_number_by_data
from Action import Browser
import time,OperateLoginElement
class LocateLoginObject():
    #该类主要是去定位登录功能中所用到的元素
    def getLocateObject(self,browser,username,password,alertmessage):
        """循环需要定位的元素，拿到一个元素之后去调用getLocatMethodAndData方法，取得元素的定位方式以及定位所需数据"""
        browser=browser
        excel=ReadExcel.ReadExcel()
        object_excelpath="F:\\pytest\\xebest-autotest\\Data\\login_data.xls"
        object_sheet=excel.getTableBySheetName(object_excelpath,"objname_locatemethod_locatedata")
        object_sheet_rows=object_sheet.nrows
        object_name_list=[]#得到需要定位的元素的名称的列表
        for i in range(object_sheet_rows):#拿到登录功能中需要定位的对象名称列表
            object_name_list.append(object_sheet.cell(i,0).value)
        object_name_list.pop(0)#去掉对象名excel中的第一行的标签项名称
        #循环需要定位的元素，拿到一个元素之后去调用getLocatMethodAndData方法，取得元素的定位方式以及定位所需数据
        for object_name in object_name_list:
            self.getLocateMethodAndData(browser,object_name,username,password,alertmessage)


    def getLocateMethodAndData(self,browser,objname,username,password,alertmessage):
        """根据需要定位的元素的名称得到需要定位的元素的定位方式以及定位数据"""
        obj_name=objname
        br=browser
        excel_path="F:\\pytest\\xebest-autotest\\Data\\login_data.xls"
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(excel_path,"objname_locatemethod_locatedata",obj_name)
        excel=ReadExcel.ReadExcel()
        locate_method_data_excelpath="F:\\pytest\\xebest-autotest\\Data\\login_data.xls"
        locate_method_data_sheet=excel.getTableBySheetName(locate_method_data_excelpath,"objname_locatemethod_locatedata")

        old_how=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+1)
        what=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+2)
        #在这里增加一个字典是因为如果直接把By.ID写在excel里的话，取出来不能用
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}

        #下述代码判断定位方式

        new_how=locate_method_dict[old_how]
        # if old_how=='linktext':
        #     new_how=locate_method_dict["linktext"]
        # elif old_how=='id':
        #     new_how=locate_method_dict['id']
        # elif old_how=='css':
        #     new_how=locate_method_dict["css"]
        # elif old_how=='xpath':
        #     new_how=locate_method_dict["xpath"]
        print obj_name,new_how,what
        #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
        self.locateElement(br,new_how,what,obj_name,username,password,alertmessage)

    def locateElement(self,browser,how,what,obj_name,username,password,alertmessage):
        br=browser
        object_name=obj_name
        try:
            located_element=br.find_element(by=how,value=what)
        except:
            print (u"元素: %s 未找到" %obj_name)
        #调用操作元素的方法
        OperateLoginElement.OperateElement().operateElement(br,object_name,located_element,username,password,alertmessage)

