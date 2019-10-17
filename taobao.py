import re
import pymongo
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 配置mongo数据库
# client = pymongo.MongoClient("localhost")
# db = client["taobao"]

# 设置浏览器参数
service_args = ["--load-images=false"]
browser = webdriver.Firefox()
# browser = webdriver.PhantomJS(service_args=service_args)
browser.set_window_size(1400, 900)  # 不设置可能访问不到正确的页面
wait = WebDriverWait(browser, 10)


# 输入网址，搜索关键字
def search_page():
    print("正在搜索...")
    try:
        browser.get("https://www.taobao.com/")
        # 搜索
        search = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#J_TSearchForm > div.search-button > button'))
        )
        search.send_keys("美食")
        submit.click()

        # 获取总页数
        total = browser.find_element_by_css_selector(
            "#mainsrp-pager > div > div > div > div.total")

        total = int(re.compile("(\d+)").search(total.text).group(1))
        return total
    except TimeoutException:
        return search_page()


# 翻页访问
def next_page(page_num):
    print("正在翻页...", page_num)
    try:
        number = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#mainsrp-pager > div > div > div > div.form > input")))

        confirm = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
        number.clear()
        number.send_keys(page_num)
        confirm.click()

        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                     "#mainsrp-pager > div > div > div > ul > li.item.active"),
                                                    str(page_num)))

        # 解析页面
        parse_page()

    except TimeoutException:
        next_page(page_num)


# 解析页面，获取商品信息
def parse_page():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               "#mainsrp-itemlist .items .item")))

    # 用pyquery解析
    doc = pq(browser.page_source)
    items = doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product = {"image": item.find(".pic .img").attr("src"), "title": item.find(".title").text(),
                   "price": item.find(".price").text(), "shop": item.find(".shop").text(),
                   "deal-cnt": item.find(".deal-cnt").text()[:-3], "location": item.find(".location").text()}
        print(product)

        # 保存数据
        save_to_mongo(product)


# 将字典格式的数据保存到mongodb中
def save_to_mongo(data):
    try:
        db["taobao"].insert(data)
        print("保存成功", data)
    except Exception:
        print("保存失败")


# 程序主函数
def main():
    total = search_page()
    for i in range(1, total + 1):
        next_page(i)
    browser.close()


if __name__ == "__main__":
    main()
