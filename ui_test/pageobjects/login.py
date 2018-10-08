# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time


# 登录模块
def login(self):
    driver = self.driver
    driver.maximize_window()

    # 此处要等待2秒，否则页面未完成加载，可能找不到输入用户名和密码的框
    time.sleep(2)
    driver.find_element_by_name("mobile").send_keys("13261448006")
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_class_name("btn-submit").click()
    time.sleep(3)
    # 登录成功后，进入测试企业--zy
    driver.find_element_by_class_name("es-things-company-box").click()
    time.sleep(1)
    driver.find_element_by_link_text(u"测试企业--zy").click()
    time.sleep(1)


def teardown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)