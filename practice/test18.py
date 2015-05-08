#encoding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

br=webdriver.Firefox()
br.get("http://www.ha.10086.cn/hmall/index.do")
time.sleep(5)
element1=br.find_element_by_class_name("list01")

ActionChains(br).move_to_element(element1).perform()
time.sleep(5)
element2=br.find_element_by_link_text("50-99")
if element2.is_displayed():
    print "元素已找到"
    element2.click()
    # element2.send_keys(Keys.ENTER)
else:
    print "元素未找到"


