#encoding:utf-8
from selenium import webdriver
import time
from Action import PublicLogin
br=PublicLogin.PublicLogin().publicLoginByCustomer()
# br.maximize_window()
br.find_element_by_css_selector("input.wenben").send_keys(u"牛肉7")
br.find_element_by_css_selector("input.sousuo").click()
time.sleep(5)
# br.find_element_by_css_selector("a[href='sell-show-5203.html']").click()
br.find_element_by_css_selector("a[title='牛肉7']").click()
time.sleep(5)

br.switch_to_window(br.window_handles[1])

# br.find_element_by_xpath("//*[@class='row row-last p-quote']/a/img").click()
# br.find_element_by_xpath("html/body/div[9]/div[1]/div/div[2]/div/div[2]/div[5]/a/img").click()
br.find_element_by_xpath("//*[@class='row row-last p-quote']/a/img").click()
time.sleep(3)
br.find_element_by_id("orderPrice").send_keys("10")
br.find_element_by_id("orderNum").send_keys("10")
br.find_element_by_id("deliveryTime").find_element_by_css_selector("option[value='08:00-10:00']").click()
br.find_element_by_id("info").send_keys("wwg")
br.find_element_by_id("orderButton").click()
print br.switch_to_alert().text
br.switch_to_alert().accept()

br.close()
br.switch_to_window(br.window_handles[0])
br.close()