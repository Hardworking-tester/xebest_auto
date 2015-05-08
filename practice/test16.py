#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("http://www.xebest.com:8000")
time.sleep(4)
above=driver.find_element_by_link_text(u"网站导航")
ActionChains(driver).move_to_element(above).perform()
time.sleep(10)
element2=driver.find_element_by_link_text(u"易支付")
# element2=driver.find_element_by_xpath("//*[@id='topnav']/ul/li[5]/div[2]/ul[2]/li[2]/a")
# element2=driver.find_element_by_css_selector("ul.clearfix>li:nth(1)>a:first")
if element2.is_displayed():
    print "元素已找到"
else:
    print "元素未找到"
element2.send_keys(Keys.ENTER)



