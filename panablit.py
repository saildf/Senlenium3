from selenium import webdriver
from time import sleep, time

d = webdriver.Firefox()
url = 'https://117.48.145.114:8082/login/login.htm'

# -----------------------------------登录----------------------
d.get(url)
d.find_element_by_id('username').send_keys('admin')
d.find_element_by_id('password').send_keys('panabit')
d.find_element_by_class_name('btn').click()
# -------------跳过验证----------------
# sleep(1)
# d.switch_to.window(d.window_handles[0])
# ---------------------登录后页面------------------

# ---------------关闭窗口--------------------
 # d.close()

