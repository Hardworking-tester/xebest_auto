#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from Data import ReadExcel,get_number_by_data
from PublicMethod import LocateElementCommonClass
class LocateSendGoodsObject():


    def getLocateElement(self):
        excel=ReadExcel.ReadExcel()
        element_excel_path="F:\\pytest\\xebest-autotest\\Data\\send_goods.xls"
        element_sheet=excel.getTableBySheetName(element_excel_path,"objname_locatemethod_locatedata")
        rows=element_sheet.nrows
        element_data_list=[]
        for i in range(1,rows):
            element_data_list.append(element_sheet.cell_value(i,0))

        for element in element_data_list:
            self.getLocateMethodAndData(element)

    def getLocateMethodAndData(self,element):
        excel=ReadExcel.ReadExcel()
        element_excel_path="F:\\pytest\\xebest-autotest\\Data\\send_goods.xls"
        element_sheet=excel.getTableBySheetName(element_excel_path,"objname_locatemethod_locatedata")

        #得到元素所在行号
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(element_excel_path,"objname_locatemethod_locatedata",element)[0]

        #得到定位方式所在列号
        locate_method_key=u"定位方式简述"
        locate_method_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(element_excel_path,"objname_locatemethod_locatedata",locate_method_key)[1]

        #得到定位所需数据所在列号
        locate_data_key=u"定位所需数据"
        locate_data_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(element_excel_path,"objname_locatemethod_locatedata",locate_data_key)[1]
        #得到元素是否需要二次定位的标志
        second_locate=u"是否需要二次定位"
        is_second_locate=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(element_excel_path,'objname_locatemethod_locatedata',second_locate)[1]

        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT,'classname':By.CLASS_NAME}
        old_first_how=element_sheet.cell_value(row_index,locate_method_col_index)
        what=element_sheet.cell_value(row_index,locate_data_col_index)
        new_first_how=locate_method_dict[old_first_how]
        judgeIsSecondLocate_flag=LocateElementCommonClass.CommonClass().judgeSecondLocateElement(is_second_locate)

        if not(judgeIsSecondLocate_flag):
            pass


pp=LocateSendGoodsObject()
pp.getLocateElement()