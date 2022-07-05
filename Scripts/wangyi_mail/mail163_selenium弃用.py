#!/usr/bin/python3

#@Readme : selenium登录163，读取未读邮件内容
import time
# from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ua = UserAgent()
# print(ua.random)  # 随机产生
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36' # 伪装
    }

def auto_pc(url,username,password):
    # selenium实例
    browser = webdriver.Chrome()   # 或填入chromedriver.exe的绝对路径
    browser.get(url)
    WebDriverWait(browser, 15).until(  # 显示等待,直到页面出现某个元素
        EC.presence_of_element_located((By.ID, "normalLoginTab"))
    )
    # 因为登录位置处于iframe中,所以要切换进去
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]"))
    #
    email = browser.find_element_by_name('email')
    pwd = browser.find_element_by_name('password')
    login = browser.find_element_by_id('dologin')

    email.clear()
    pwd.clear()
    email.send_keys(username)
    pwd.send_keys(password)
    login.click()

    time.sleep(20)

    browser.implicitly_wait(10)  # 隐式等待（作用：等待网页加载完成）
    # 登录成功后获取cookie
    cookie = browser.get_cookies()
    print(cookie)

    # ----------------------查看是否登录成功---------------------
    # 退出iframe,之前切换到iframe框架上，当进入网页后，需要退出iframe才能操作网页其他的元素
    browser.switch_to.default_content()
    # 简单判断登录是否成功
    name = browser.find_element_by_id("spnUid").text
    print(name)
    if name == (username+'@163.com'):
        print('邮箱登录成功')
        read_email(browser)
    else:
        print('邮箱登录失败')

def read_email(browser):
    # 读邮件
    # class="gWel-mailInfo-ico"
    # browser.find_element_by_class_name('gWel-mailInfo-ico').click() # 点未读
    browser.find_element_by_class_name('nui-tree-item-text').click() # 点收件箱
    # browser.find_element_by_xpath('//*[@id="_mail_menuitem_4_291"]/div/span')#点未读


    time.sleep(2)
    #class="tc0"  获取内容列表
    readList = browser.find_elements_by_class_name('tc0')
    # print(type(readList))
    for read in readList:
        # print(read.text)   # 输出列表内容
        pass

    # 邮件标题
    readList2 = browser.find_element_by_class_name('da0')
    print('邮件标题：',readList2.text,type(readList))
    readList2.click()

    # 切换到iframe架构中
    frame1 = browser.find_element_by_class_name('oD0')
    browser.switch_to.frame(frame1)                         # 把iframe赋值给frame1，然后传递给方法
    content=browser.find_element_by_class_name('netease_mail_readhtml')   # 这是某个未读邮件的class
    print('邮件内容：',content.text)
    # 回到上一层架构：(多表单时，进入一个表单要切回上一层架构，在切入到另一个表单中)
    browser.switch_to.default_content()
    time.sleep(2)

    # --------------------退出登录，退出浏览器--------------------
    # browser.find_element_by_class_name('js-component-component kt1').click()
    browser.close()
    browser.quit()

if __name__ == '__main__':
    url = 'https://mail.163.com/'
    username ='avein521'   # 账号
    password='czhZDY0519'     # 密码
    auto_pc(url, username, password)

