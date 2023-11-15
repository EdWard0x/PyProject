import threading
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def web():
    web = webdriver.Chrome()
    web.get('https://app.masa.finance/')
    try:
        element = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
        )
    finally:
        username = web.find_element(By.XPATH, '//*[@id="username"]').send_keys('testpro2021@163.com')
        passwd = web.find_element(By.XPATH, '//*[@id="password"]').send_keys('czhZDY0519')
        sub = web.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/form/div[2]/button').send_keys(
            Keys.ENTER)
        time.sleep(5)

        try:
            element = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[1]/span[4]'))
            )
        finally:
            web.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[1]/span[4]').click()
            web.find_element(By.XPATH, '//*[@id="enode"]').send_keys('abcdefg')
            web.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[5]/button').click()
            time.sleep(60)
            web.quit()

if __name__ == '__main__':
    t1 = threading.Thread(target=web, args=())
    t2 = threading.Thread(target=web, args=())
    # 启动线程运行
    t1.start()
    t2.start()

    # 等待所有线程执行完毕
    t1.join()  # join() 等待线程终止，要不然一直挂起
    t2.join()