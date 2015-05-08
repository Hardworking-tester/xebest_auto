# encoding:utf-8
import Browser
from selenium import webdriver
import unittest,time
from object import LocateRegisterObject
from Data import ReadExcel,get_number_by_data
from selenium.webdriver.common.by import By
from oracle import select
class Register(unittest.TestCase):

    def setUp(self):
        self.browser=Browser.Browser().init_browserByRegister()

    def getRegisterDataByTestcaseId(self,testcaseid):
        register_exclepath="F:\\pytest\\xebest-autotest\\Data\\register_data.xls"
        register_sheetname="register_data"
        register_sheet=ReadExcel.ReadExcel().getTableBySheetName(register_exclepath,register_sheetname)

        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(register_exclepath,register_sheetname,testcaseid)
        # email-address:邮箱地址,loginpassword:登录密码,reloginpassword:确认登录密码,phonenumber:手机号码,smscheckcode:短信验证码
        # picturecheckcode:图片验证码
        element_list=['email-address','loginpassword','reloginpassword','phonenumber','smscheckcode','picturecheckcode']
        register_data_list=[]

        col_index=2
        for i in range(element_list.__len__()):
            register_data_list.append(register_sheet.cell_value(row_col_number_list[0],(row_col_number_list[1])+col_index))
            col_index +=1

        return register_data_list


    def testRegisterSuccess(self):
        u"""正确数据注册邮箱"""
        testcaseid='case_0008'
        br=self.browser
        print testcaseid
        register_data_list=self.getRegisterDataByTestcaseId(testcaseid)
        LocateRegisterObject.LocateRegisterObject().getLocateObject(br,register_data_list)
        time.sleep(20)
        if self.assertIsEqual(testcaseid):
            print (u"通过页面验证确认注册成功")
        else:
            print (u"通过页面验证确认未注册成功")
        count_data=self.assertByOracle(register_data_list)
        if count_data>=1:
            print (u"通过数据库查询确认注册成功了")
        else:
            print (u"通过数据库查询确认注册没有成功")
        br.get_screenshot_as_file("F:\\testresult\\image_SUCCESSRegister.png")
        print ("image_SUCCESSRegister.png")


    def testRegisterFailedWithErrorEmailFormat(self):
        u"""邮箱地址格式错误时注册用户"""
        testcaseid='case_0009'
        br=self.browser
        print testcaseid
        register_data_list=self.getRegisterDataByTestcaseId(testcaseid)
        LocateRegisterObject.LocateRegisterObject().getLocateObject(br,register_data_list)
        time.sleep(20)
        if not(self.assertIsEqual(testcaseid)):
            print (u"通过页面验证确认未注册成功")
        else:
            print (u"注册功能出现bug了")

        count_data=self.assertByOracle(register_data_list)
        if count_data>=1:
            print (u"通过数据库查询确认注册成功了，但是注册功能出问题了")
        else:
            print (u"通过数据库查询确认注册没有成功，注册功能正常")
        br.get_screenshot_as_file("F:\\testresult\\image_FailedWithErrorEmailFormat.png")
        print ("image_FailedWithErrorEmailFormat.png")

    def testRegisterFailedWithErrorEmailFormatAndExistPhone(self):
        u"""邮箱地址格式错误,手机号已存在时注册用户"""
        testcaseid='case_0010'
        br=self.browser
        print testcaseid
        register_data_list=self.getRegisterDataByTestcaseId(testcaseid)
        LocateRegisterObject.LocateRegisterObject().getLocateObject(br,register_data_list)
        time.sleep(20)
        if not(self.assertIsEqual(testcaseid)):
            print (u"通过页面验证确认未注册成功")
        else:
            print (u"注册功能出现bug了")

        count_data=self.assertByOracle(register_data_list)
        if count_data>=1:
            print (u"通过数据库查询确认注册成功了，但是注册功能出问题了")
        else:
            print (u"通过数据库查询确认注册没有成功，注册功能正常")
        br.get_screenshot_as_file("F:\\testresult\\image_FailedWithErrorEmailFormatAndExistPhone.png")
        print ("image_FailedWithErrorEmailFormatAndExistPhone.png")

    def testRegisterFailedWithErrorSmscheckcode(self):
        u"""短信验证码错误时注册用户"""
        testcaseid='case_0011'
        br=self.browser
        print testcaseid
        register_data_list=self.getRegisterDataByTestcaseId(testcaseid)
        LocateRegisterObject.LocateRegisterObject().getLocateObject(br,register_data_list)
        time.sleep(20)
        if not(self.assertIsEqual(testcaseid)):
            print (u"通过页面验证确认未注册成功")
        else:
            print (u"注册功能出现bug了")

        count_data=self.assertByOracle(register_data_list)
        if count_data>=1:
            print (u"通过数据库查询确认注册成功了，但是注册功能出问题了")
        else:
            print (u"通过数据库查询确认注册没有成功，注册功能正常")

        br.get_screenshot_as_file("F:\\testresult\\image_FailedWithErrorSmscheckcode.png")
        print ("image_FailedWithErrorSmscheckcode.png")


    def assertByOracle(self,register_data_list):
        """
        通过数据库查询判断会员是否注册成功，并且返回查询到的结果总数
        """
        sql="select qy.* from yydscs.csm_user_info qy where qy.login_name="
        count_data=select.SelectFromOracle().selectFromOracleWithoutChineseWord(sql=sql,key=register_data_list[0])
        return count_data

    def assertIsEqual(self,testcaseid):

        """
        通过断言判断错误提示是否和期望的一致，并且通过查询界面的元素是否出现以及元素的文本值去判断（通过界面）是否注册成功。如果查询到注册成功的标记则返回true
        ，否则返回false
        """
        assertmessage_exclepath="F:\\pytest\\xebest-autotest\\Data\\register_data.xls"
        assertmessage_sheetname="assert_message"
        assertmessage_sheet=ReadExcel.ReadExcel().getTableBySheetName(assertmessage_exclepath,assertmessage_sheetname)
        rows=assertmessage_sheet.nrows
        for i in range(1,rows):
            if testcaseid in assertmessage_sheet.cell_value(i,0):
                time.sleep(3)
                if self.browser.find_element_by_xpath(assertmessage_sheet.cell_value(i,3)).text !=assertmessage_sheet.cell_value(i,4):
                    print u"页面提示语：%s" %(self.browser.find_element_by_xpath(assertmessage_sheet.cell_value(i,3)).text)+"\t"+u"和预期的提示语：%s：不相等" %(assertmessage_sheet.cell_value(i,4))

                self.assertEqual(self.browser.find_element_by_xpath(assertmessage_sheet.cell_value(i,3)).text,assertmessage_sheet.cell_value(i,4),msg="not equal")
            else:
                continue

        if self.browser.find_element_by_xpath("//a[@class='btn-red']/span").is_displayed() and self.browser.find_element_by_xpath("//a[@class='btn-red']/span").text==u">>去邮箱激活":
            return True
        else:
            return False

    def tearDown(self):
        self.browser.close()

