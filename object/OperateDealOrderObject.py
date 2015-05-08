#encoding:utf-8
from Data import ReadExcel,get_number_by_data
import time
class OperateDealOrderObject():


    def getOperateMethod(self):
        pass
    def operateLocatedElement(self,element,located_element):
        element=element
        located_element=located_element
        excel=ReadExcel.ReadExcel()
        operate_excel_path="F:\\pytest\\xebest-autotest\\Data\\deal_order.xls"
        operate_excel_sheet=excel.getTableBySheetName(operate_excel_path,"operate_method")
        #得到当前操作的元素在操作方式表中所在行
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operate_excel_path,"operate_method",element)[0]
        #得到操作方式所在列
        operateMethod_value=u"操作方式"
        col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operate_excel_path,"operate_method",operateMethod_value)[1]

        operateMethod=operate_excel_sheet.cell_value(row_index,col_index)

        if operateMethod=="click":
            located_element.click()
            time.sleep(3)
