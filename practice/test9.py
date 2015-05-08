# encoding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support.select import Select
br=webdriver.Firefox()
# br.get("https://user.xebest.com:8443/loginAction!init.action")

br.get("http://www.xebest.com:8000")
br.maximize_window()
br.find_element_by_link_text("请登录").click()
br.find_element_by_id("userName").send_keys("wwg54421@163.com")
br.find_element_by_id("password").send_keys("wwg123456")
br.find_element_by_id("imgLogin").click()
# br.find_element_by_id("userName").send_keys('wwg54421@163.com')
# br.find_element_by_id("passWord").send_keys('wwg123456')
# br.find_element_by_id("checkCode").send_keys('12345')
# br.find_element_by_id('submit-btn').click()
time.sleep(4)
br.switch_to.alert.accept()
time.sleep(3)
br.find_element_by_css_selector('a.red').click()
time.sleep(2)
br.switch_to.window(br.window_handles[-1])
time.sleep(2)
br.find_element_by_link_text("我是供应商").click()
br.find_element_by_link_text("产品管理").click()
br.find_element_by_link_text(u"发布信息").click()
time.sleep(4)
WebDriverWait(br,10).until(lambda br:br.find_element_by_id("userItem")).click()#网站栏目选择
WebDriverWait(br,10).until(lambda br:br.find_element_by_link_text(u"供应信息")).click()
WebDriverWait(br,10).until(lambda br:br.find_element_by_xpath("//*[@id='seeUserItemsBody']/div[2]/div/ul/li/a")).click()
WebDriverWait(br,10).until(lambda br:br.find_element_by_css_selector("button.btn.selectOk")).click()
WebDriverWait(br,10).until(lambda br:br.find_element_by_id("newsItem")).click()#产品类别选择
time.sleep(5)
br.find_element_by_css_selector("a[Data-id='1000001008']").click()
time.sleep(2)
br.find_element_by_css_selector("a[Data-id='1000001008001']").click()
time.sleep(2)
br.find_element_by_css_selector("a[Data-id='1000001008001001']").click()
time.sleep(2)
br.find_element_by_xpath("//*[@id='seeNewsItemsBody']/div[3]/button").click()#产品类别选择对话框的确定按钮
br.find_element_by_id("infoTitle").send_keys("wwg")#产品标题
# br.find_element_by_id("infoFlag").send_keys("wwg")#关键词

br.find_element_by_id("proStandard").send_keys("wwg")#规格
br.find_element_by_id("proCompany").send_keys("wwg")#生产厂家
js1="$(\"input[Data-provide='datetimepicker'    ]\").removeAttr('readonly');$(\"input[Data-provide='datetimepicker']\").attr('value','2014-08-09')"
br.execute_script(js1)#生产日期
br.find_element_by_id("infoPrice").send_keys("1")#批发价
br.find_element_by_id("pricelast").send_keys("1")#零售价
br.find_element_by_id("infoCon").send_keys("2222")#供应量
br.find_element_by_id("proMinNum").send_keys("1")#最小起订量
br.find_element_by_id("province").find_element_by_css_selector("option[value=\"10008\"]").click()
br.find_element_by_id("city").find_element_by_css_selector("option[value=\"10009\"]").click()#发货地
time.sleep(3)
br.find_element_by_id("proDaysLimit").send_keys("1")#发货期限
time.sleep(2)
br.find_element_by_xpath("//*[@id='img_list']/p[1]/a/img").click()
time.sleep(2)
br.find_element_by_xpath("//div[@id='tabNavi']/ul/li[2]").click()
br.find_element_by_id("imgFile").send_keys("E:\\wwg\\xampp\\php\\php.gif")
time.sleep(4)
br.find_element_by_id("upToServer").click()#图片
br.find_element_by_id("infoBrief").send_keys("wwg")#产品简介
content="wwg"
js2="KE.text('infoContent','123wwg')"
br.execute_script(js2)#产品详情
js3="document.getElementsByClassName(\"ke-iframe\")[1].contentWindow.document.body.innerHTML=\"%s\"" %(content)
br.execute_script(js3)#配送说明
br.find_element_by_id('checkCode').send_keys('12345')
br.switch_to.window(br.window_handles[-1])
# br.find_element_by_id("saveBtn").click()


br.find_element_by_id("infoPublishForm").submit()
print br.find_element_by_xpath("//*[@id='infoPublishForm']/div[4]/div/ul/li[2]/span").text