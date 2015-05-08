#encoding:utf-8
from Data import get_number_by_data,ReadExcel
from selenium import webdriver
from object import OperateDealOrderObject
from selenium.webdriver.common.by import By
from PublicMethod.LocateElementCommonClass import CommonClass
class LocateDealOrderObject():

    def getElementList(self,br,testcaseId):
        testcase_id=testcaseId
        excel=ReadExcel.ReadExcel()
        excel_path="F:\\pytest\\xebest-autotest\\Data\\deal_order.xls"
        excel_sheet=excel.getTableBySheetName(excel_path,"objname_locatemethod_locatedata")
        rows=excel_sheet.nrows
        element_list=[]
        for i in range(1,rows):
            element_list.append(excel_sheet.cell_value(i,0))

        for element in element_list:
            #调用判断元素是否操作的方法
            if self.judgeElementIsOperate(element,testcase_id):
                #调用定位元素的方法
                self.getLocateMethodAndData(br,element)
            else:
                print ("元素：%s不需要操作" %element)

    def judgeElementIsOperate(self,element,testcase_id):

        excel=ReadExcel.ReadExcel()
        excel_path="F:\\pytest\\xebest-autotest\\Data\\deal_order.xls"
        excel_sheet=excel.getTableBySheetName(excel_path,"isoperateElement")
        #得到元素所在的行号
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(excel_path,"isoperateElement",element)[0]
        #得到测试用例所在的列号
        col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(excel_path,"isoperateElement",testcase_id)[1]

        operateFlag=excel_sheet.cell_value(row_index,col_index)

        if operateFlag=="Y":
            return True
        else:
            return False

    def getLocateMethodAndData(self,br,element):
        element=element
        excel=ReadExcel.ReadExcel()
        object_excel_path="F:\\pytest\\xebest-autotest\\Data\\deal_order.xls"
        object_sheet=excel.getTableBySheetName(object_excel_path,"objname_locatemethod_locatedata")
        #得到元素所在行
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(object_excel_path,"objname_locatemethod_locatedata",element)[0]
        #得到定位方式所在列
        locateMethod_Key=u"定位方式简述"
        locateMethod_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(object_excel_path,"objname_locatemethod_locatedata",locateMethod_Key)[1]
        #得到定位所需数据所在列
        locateData_key=u"定位所需数据"
        locateData_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(object_excel_path,"objname_locatemethod_locatedata",locateData_key)[1]

        #得到判断元素是否需要二次定位的判断条件所在列
        isSecondLocate_key=u"是否需要二次定位"
        SecondLocate_key_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(object_excel_path,"objname_locatemethod_locatedata",isSecondLocate_key)[1]
        #存储从excel表中取出的定位方式和定位数据,以及判断是否需要二次定位的条件
        old_how=object_sheet.cell_value(row_index,locateMethod_colNumber)
        old_what=object_sheet.cell_value(row_index,locateData_colNumber)
        secondLocate=object_sheet.cell_value(row_index,SecondLocate_key_colNumber)
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}

        if not(CommonClass().judgeSecondLocateElement(secondLocate)):
            if old_how=="switchHandle":
                index=int(old_what)
                CommonClass().switchHandle(br,index)
            else:
                new_how=locate_method_dict[old_how]
                located_element=CommonClass().findElement(br,new_how,old_what)
                OperateDealOrderObject.OperateDealOrderObject().operateLocatedElement(element,located_element)

        else:
            new_first_how=locate_method_dict[old_how]
            #得到二次定位方式的值所在列
            secondLocatemethod_key=u"二次定位的方式"
            secondLocate_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(object_excel_path,"objname_locatemethod_locatedata",secondLocatemethod_key)[1]
            old_second_how=object_sheet.cell_value(row_index,secondLocate_colNumber)
            #得到二次定位所需值
            secondLocateData_key=u"二次定位所需数据"
            secondLocateData_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(object_excel_path,"objname_locatemethod_locatedata",secondLocateData_key)[1]
            secondLocate_what=object_sheet.cell_value(row_index,secondLocateData_colNumber)
            new_second_how=locate_method_dict[old_second_how]

            second_located_element=CommonClass().locateElementIndirectly(br,new_first_how,old_what,new_second_how,secondLocate_what)

            OperateDealOrderObject.OperateDealOrderObject().operateLocatedElement(element,second_located_element)
