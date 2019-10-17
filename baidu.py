from time import sleep, time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
url = 'https://www.baidu.com/'
driver.get(url)
action = ActionChains(driver)
# --------------------------元素操作--------------------------------
# 一、打开百度搜索小D课堂并登录后查找我的课堂进行播放
driver.find_element_by_id('kw').send_keys('163')
driver.find_element_by_id('su').click()
sleep(3)
# 进入课堂
# driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/h3/a/em').click()
driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/h3/a[1]').click()
sleep(5)
driver.find_element_by_xpath('//*div[@id="switchAccountLogin"]')
# driver.find_element_by_id('switchAccountLogin').click()
driver.find_element_by_id('auto-id-1571222370147').send_keys('saildf')
driver.find_element_by_id('auto-id-1571222370150').send_keys('anc11399232801')