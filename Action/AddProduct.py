# encoding:utf-8
import PublicLogin,unittest,time
from Data import get_number_by_data,ReadExcel
from object import LocateAddProductObject
from oracle import select
class AddProduct(unittest.TestCase):

    def setUp(self):
        self.browser=PublicLogin.PublicLogin().publicLoginByCustomerCenter()

    def getAddProductDataByTestcaseid(self,testcaseid):
        """根据传递过来得testcaseid去拿到发布产品所需要填写的内容"""
        excel=ReadExcel.ReadExcel()
        testcase_excelpath="F:\\pytest\\xebest-autotest\\Data\\addProduct_data.xls"
        testcase_sheet=excel.getTableBySheetName(testcase_excelpath,"addproduct_data")
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(testcase_excelpath,"addproduct_data",testcaseid)
        data_list=[]
        # product_title:产品标题,key_word:关键词,standard:规格,producter:生产厂家,quality_date:保质期,storage_conditions:存储条件
        # product_allow_id:生产许可证号,product_standard_id:产品标准号,shop_price:批发价,retail_price:零售价
        # supply_amount:供货量,min_amount:最小起订量,sendproduct_limit:发货期限,picture_path:图片地址,product_summary:产品简介,check_code:验证码
        element_list=['product_title','key_word','standard','producter','quality_date',
                      'storage_conditions','product_allow_id','product_standard_id',
                      'shop_price','retail_price','supply_amount','min_amount','sendproduct_limit',
                      'picture_path','product_summary','check_code']
        col_index=2
        for i in range(element_list.__len__()):
            element_list[i]=testcase_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+col_index)
            col_index += 1
        for index in range(element_list.__len__()):
            data_list.append(element_list[index])
        return data_list

    def testAddProductSuccess(self):
        u"""测试正确数据发布产品功能"""

        testcaseid='case_0005'
        print testcaseid
        data_list=self.getAddProductDataByTestcaseid(testcaseid)

        sql="select dd.* from yydscs.IMS_NEWS dd where dd.title="
        old_dataCount=select.SelectFromOracle().selectFromOracle(sql,data_list[0])

        LocateAddProductObject.LocateLoginObject().getLocateObject(testcaseid,self.browser,data_list)

        time.sleep(4)
        self.browser.get_screenshot_as_file("F:\\testresult\\image_SUCCESSaddProduct.png")
        print("image_SUCCESSaddProduct.png ")


        new_dataCount=select.SelectFromOracle().selectFromOracle(sql,data_list[0])
        if new_dataCount>old_dataCount:
            print (u"通过数据库查询到产品发布成功")
        else:
            print(u"通过数据库查询到产品发布失败")

        print (u"断言判定马上就要开始了---------------------------")
        #调用断言判断在前台页面判断产品是否发布成功
        self.assertMethod(data_list,self.browser.current_url)

    def testAddProductWithoutKeyword(self):
        u"""测试不输入关键词进行发布产品功能"""

        testcaseid='case_0006'
        print testcaseid
        data_list=self.getAddProductDataByTestcaseid(testcaseid)

        sql="select dd.* from yydscs.IMS_NEWS dd where dd.title="
        old_dataCount=select.SelectFromOracle().selectFromOracle(sql,data_list[0])

        LocateAddProductObject.LocateLoginObject().getLocateObject(testcaseid,self.browser,data_list)

        time.sleep(4)
        self.browser.get_screenshot_as_file("F:\\testresult\\image_addProductFailedWithoutKeyword.png")
        print("image_addProductFailedWithoutKeyword.png ")

        new_dataCount=select.SelectFromOracle().selectFromOracle(sql,data_list[0])
        if new_dataCount>old_dataCount:
            print (u"通过数据库查询到产品发布成功")
        else:
            print(u"通过数据库查询到产品发布失败")

    def testAddProductWithoutWebsiteItem(self):
            u"""测试不选择栏目进行发布产品功能"""

            testcaseid='case_0007'
            print testcaseid
            data_list=self.getAddProductDataByTestcaseid(testcaseid)

            sql="select dd.* from yydscs.IMS_NEWS dd where dd.title="
            old_dataCount=select.SelectFromOracle().selectFromOracle(sql,data_list[0])

            LocateAddProductObject.LocateAddProductObject().getLocateObject(testcaseid,self.browser,data_list)

            time.sleep(4)
            self.browser.get_screenshot_as_file("F:\\testresult\\image_addProductFailedWithoutWebsiteItem.png")
            print("image_addProductFailedWithoutWebsiteItem.png ")

            new_dataCount=select.SelectFromOracle().selectFromOracle(sql,data_list[0])
            if new_dataCount>old_dataCount:
                print (u"通过数据库查询到产品发布成功")
            else:
                print(u"通过数据库查询到产品发布失败")

    def assertMethod(self,data_list,currentURL):

        """

        通过断言在前台页面判断产品是否发布成功
        """
        #产品发布完成后跳转的页面
        successUrl="https://user.xebest.com:8443/site/infogymanager!list.action?infoType=2"
        self.assertEqual(currentURL,successUrl,msg="the url whitch successurl is not equal with currenturl")
        if self.browser.find_element_by_xpath("//tbody[@id='ids-group']/tr[1]/td[2]/a").is_displayed() and self.browser.find_element_by_xpath("//tbody[@id='ids-group']/tr[1]/td[2]/a").text==data_list[0]:
            print (u"通过页面查找元素判断产品发布成功")
        else:
            print (u"通过页面查找元素判断产品没有发布成功")



    def tearDown(self):
        self.browser.close()





