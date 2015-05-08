# encoding:utf-8
from Data import ReadExcel,get_number_by_data
class OperateRegisterElement():



    def operateElement(self,register_data_list,objname,located_element):
        assertmessage_exclepath="F:\\pytest\\xebest-autotest\\Data\\register_data.xls"
        assertmessage_sheetname="assert_message"

        operate_method=self.getOperateMethod(objname)
        if operate_method=="click":

            located_element.click()
        elif operate_method=="sendkey" and objname==u"邮箱地址":

            located_element.clear()
            located_element.send_keys(register_data_list[0])

        elif operate_method=="sendkey" and objname==u"登录密码":

            located_element.clear()
            located_element.send_keys(register_data_list[1])

        elif operate_method=="sendkey" and objname==u"确认登录密码":

            located_element.clear()
            located_element.send_keys(register_data_list[2])

        elif operate_method=="sendkey" and objname==u"手机号码":

            located_element.clear()
            located_element.send_keys(register_data_list[3])

        elif operate_method=="sendkey" and objname==u"短信验证码":

            located_element.clear()
            located_element.send_keys(int(register_data_list[4]))

        elif operate_method=="sendkey" and objname==u"图片验证码":

            located_element.clear()
            located_element.send_keys(int(register_data_list[5]))

        # elif operate_method=="Gettext":
        #
        #
        #     located_element.text


    def getOperateMethod(self,objname):

            register_exclepath="F:\\pytest\\xebest-autotest\\Data\\register_data.xls"
            register_sheetname="operate_method"
            register_sheet=ReadExcel.ReadExcel().getTableBySheetName(register_exclepath,register_sheetname)
            row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(register_exclepath,register_sheetname,objname)
            element_operate_method=register_sheet.cell_value(row_col_list[0],(row_col_list[1]+1))
            return  element_operate_method
