from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login():
    _username = ' '
    _password = ' '
    username_xpath = "//*[@id='app']/div/div/div[2]/div/div[1]/div/div/div[3]/form/div[1]/div/div/input"
    password_xpath = "//*[@id='app']/div/div/div[2]/div/div[1]/div/div/div[3]/form/div[2]/div/div/input"
    button_xpath = "//*[@id='app']/div/div/div[2]/div/div[1]/div/div/div[3]/form/button"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
    user = driver.find_element(By.XPATH, username_xpath)
    user.send_keys(_username)
    password = driver.find_element(By.XPATH, password_xpath)
    password.send_keys(_password)
    button = driver.find_element(By.XPATH, button_xpath)
    button.click()


def select():
    global i
    global count

    print('count', count, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    count += 1
    driver.get('https://courseweb.ulearning.cn/ulearning/index.html#/course/textbook?courseId=114610')
    time.sleep(5)
    if i == 0:
        driver.switch_to.alert.accept()
    time.sleep(2)

    # 获取数据
    elem1_xpath = "//*[@id='chapterTr110168528']/td[3]"
    elem2_xpath = '//*[@id="chapterTr110168538"]/td[3]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, elem1_xpath)))
    elem1 = driver.find_element(By.XPATH, elem1_xpath).text
    elem2 = driver.find_element(By.XPATH, elem2_xpath).text
    print("当前的学习时间")
    print("第一章", elem1)
    print('第二章', elem2)

    # 数据处理
    temp1 = (int(elem1[0]) * 10 + int(elem1[1])) * 3600 + (int(elem1[3]) * 10 + int(elem1[4])) * 60 + (
            int(elem1[6]) * 10 + int(elem1[7]))
    temp2 = (int(elem2[0]) * 10 + int(elem2[1])) * 3600 + (int(elem2[3]) * 10 + int(elem2[4])) * 60 + (
            int(elem2[6]) * 10 + int(elem2[7]))
    time.sleep(2)
    print('开始学习')

    # 根据时长来选择课程
    ranges = [[0, 14400, 1], [14400, 28800, 2], [28800, 43200, 3], [43200, 57600, 4],
              [57600, 72000, 5], [72000, 86400, 6], [86400, 100800, 7], [100800, 115200, 8],
              [115200, 129600, 9], [129600, 144000, 10], [144000, 158400, 11], [158400, 172800, 12],
              [172800, 187200, 13], [187200, 201600, 14], [201600, 216000, 15], [216000, 230400, 16]]

    if temp1 < 57600:
        for r in ranges:
            if r[0] <= temp1 < r[1]:
                function(1, r[2])
                break
    elif temp2 < 230400:
        for r in ranges:
            if r[0] <= temp1 < r[1]:
                function(2, r[2])
                break
    else:
        print('程序已完成学习，请检查学习数据')


def function(a, b):
    global i
    if a == 1:
        # 开始学习
        url_learn = 'https://ua.ulearning.cn/learnCourse/learnCourse.html?courseId=33998&chapterId=110168528&classId=592245'
        driver.get(url_learn)
        time.sleep(15)
        # 跳过指引
        if i == 1:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div[4]/div')))
            driver.find_element(By.XPATH, '/html/body/div[8]/div[4]/div').click()
            i = 0
        if b == 1:
            driver.find_element(By.XPATH, '//*[@id="page4809639"]/div').click()
            time.sleep(600)
            select()
        elif b == 2:
            driver.find_element(By.XPATH, '//*[@id="page4809640"]/div').click()
            time.sleep(600)
            select()
        elif b == 3:
            driver.find_element(By.XPATH, '//*[@id="page4809641"]/div').click()
            time.sleep(600)
            select()
        elif b == 4:
            driver.find_element(By.XPATH, '//*[@id="page4809645"]/div').click()
            time.sleep(600)
            select()

    elif a == 2:
        url_learn = 'https://ua.ulearning.cn/learnCourse/learnCourse.html?courseId=33998&chapterId=110168538&classId=592245'
        js = 'var q = document.getElementsByClassName("page-item")[14].scrollIntoView();'
        driver.get(url_learn)
        time.sleep(5)
        # 跳过指引
        if i == 1:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div[4]/div')))
            driver.find_element(By.XPATH, '/html/body/div[8]/div[4]/div').click()
            i = 0
        time.sleep(1)
        if b == 1:
            driver.find_element(By.XPATH, '//*[@id="page4809646"]/div').click()
            time.sleep(600)
            select()
        elif b == 2:
            driver.find_element(By.XPATH, '//*[@id="page4823828"]/div').click()
            time.sleep(600)
            select()
        elif b == 3:
            driver.find_element(By.XPATH, '//*[@id="page4823829"]/div').click()
            time.sleep(600)
            select()
        elif b == 4:
            driver.find_element(By.XPATH, '//*[@id="page4823830"]/div').click()
            time.sleep(600)
            select()
        elif b == 5:
            driver.find_element(By.XPATH, '//*[@id="page4823831"]/div').click()
            time.sleep(600)
            select()
        elif b == 6:
            driver.find_element(By.XPATH, '//*[@id="page4823832"]/div').click()
            time.sleep(600)
            select()
        elif b == 7:
            driver.find_element(By.XPATH, '//*[@id="page4823833"]/div').click()
            time.sleep(600)
            select()
        elif b == 8:
            driver.find_element(By.XPATH, '//*[@id="page4823834"]/div').click()
            time.sleep(600)
            select()
        elif b == 9:
            driver.find_element(By.XPATH, '//*[@id="page4823835"]/div').click()
            time.sleep(600)
            select()
        elif b == 10:
            driver.find_element(By.XPATH, '//*[@id="page4823836"]/div').click()
            time.sleep(600)
            select()
        elif b == 11:
            driver.execute_script(js)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="page4823837"]/div').click()
            time.sleep(600)
            select()
        elif b == 12:
            driver.execute_script(js)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="page4823838"]/div').click()
            time.sleep(600)
            select()
        elif b == 13:
            driver.execute_script(js)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="page4823839"]/div').click()
            time.sleep(600)
            select()
        elif b == 14:
            driver.execute_script(js)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="page4823840"]/div').click()
            time.sleep(600)
            select()
        elif b == 15:
            driver.execute_script(js)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="page4823841"]/div').click()
            time.sleep(600)
            select()
        elif b == 16:
            driver.execute_script(js)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="page4823842"]/div').click()
            time.sleep(600)
            select()


# 打开网页
i = 1
count = 0
url = "https://umooc.ulearning.cn/pc.html#/login"

# 执行操作
# noinspection PyBroadException

try:
    driver = webdriver.Chrome()
    driver.get(url)
    print("开始工作")
    login()
    time.sleep(5)
    select()
except:
    print("发生异常！程序即将退出。")
finally:
    print("程序退出")

