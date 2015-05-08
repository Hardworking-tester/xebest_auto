#encoding:utf-8
from Data import ReadExcel,get_number_by_data
from selenium.webdriver.common.by import By
from selenium import webdriver
from PublicMethod import LocateElementCommonClass
import OperatePayByBalanceElement
class LocatePayByBalanceObject():

    def getLocateElementList(self,browser,testcaseId,send_data_list):
        caseid='case_0010'
        excel=ReadExcel.ReadExcel()
        element_path="F:\\pytest\\xebest-autotest\\Data\\pay_by_balance.xls"
        element_sheet=excel.getTableBySheetName(element_path,"objname_locatemethod_locatedata")
        rows=element_sheet.nrows
        #得到元素名称所在列
        element_name=u"元素名称"
        col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(element_path,"objname_locatemethod_locatedata",element_name)[1]
        element_list=[]
        for i in range(1,rows):
            element_list.append(element_sheet.cell_value(i,col_index))

        for element in element_list:

            if self.judgeElementIsLocate(element,caseid):
                self.getLoacteMethodAndData(browser,element,send_data_list)
                # print "元素：%s 需要被操作" %(element.encode('utf-8'))
            else:
                print "元素:%s 不需要被操作" %(element.encode('utf-8'))

    def judgeElementIsLocate(self,element,caseid):

        excel=ReadExcel.ReadExcel()
        element_path="F:\\pytest\\xebest-autotest\\Data\\pay_by_balance.xls"
        element_sheet=excel.getTableBySheetName(element_path,"isoperateElement")
        #得到测试用例id所在列号
        col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(element_path,"isoperateElement",caseid)[1]
        #得到需要定位的元素所在的行号
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(element_path,"isoperateElement",element)[0]
        locate_flag=element_sheet.cell_value(row_index,col_index)
        if locate_flag=='Y':
            return True
        else:
            return False

    def getLoacteMethodAndData(self,browser,element,send_data_list):
        excel=ReadExcel.ReadExcel()
        locate_element_path="F:\\pytest\\xebest-autotest\\Data\\pay_by_balance.xls"
        locate_element_sheet=excel.getTableBySheetName(locate_element_path,'objname_locatemethod_locatedata')
        #得到需要定位的元素所在的行号
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_element_path,'objname_locatemethod_locatedata',element)[0]
        #得到定位方式所在的列号
        locate_mehtod=u"定位方式简述"
        locate_method_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_element_path,'objname_locatemethod_locatedata',locate_mehtod)[1]
        #得到定位元素所需要的数据所在的列号
        locate_data=u"定位所需数据"
        locate_data_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_element_path,'objname_locatemethod_locatedata',locate_data)[1]
        #得到元素是否需要二次定位的标志
        second_locate=u"是否需要二次定位"
        is_second_locate=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_element_path,'objname_locatemethod_locatedata',second_locate)[1]

        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        old_locate_method=locate_element_sheet.cell_value(row_index,locate_method_col_index)
        what=locate_element_sheet.cell_value(row_index,locate_data_col_index)
        second_locate_flag=locate_element_sheet.cell_value(row_index,is_second_locate)
        new_locate_how=locate_method_dict[old_locate_method]
        if not(LocateElementCommonClass.CommonClass().judgeSecondLocateElement(second_locate_flag)):
            located_element=LocateElementCommonClass.CommonClass().findElement(browser,new_locate_how,what,element)
            OperatePayByBalanceElement.OperatePayByBalanceElement().operatePayElement(element,located_element,send_data_list)

        else:
            #得到二次定位方式的值所在列
            secondLocatemethod_key=u"二次定位的方式"
            secondLocate_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_element_path,"objname_locatemethod_locatedata",secondLocatemethod_key)[1]
            old_second_how=locate_element_sheet.cell_value(row_index,secondLocate_colNumber)
            #得到二次定位所需值
            secondLocateData_key=u"二次定位所需数据"
            secondLocateData_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_element_path,"objname_locatemethod_locatedata",secondLocateData_key)[1]
            secondLocate_what=locate_element_sheet.cell_value(row_index,secondLocateData_colNumber)
            new_second_how=locate_method_dict[old_second_how]

            second_located_element=LocateElementCommonClass.CommonClass().locateElementIndirectly(browser,new_locate_how,what,new_second_how,secondLocate_what)

            OperatePayByBalanceElement.OperatePayByBalanceElement().operatePayElement(element,second_located_element,send_data_list)


# pp=LocatePayByBalanceObject()
# pp.getLocateElementList()