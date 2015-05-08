# encoding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command

br=webdriver.Firefox()
br.get("http://www.xebest.com:8000")
br.find_element_by_link_text("请登录").click()

# ActionChains(br).key_down(Keys.LEFT_CONTROL).send_keys("a").perform()
br.find_element_by_id('userName').send_keys('wwg74581@163.com')
ActionChains(br).send_keys(Keys.TAB).perform()
ActionChains(br).send_keys('wwg123456').perform()
br.find_element_by_id("imgLogin").click()
Command.ACCEPT_ALERT
# br.find_element_by_id('userName').send_keys(Keys.TAB)
# ActionChains(br).key_down(Keys.LEFT_SHIFT).send_keys(Keys.HOME).key_up(Keys.LEFT_SHIFT).perform()
# ActionChains(br).key_down(Keys.LEFT_CONTROL).send_keys("c").perform()
# br.find_element_by_id('userName').send_keys(Keys.TAB)
# Keys.TAB
# ActionChains(br).send_keys(Keys.TAB).perform()
# ActionChains(br).send_keys(Keys.TAB).perform()
# ActionChains(br).send_keys(Keys.ENTER).perform()