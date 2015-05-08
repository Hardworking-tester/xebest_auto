#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from object import *
from selenium.webdriver.support.wait import WebDriverWait
from resultlog.ResultLog import ResultLog
class CommonClass():

    def judgeSecondLocateElement(self,secondLocate):
        """判断元素是否需要二次定位"""
        if secondLocate=="Y":
            return True
        else:
            return False
    def findElement(self,browser,new_how,old_what,element):
        """定位元素"""
        log=ResultLog()
        browser=browser
        how=new_how
        what=old_what
        try:
            located_element=WebDriverWait(browser,20).until(lambda browser : browser.find_element(by=how,value=what))

        except Exception:
            log.info("元素：%s 定位失败" %(element.encode('utf-8')))
            print ("element: %s is not located" %element)
            raise NameError("element：%s is located filed" %element)
        else:
            log.info("元素：%s 已定位成功" %(element.encode('utf-8')))
            return located_element
        # print locate_object
        # OperateQuotePriceObject.OperateQuotePriceObject().opermateQuotePriceElement(browser,located_element,locate_object,send_data)


    def findElements(self):
        """定位元素组"""
        pass



    def locateElementIndirectly(self,browser,new_first_how,old_what,new_second_how,secondLocate_what):
        """处理需要经过父元素才能定位到的子元素"""
        browser=browser
        how=new_first_how
        what=old_what
        second_how=new_second_how
        second_what=secondLocate_what
        first_located_element=browser.find_element(by=how,value=what)
        def locateElementSecondly():
            second_located_element=first_located_element.find_element(by=second_how,value=second_what)
            return second_located_element
        return locateElementSecondly()


    def dealAlert(self,browser):
        """处理弹出框"""
        browser.switch_to.alert.accept()

    def executeJs(self):
        """处理页面需要执行js才能完成的功能"""
        pass

    def sendDataToRichText(self):
        """往富文本框内写内容"""
        pass

    def switchHandle(self,browser,index):
        """切换句柄"""
        browser.switch_to.window(browser.window_handles[index])

