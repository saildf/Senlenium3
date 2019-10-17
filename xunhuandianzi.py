from selenium import webdriver
import time

d = webdriver.Firefox()
url = 'http://localhost:8080/Banksys_ssh/'
d.get(url)
i = 0
for i in range(1000):
    d.find_element_by_id('loginValidate_userNO').send_keys('1571224719329')
    d.find_element_by_id('loginValidate_password').send_keys('123456')
    d.find_element_by_id('loginValidate_0').click()
    # -----------------------------------存款-----------------------------
    d.switch_to.frame("leftFrame")
    d.find_element_by_xpath('/html/body/p[2]/a/img').click()
    d.switch_to.default_content()
    d.switch_to.frame("mainFrame")
    d.find_element_by_id('smoneyValidate_money').send_keys('1000')
    d.find_element_by_id('smoneyValidate_0').click()
    # -------------------------------------------------------取款-----------------------------
    # d.switch_to_default_content()
    d.switch_to.default_content()
    d.switch_to.frame("leftFrame")
    d.find_element_by_xpath('/html/body/p[3]/a/img').click()
    d.switch_to.default_content()
    d.switch_to.frame("mainFrame")
    d.find_element_by_id('fmoneyValidate_money').send_keys('100')
    d.find_element_by_id('fmoneyValidate_0').click()

    # --------------------------------------退出---------------------------
    d.switch_to.default_content()
    d.switch_to.frame("leftFrame")
    d.find_element_by_xpath('/html/body/p[7]/a/img').click()

    d.switch_to.default_content()
    # d.find_element_by_xpath('/html/body/center/a').click()
    d.find_element_by_link_text('返回').click()