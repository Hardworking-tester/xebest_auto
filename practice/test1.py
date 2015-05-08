# encoding:utf-8
from selenium import webdriver
import time,unittest
from selenium.webdriver.support.ui import WebDriverWait
class TT1(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.get("http://www.xebest.com:8000")


    def testTea1(self):
        br=self.browser
        br.maximize_window()
        br.find_element_by_link_text(u"请登录").click()
        time.sleep(2)
        br.find_element_by_id('userName').send_keys('wwg54421@163.com')
        # br.implicitly_wait(5)
        time.sleep(2)
        br.find_element_by_id('password').send_keys('wwg123456')
        br.find_element_by_id('imgLogin').click()
        time.sleep(2)
        # print br.switch_to.alert.text
        br.switch_to.alert.accept()
        time.sleep(5)
        br.find_element_by_css_selector('a.red').click()
        time.sleep(4)
        br.switch_to.window(br.window_handles[1])
        time.sleep(4)
        br.refresh()
        br.find_element_by_link_text('我是供应商').click()
        time.sleep(4)
        br.find_element_by_link_text(u'产品管理').click()
        br.find_element_by_link_text(u'发布信息').click()
        br.implicitly_wait(4)
        br.find_element_by_id('userItem').click()
        br.find_element_by_link_text(u"供应信息").click()
        br.find_element_by_css_selector("button.btn.selectOk").click()
        br.find_element_by_id('newsItem').click()
        br.find_elements_by_css_selector('a.parent.rootClass')[0].click()
        time.sleep(2)
        br.find_element_by_css_selector("a[data-id='1000001008001']").click()
        time.sleep(2)
        br.find_element_by_css_selector("a[data-id='1000001008001001']").click()
        time.sleep(2)
        br.find_element_by_xpath("//div[@id='seeNewsItemsBody']/div[3]/button").click()
        time.sleep(3)
        br.find_element_by_id('infoTitle').send_keys('wwg')
        br.find_element_by_id('infoFlag').send_keys('wwg')
        data=br.find_element_by_id('proBrandName').find_elements_by_tag_name('option')
        print data.__len__()
        br.find_element_by_id('proBrandName').find_element_by_css_selector("option[value='LG']").click()

        br.find_element_by_id('proStandard').send_keys('wwg')
        br.find_element_by_id('proCompany').send_keys('zp')
        js1="$(\"input[data-provide='datetimepicker']\").removeAttr('readonly');$(\"input[data-provide='datetimepicker']\").attr('value','2014-10-10')"
        br.execute_script(js1)
        br.find_element_by_id('proLife').send_keys('4')
        br.find_element_by_id('proLifeUnit').find_element_by_css_selector("option[value='月']").click()
        br.find_element_by_id('proStorage').send_keys('wwg')
        br.find_element_by_id('proLicense').send_keys('wwg')
        br.find_element_by_id('proStandarNo').send_keys('wwg')
        br.find_element_by_id('proContry').find_element_by_css_selector("option[value='104']").click()
        br.find_element_by_id('proPriceUnit').find_element_by_css_selector("option[value='件']").click()
        br.find_element_by_id('infoPrice').send_keys('10')
        br.find_element_by_id('pricelast').send_keys('10')
        br.find_element_by_id('infoCon').send_keys('10')
        br.find_element_by_id('proMinNum').send_keys('10')
        br.find_element_by_id('province').find_element_by_css_selector("option[value='10066']").click()
        br.find_element_by_id('city').find_element_by_css_selector("option[value='10075']").click()
        br.find_element_by_id('proDaysLimit').send_keys('6')
        picture_path='F:\\picture\\screenshot.jpg'
        br.find_element_by_xpath("//*[@id='img_list']/p/a/img").click()
        br.find_element_by_xpath("//*[@id='tabNavi']/ul/li[2]").click()
        br.find_element_by_id('imgFile').send_keys(picture_path)
        br.find_element_by_id('upToServer').click()
        br.find_element_by_id('infoBrief').send_keys('wwg')
        js2="document.getElementsByClassName('ke-iframe')[0].contentWindow.document.body.innerHTML=\"%s\" " %(u'王伟高')
        br.execute_script(js2)

        js3="document.getElementsByClassName('ke-iframe')[1].contentWindow.document.body.innerHTML=\"%s\" " %(u'放风筝')
        br.execute_script(js3)



        time.sleep(10)
    def tearDown(self):
        pass


if __name__=='__main__':
    unittest.main()
