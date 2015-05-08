#encoding:utf-8
from selenium import webdriver
from Data import ReadExcel,get_number_by_data
class OperateSendGoodsElement():
    def getOperateMethod(self,element):
        excel=ReadExcel.ReadExcel()
        operateElement_excel_path="F:\\pytest\\xebest-autotest\\Data\\send_goods.xls"
        operateElement_sheet=excel.getTableBySheetName(operateElement_excel_path,"operate_method")

        #得到操作方式所在列
        operate_method_key=u"操作方式"
        operate_method_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operateElement_excel_path,"operate_method",operate_method_key)[1]

        #得到需要定位的元素所在的行号
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operateElement_excel_path,"operate_method",element)[1]
