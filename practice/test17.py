#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
br=webdriver.Firefox()
br.get("http://www.ha.10086.cn/hmall/index.do")
time.sleep(5)
above=br.find_element_by_link_text(u"我的商城")
ActionChains(br).move_to_element(above).perform()
time.sleep(5)
# element2=br.find_element_by_link_text(u"登录")
element2=br.find_element_by_xpath("//div[@id='Loghtml']/a")
if element2.is_displayed():
    print "元素已找到"
    element2.click()
    # element2.send_keys(Keys.ENTER)
else:
    print "元素未找到"
