#encoding:utf-8
from Data import get_number_by_data,ReadExcel
import time
from PublicMethod import SmsCheckCode
from resultlog import ResultLog
class OperatePayByBalanceElement():

    def operatePayElement(self,element,located_element,send_data_list):
        log=ResultLog.ResultLog()
        excel=ReadExcel.ReadExcel()
        operate_excel_path="F:\\pytest\\xebest-autotest\\Data\\pay_by_balance.xls"
        operate_sheet=excel.getTableBySheetName(operate_excel_path,"operate_method")
        #得到操作方式所在列
        operate_method=u"操作方式"
        operate_method_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operate_excel_path,"operate_method",operate_method)[1]

        #得到元素所在行
        row_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operate_excel_path,"operate_method",element)[0]

        operate_method_flag=operate_sheet.cell_value(row_index,operate_method_col_index)

        if operate_method_flag=='click':
            try:
                located_element.click()
                time.sleep(3)
            except:
                print ("element:%s cannot operate" %element)
                raise ValueError("no element can operate")
            else:
                log.info("元素：%s 操作成功" %(element.encode('utf-8')))
        elif operate_method_flag=='sendkey' and element==u'CheckCodeInput':

            checkcode=SmsCheckCode.SmsCheckCode().getCheckCode()
            time.sleep(2)
            if checkcode:

                log.info("验证码获取成功，获取到的验证码为：%s" %(checkcode.encode('utf-8')))
            else:
                log.info("验证码获取失败")
            located_element.send_keys(checkcode)
        elif operate_method_flag=='sendkey' and element==u'PayPasswordInput':
            located_element.clear()
            located_element.send_keys(send_data_list[0])