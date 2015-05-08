#encoding:utf-8
from Data import ReadExcel,get_number_by_data
from selenium.webdriver.common.by import By
from selenium import webdriver
import OperateQuotePriceObject
from PublicMethod import LocateElementCommonClass
from resultlog.ResultLog import ResultLog
class LocateQuotePriceObject():

    def getLocateObject(self,testcaseId,browser,send_data_list):
        """得到需要定位的元素的列表"""
        testcaseId=testcaseId
        browser=browser
        send_data=send_data_list
        object_excelpath="F:\\pytest\\xebest-autotest\\Data\\quoteprice_data.xls"
        object_sheet=ReadExcel.ReadExcel().getTableBySheetName(object_excelpath,"objname_locatemethod_locatedata")
        rows=object_sheet.nrows
        object_data_list=[]
        for i in range(1,rows):
            object_data_list.append(object_sheet.cell_value(i,0))

        for element in object_data_list:
            if self.judgeElementIsOperate(testcaseId,element):
                self.getLocateMethodAndData(element,browser,send_data)
            else:
                print "元素:%s不需要被操作" %(element.encode('utf-8'))




    def judgeElementIsOperate(self,testcaseId,element):
        excel=ReadExcel.ReadExcel()
        judge_excelpath="F:\\pytest\\xebest-autotest\\Data\\quoteprice_data.xls"
        judge_sheet=excel.getTableBySheetName(judge_excelpath,"isoperateElement")
        #得到列号
        testcaseid_row_col_data_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(judge_excelpath,"isoperateElement",testcaseId)
        colNumber=testcaseid_row_col_data_list[1]
        #得到行号
        element_row_col_data_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(judge_excelpath,"isoperateElement",element)
        rowNumber=element_row_col_data_list[0]

        if judge_sheet.cell(rowNumber,colNumber).value=="Y":
            return True
        else:
            return False


    def getLocateMethodAndData(self,element,browser,send_data):
        browser=browser
        locate_object=element
        excel=ReadExcel.ReadExcel()
        locate_method_data_path="F:\\pytest\\xebest-autotest\\Data\\quoteprice_data.xls"
        locate_element_sheet=excel.getTableBySheetName(locate_method_data_path,"objname_locatemethod_locatedata")
        #得到需要定位的元素所在行
        locateObject_rowCol_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_method_data_path,"objname_locatemethod_locatedata",locate_object)
        rowNumber=locateObject_rowCol_number_list[0]
        #得到需要定位的元素的定位方式所在列
        locateMethod_Key=u"定位方式简述"
        locateMethod_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_method_data_path,"objname_locatemethod_locatedata",locateMethod_Key)[1]
        #得到需要定位的元素的定位数据所在列
        locateData_key=u"定位所需数据"
        locateData_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_method_data_path,"objname_locatemethod_locatedata",locateData_key)[1]
        #得到判断元素是否需要二次定位的判断条件所在列
        isSecondLocate_key=u"是否需要二次定位"
        SecondLocate_key_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_method_data_path,"objname_locatemethod_locatedata",isSecondLocate_key)[1]
        #存储从excel表中取出的定位方式和定位数据,以及判断是否需要二次定位的条件
        old_how=locate_element_sheet.cell_value(rowNumber,locateMethod_colNumber)
        old_what=locate_element_sheet.cell_value(rowNumber,locateData_colNumber)
        secondLocate=locate_element_sheet.cell_value(rowNumber,SecondLocate_key_colNumber)
        # old_how=locate_element_sheet.cell_value(rowNumber,locateMethod_colNumber).encode('utf-8')
        # old_what=locate_element_sheet.cell_value(rowNumber,locateData_colNumber).encode('utf-8')
        # print "元素%s的定位方式为:%s，定位数据为%s" %(element.encode('utf-8'),old_how,old_what)
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}


        #new_first_how=locate_method_dict[old_how]
        if not (LocateElementCommonClass.CommonClass().judgeSecondLocateElement(secondLocate)):

            if old_how=="switchHandle":
                index=int(old_what)
                LocateElementCommonClass.CommonClass().switchHandle(browser,index)
                # self.switchWindow(browser,index,locate_object)
            else:
                new_how=locate_method_dict[old_how]
                located_element=LocateElementCommonClass.CommonClass().findElement(browser,new_how,old_what)
                log=ResultLog()
                log.info("需要定位的元素为：%s，元素的定位方式为：%s，定位元素所需的数据为：%s" %(locate_object.encode('utf-8'),old_how.encode('utf-8'),old_what.encode('utf-8')))
                OperateQuotePriceObject.OperateQuotePriceObject().opermateQuotePriceElement(browser,located_element,locate_object,send_data)
                # self.locateElement(browser,new_how,old_what,locate_object,send_data)
        else:
            new_first_how=locate_method_dict[old_how]
            #得到二次定位方式的值所在列
            secondLocatemethod_key=u"二次定位的方式"
            secondLocate_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_method_data_path,"objname_locatemethod_locatedata",secondLocatemethod_key)[1]
            old_second_how=locate_element_sheet.cell_value(rowNumber,secondLocate_colNumber)
            #得到二次定位所需值
            secondLocateData_key=u"二次定位所需数据"
            secondLocateData_colNumber=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_method_data_path,"objname_locatemethod_locatedata",secondLocateData_key)[1]
            secondLocate_what=locate_element_sheet.cell_value(rowNumber,secondLocateData_colNumber)
            new_second_how=locate_method_dict[old_second_how]
            # self.locateElmentFirst(browser,new_first_how,old_what,locate_object,send_data,new_second_how,secondLocate_what)
            log=ResultLog()
            log.info("需要定位的元素为：%s，元素的定位方式为：%s，定位元素所需的数据为：%s" %(locate_object.encode('utf-8'),old_second_how.encode('utf-8'),secondLocate_what.encode('utf-8')))
            second_located_element=LocateElementCommonClass.CommonClass().locateElementIndirectly(browser,new_first_how,old_what,new_second_how,secondLocate_what)
            # print second_located_element
            OperateQuotePriceObject.OperateQuotePriceObject().opermateQuotePriceElement(browser,second_located_element,locate_object,send_data)

    # def judgeSecondLocateElement(self,secondLocate):
    #     """判断元素是否需要二次定位"""
    #     if secondLocate=="Y":
    #         return True
    #     else:
    #         return False


    # def locateElement(self,browser,new_how,old_what,locate_object,send_data):
    #     browser=browser
    #     how=new_how
    #     what=old_what
    #     located_element=browser.find_element(by=how,value=what)
    #     print locate_object
    #     OperateQuotePriceObject.OperateQuotePriceObject().opermateQuotePriceElement(browser,located_element,locate_object,send_data)


    # def locateElmentFirst(self,browser,new_first_how,old_what,locate_object,send_data,new_second_how,secondLocate_what):
    #     """此方法主要用于需要二次定位的元素进行第一次定位"""
    #     browser=browser
    #     how=new_first_how
    #     what=old_what
    #     first_located_element=browser.find_element(by=how,value=what)
    #     self.locateElementSecond(browser,locate_object,first_located_element,new_second_how,secondLocate_what,send_data)
    #
    # def locateElementSecond(self,browser,locate_object,first_located_element,new_second_how,secondLocate_what,send_data):
    #     """此方法主要用于需要二次定位的元素进行第二次定位"""
    #     second_located_element=first_located_element.find_element(by=new_second_how,value=secondLocate_what)
    #     OperateQuotePriceObject.OperateQuotePriceObject().opermateQuotePriceElement(browser,second_located_element,locate_object,send_data)

    # def switchWindow(self,browser,index,locate_object):
    #     browser.switch_to.window(browser.window_handles[index])


# pp=LocateQuotePriceObject()
# pp.getLocateObject()
# pp.judgeElementIsOperate()
# pp.getLocateMethodAndData()
