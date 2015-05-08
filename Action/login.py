# encoding:utf-8
from selenium import  webdriver
from Data import ReadExcel
from Data import get_number_by_data
from object import LocateLoginObject
import Browser,unittest
import time
from resultlog import ResultLog
class Login(unittest.TestCase):


    def setUp(self):
        self.browser=Browser.Browser().init_browser()

    def getUsernameAndPasswordByTestcaseid(self,testcaseid):
        """根据传递过来得testcaseid去拿到用户名、密码、弹出框内容"""
        excel=ReadExcel.ReadExcel()
        testcase_excelpath="F:\\pytest\\xebest-autotest\\Data\\login_data.xls"
        testcase_sheet=excel.getTableBySheetName(testcase_excelpath,"username_password_data")
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(testcase_excelpath,"username_password_data",testcaseid)
        data_list=[]
        user_name=testcase_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+2)
        pass_word=testcase_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+3)
        alert_message=testcase_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+4)
        data_list.append(user_name)
        data_list.append(pass_word)
        data_list.append(alert_message)

        return data_list


    def testNullUsername(self):
        u"""用户名为空的测试用例"""
        testcaseid='case_0002'
        print testcaseid
        data_list=self.getUsernameAndPasswordByTestcaseid(testcaseid)
        username=data_list[0]
        password=data_list[1]
        alertmessage=data_list[2]
        LocateLoginObject.LocateLoginObject().getLocateObject(self.browser,username,password,alertmessage)
        self.dealAlert(alertmessage)
        self.browser.get_screenshot_as_file("F:\\testresult\\image_NULLusername.png")
        print("image_NULLusername.png")

    def testNotExistUsername(self):
        u"""用户名不存在的测试用例"""
        testcaseid='case_0001'
        print testcaseid
        data_list=self.getUsernameAndPasswordByTestcaseid(testcaseid)
        username=data_list[0]
        password=data_list[1]
        alertmessage=data_list[2]
        LocateLoginObject.LocateLoginObject().getLocateObject(self.browser,username,password,alertmessage)
        self.dealAlert(alertmessage)
        self.browser.get_screenshot_as_file("F:\\testresult\\image_NOTExistUser.png")
        print("image_NOTExistUser.png")

    def testErrorPassword(self):
        u"""密码错误的测试用例"""
        testcaseid='case_0003'
        print testcaseid
        data_list=self.getUsernameAndPasswordByTestcaseid(testcaseid)
        username=data_list[0]
        password=data_list[1]
        alertmessage=data_list[2]
        LocateLoginObject.LocateLoginObject().getLocateObject(self.browser,username,password,alertmessage)

        self.dealAlert(alertmessage)
        self.browser.get_screenshot_as_file("F:\\testresult\\image_ERRORPassword.png")
        print("image_ERRORPassword.png")

    def testSuccessLogin(self):
        u"""登录成功的测试用例"""
        testcaseid='case_0004'
        print testcaseid
        data_list=self.getUsernameAndPasswordByTestcaseid(testcaseid)
        username=data_list[0]
        password=data_list[1]
        alertmessage=data_list[2]
        LocateLoginObject.LocateLoginObject().getLocateObject(self.browser,username,password,alertmessage)

        self.dealAlert(alertmessage)
        self.browser.get_screenshot_as_file("F:\\testresult\\image_SUCCESSLogin.png")
        print("image_SUCCESSLogin.png ")



    def dealAlert(self,alertmessage):
        """处理弹出框"""
        #为弹出框增加断言
        print (u"弹出框内容为：%s" %self.browser.switch_to_alert().text)
        print (u"预期弹出框内容为：%s" %alertmessage)
        self.assertEqual(alertmessage,self.browser.switch_to_alert().text,msg='the alert message is not equal with expection')
        #捕获弹出框异常并打印到测试报告中
        try:
            self.browser.switch_to_alert().accept()
        except:
            print(u"没有找到弹出框")
    def tearDown(self):
        self.browser.close()