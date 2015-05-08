# encoding:utf-8
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.command import Command
from selenium import webdriver
import time
br=webdriver.Firefox()
br.get("http://www.xebest.com:8000")
#
# print br.execute(Command.GET_TITLE)
br.find_element_by_link_text("请登录")
br.execute(Command.CLICK)
# br.find_element_by_link_text("请登录").click()
print br.find_element_by_id("userName").tag_name
# br.find_element_by_id("password").send_keys("wwg123456")
#
# br.find_element_by_id("imgLogin").click()
# time.sleep(4)
# tt=br.execute(Command.GET_ALERT_TEXT)
# br.execute(Command.ACCEPT_ALERT)
# print tt['value']
# print br.get_log("browser")
# print br.get_log("driver")
# print br.get_log("client")
# print br.get_log("server")
# br.get_screenshot_as_file("E:\\data\\dtt.png")