#encoding:utf-8
import os
import sys,xlrd
from selenium.webdriver.common.by import By
from Data import ReadExcel,get_number_by_data
from Action import Browser
import time,OperateAddProductElement
from Action import PublicLogin
from selenium.webdriver.support.ui import WebDriverWait
class LocateAddProductObject():
    #该类主要是去定位发布产品功能中所用到的元素
    def getLocateObject(self,testcaseid,browser,data_list):
        """循环需要定位的元素，拿到一个元素之后去调用getLocatMethodAndData方法，取得元素的定位方式以及定位所需数据"""

        browser=browser
        excel=ReadExcel.ReadExcel()
        object_excelpath="F:\\pytest\\xebest-autotest\\Data\\addProduct_data.xls"
        object_sheet=excel.getTableBySheetName(object_excelpath,"objname_locatemethod_locatedata")
        object_sheet_rows=object_sheet.nrows
        object_name_list=[]#得到需要定位的元素的名称的列表

        for i in range(object_sheet_rows):#拿到发布产品功能中需要定位的对象名称列表
            object_name_list.append(object_sheet.cell(i,0).value)
        object_name_list.pop(0)#去掉对象名excel中的第一行的标签项名称
        #循环需要定位的元素，拿到一个元素之后去调用getLocatMethodAndData方法，取得元素的定位方式以及定位所需数据
        for object_name in object_name_list:
            if self.judgeElementIsOperate(testcaseid,object_name):
                self.getLocateMethodAndData(browser,object_name,data_list)
            else:
                print object_name+u":元素在本次测试中没有进行操作"

    def judgeElementIsOperate(self,caseId,objectName):

        """
        判断该元素是否需要操作
        """
        excel=ReadExcel.ReadExcel()
        judge_excelpath="F:\\pytest\\xebest-autotest\\Data\\addProduct_data.xls"
        judge_sheet=excel.getTableBySheetName(judge_excelpath,"isoperateElement")
        judge_sheet_rows=judge_sheet.nrows

        #得到caseid所在的列号
        row_col_number_list1=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(judge_excelpath,"isoperateElement",caseId)
        colNumber=row_col_number_list1[1]
        #得到元素所在的行号
        row_col_number_list2=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(judge_excelpath,"isoperateElement",objectName)
        rowNumber=row_col_number_list2[0]
        if judge_sheet.cell_value(rowNumber,colNumber)=="Y":
            return True
        else:
            return False


    def getLocateMethodAndData(self,browser,object_name,data_list):
        """根据需要定位的元素的名称得到需要定位的元素的定位方式以及定位数据"""
        obj_name=object_name
        br=browser
        locate_method_data_excelpath="F:\\pytest\\xebest-autotest\\Data\\addProduct_data.xls"
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(locate_method_data_excelpath,"objname_locatemethod_locatedata",obj_name)#获得需要定位的元素名称所在的行和列
        excel=ReadExcel.ReadExcel()
        locate_method_data_sheet=excel.getTableBySheetName(locate_method_data_excelpath,"objname_locatemethod_locatedata")
        old_how=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+1)#获得excel中存储的定位方式
        what=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+2)#获得excel中存储的定位数据
        first_oneOrMore=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+3)#取得标记位以供判断是需要多次定位的元素在第一次定位时是定位一个元素还是定位多个元素
        second_oneOrMore=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+8)#取得标记位以供判断是需要多次定位的元素在第二次定位时是定位一个元素还是定位多个元素
        second_locate_flag=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+5)#取得标记位以供判断元素是否需要二次定位
        #在这里增加一个字典是因为如果直接把By.ID写在excel里的话，取出来不能用
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        #通过判断second_locate_flag的值，如果是N的话就表示不需要进行二次判断，那么直接使用定位元素并且定位的直接方式进行
        if second_locate_flag=='N':
            if old_how=='linktext':
                new_how=locate_method_dict["linktext"]
                #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
                self.locateElement(br,new_how,what,obj_name,data_list)
            elif old_how=='id':
                new_how=locate_method_dict['id']
                #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
                self.locateElement(br,new_how,what,obj_name,data_list)
            elif old_how=='css':
                new_how=locate_method_dict["css"]
                if first_oneOrMore=='element':
                    self.locateElement(br,new_how,what,obj_name,data_list)
                elif first_oneOrMore=='elements':
                    elements_index=int(locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+4))
                    self.locateElements(br,new_how,what,elements_index,obj_name,data_list)
            elif old_how=='xpath':
                new_how=locate_method_dict["xpath"]
                #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
                self.locateElement(br,new_how,what,obj_name,data_list)
            elif old_how=='js':

                #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
                self.locateElementByJs(br,what,obj_name,data_list)

            # elif old_how=='switchwindow':
            #     self.switchWindow(br,int(what),object_name,data_list)




        #通过判断second_locate_flag的值，如果是Y的话就表示需要进行二次判断，那么需要两次定位才能定位到该元素
        elif second_locate_flag=='Y':
            second_how=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+6)#得到二次定位的方式
            second_what=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+7)#得到二次定位所需的定位数据
            if old_how=='linktext':
                new_how=locate_method_dict["linktext"]
                #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
                self.locateElementFirst(br,new_how,what,obj_name,data_list,second_how,second_what,first_oneOrMore,locate_method_data_sheet,row_col_number_list)
            elif old_how=='id':
                new_how=locate_method_dict['id']
                #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
                self.locateElementFirst(br,new_how,what,obj_name,data_list,second_how,second_what,first_oneOrMore,locate_method_data_sheet,row_col_number_list)
            elif old_how=='css':
                new_how=locate_method_dict["css"]
                if first_oneOrMore=='element':
                    self.locateElementFirst(br,new_how,what,obj_name,data_list,second_how,second_what,first_oneOrMore,locate_method_data_sheet,row_col_number_list)
                elif first_oneOrMore=='elements':
                    first_elements_index=int(locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+4))
                    self.locateElmentsFirst(br,new_how,what,first_elements_index,obj_name,data_list,second_how,second_what,first_oneOrMore,second_oneOrMore,locate_method_data_sheet,row_col_number_list)
            elif old_how=='xpath':
                new_how=locate_method_dict["xpath"]
                #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
                self.locateElementFirst(br,new_how,what,obj_name,data_list,second_how,second_what,second_oneOrMore,locate_method_data_sheet,row_col_number_list)

    def locateElementFirst(self,browser,how,what,obj_name,data_list,second_how,second_what,oneOrAll,locate_method_data_sheet,row_col_number_list):
        #该方法作用：针对需要二次定位的元素,在此进行第一次定位
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        br=browser
        object_name=obj_name
        first_located_element=WebDriverWait(br,10).until(lambda br:br.find_element(by=how,value=what))
        if second_how=='linktext':
            second_new_how=locate_method_dict["linktext"]

            self.locateElementSecond(br,first_located_element,second_new_how,second_what,object_name,data_list)
        elif second_how=='id':
            second_new_how=locate_method_dict['id']

            self.locateElementSecond(br,first_located_element,second_new_how,second_what,object_name,data_list)
        elif second_how=='css':
            second_new_how=locate_method_dict["css"]
            if oneOrAll=='element':
                self.locateElementSecond(br,first_located_element,second_new_how,second_what,object_name,data_list)
            elif oneOrAll=='elements':
                elements_index=int(locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+4))
                self.locateElmentsSecond(br,first_located_element,second_new_how,second_what,elements_index,object_name,data_list)
        elif second_how=='xpath':
            second_new_how=locate_method_dict["xpath"]

            self.locateElementSecond(br,first_located_element,second_new_how,second_what,object_name,data_list)


    def locateElementSecond(self,br,first_located_element,second_new_how,second_what,object_name,data_list):
            #该方法针对需要二次定位的元素，在此进行第二次定位，并调用操作元素的方法
            br=br
            object_name=object_name
            second_located_element=WebDriverWait(first_located_element,10).until(lambda first_located_element:first_located_element.find_element(by=second_new_how,value=second_what))
            #调用操作元素的方法
            OperateAddProductElement.OperateElement().opermateAddProductElement(br,object_name,second_located_element,data_list)


    def locateElmentsFirst(self,br,new_how,what,first_elements_index,obj_name,data_list,second_how,second_what,first_oneOrAll,second_oneOrAll,locate_method_data_sheet,row_col_number_list):
        #该方法作用：需要定位的元素采用的是css定位方式，该元素需要经过两次定位，并且第一次需要定位的是一组元素的时候使用此方法
        br=br
        object_name=obj_name
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        first_located_element=WebDriverWait(br,10).until(lambda br:br.find_elements(by=new_how,value=what)[first_elements_index])
        if second_how=='linktext':
                second_new_how=locate_method_dict["linktext"]
                #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
                self.locateElementSecond(br,first_located_element,second_new_how,second_what,object_name,data_list)
        elif second_how=='id':
            second_new_how=locate_method_dict['id']
            #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
            self.locateElementSecond(br,first_located_element,second_new_how,second_what,object_name,data_list)
        elif second_how=='css':
            second_new_how=locate_method_dict["css"]
            if second_oneOrAll=='element':
                self.locateElementSecond(br,first_located_element,second_new_how,second_what,object_name,data_list)
            elif second_oneOrAll=='elements':
                second_elements_index=int(locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+9))
                self.locateElmentsSecond(br,first_located_element,second_new_how,second_what,second_elements_index,object_name,data_list)
        elif second_how=='xpath':
            second_new_how=locate_method_dict["xpath"]
            #调用定位元素方法，并传递给该方法一个定位方式，定位值，元素名称，用户名，密码，弹出框内容
            self.locateElementSecond(br,first_located_element,second_new_how,what,object_name,data_list)

    def locateElmentsSecond(self,br,first_located_element,second_new_how,second_what,second_elements_index,object_name,data_list):
        br=br
        object_name=object_name
        second_located_element=WebDriverWait(first_located_element,10).until(lambda first_located_element:first_located_element.find_elements(by=second_new_how,value=second_what)[second_elements_index])
        OperateAddProductElement.OperateElement().opermateAddProductElement(br,object_name,second_located_element,data_list)

    def locateElementByJs(self,br,js,obj_name,data_list):
        br.execute_script(js)

    # def switchWindow(self,br,windowIndex,obj_name,data_list):
#     br.switch_to.window(br.window_handles[windowIndex])

    def locateElement(self,browser,how,what,obj_name,data_list):
        #该方法作用：只针对一次定位可以定位到的元素，定位之后操作
        br=browser
        object_name=obj_name
        located_element=WebDriverWait(br,10).until(lambda br:br.find_element(by=how,value=what))
        #调用操作元素的方法
        OperateAddProductElement.OperateElement().opermateAddProductElement(br,object_name,located_element,data_list)



    def locateElements(self,browser,how,what,index,obj_name,data_list):
        br=browser
        object_name=obj_name
        located_element=WebDriverWait(br,10).until(lambda br:br.find_elements(by=how,value=what)[index])
        #调用操作元素的方法
        OperateAddProductElement.OperateElement().opermateAddProductElement(br,object_name,located_element,data_list)

