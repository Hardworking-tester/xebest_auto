# encoding:utf-8
from Data import ReadExcel,get_number_by_data
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import OperateRegisterElement
class LocateRegisterObject():



    def getLocateObject(self,browser,register_data_list):
        register_exclepath="F:\\pytest\\xebest-autotest\\Data\\register_data.xls"
        register_sheetname="objname_locatemethod_locatedata"
        register_sheet=ReadExcel.ReadExcel().getTableBySheetName(register_exclepath,register_sheetname)
        register_object_list=[]
        register_object_rows=register_sheet.nrows
        for i in range(register_object_rows):
            register_object_list.append(register_sheet.cell_value(i,0))

        register_object_list.pop(0)
        for obj in register_object_list:
            if self.judgeElementIsOperate(obj):
                self.getRegisterObjectLocateMethod(browser,register_data_list,obj)
            else:
                print (u"本次不操作元素:")+obj

    def judgeElementIsOperate(self,objname):
        judge_excelpath="F:\\pytest\\xebest-autotest\\Data\\register_data.xls"
        judge_sheetname="isoperateElement"
        judge_sheet=ReadExcel.ReadExcel().getTableBySheetName(judge_excelpath,judge_sheetname)
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(judge_excelpath,judge_sheetname,objname)
        if judge_sheet.cell_value(row_col_list[0],(row_col_list[1]+1))=="Y":
            return True
        else:
            return False

    def getRegisterObjectLocateMethod(self,browser,register_data_list,register_object):
        register_exclepath="F:\\pytest\\xebest-autotest\\Data\\register_data.xls"
        register_sheetname="objname_locatemethod_locatedata"
        register_sheet=ReadExcel.ReadExcel().getTableBySheetName(register_exclepath,register_sheetname)
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(register_exclepath,register_sheetname,register_object)
        old_how=register_sheet.cell_value(row_col_list[0],(row_col_list[1]+1))
        what=register_sheet.cell_value(row_col_list[0],(row_col_list[1]+2))
        #在这里增加一个字典是因为如果直接把By.ID写在excel里的话，取出来不能用
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        new_how=locate_method_dict[old_how]
        self.locateRegisterObject(browser,register_data_list,register_object,new_how,what)


    def locateRegisterObject(self,browser,register_data_list,objname,how,what):
        br=browser
        located_element=br.find_element(by=how,value=what)
        OperateRegisterElement.OperateRegisterElement().operateElement(register_data_list,objname,located_element)

