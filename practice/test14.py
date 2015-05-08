#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
br=webdriver.Firefox()
# br.maximize_window()
br.get("http://www.xebest.com:8000")
elements=br.find_elements_by_class_name("nav-arrow")
element1=elements[4]
if element1.is_displayed():
    print ("网站导航链接已定位到")
else:
    print ("网站导航元素未找到，请更换定位方式后重新定位")

# if br.find_element_by_xpath("//*[@id='topnav']/ul/li[5]/div[2]/ul[2]/li[2]/a").is_displayed():

# if br.find_element_by_css_selector("div#topnav>ul:first>li:nth(4)>div:nth(1)>ul:nth(1)>li(1)>a").is_displayed():
# if br.find_element_by_css_selector("li#all_menu>ul:nth(0)>li:nth(0)>a>span").is_displayed():
# if br.find_element_by_link_text(u"易支付").is_displayed():
#     print ("易支付元素已找到")
# else:
#     print("易支付元素未找到，请更换定位方式后重新定位")
# epay=br.find_element_by_css_selector("div#topnav>ul>li:nth(4)>div:nht(1)>ul:nth(1)>li(1)>a")
# epay=br.find_element_by_xpath("//*[@id='topnav']/ul/li[5]/div[2]/ul[2]/li[2]/a")
# epay=br.find_element_by_xpath("//*[@id='topnav']/ul/li[5]/div[2]/ul[2]/li[2]/a")
epay=br.find_element_by_link_text(u"易支付")
ActionChains(br).move_to_element(element1).click(element1).perform()
ActionChains(br).move_to_element(epay).click(epay).perform()