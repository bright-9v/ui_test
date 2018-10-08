# -*- coding:utf-8 -*-

from unit.base_page import BasePage
import time

class CalcTableHome(BasePage):
    #先收起事事节点，否则页面上看不到统计节点
    lay_up_things_link = 'xpath=>//*[@id="es-body"]/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/ul/li[1]/a'
    calc_link = "link_text=>统计"
    calc_worktable_link = "link_text=>工作表统计"
    #点击选择工作表
    choose_table_link = 'xpath=>//*[@id="es-layout-content-body"]/div/div/div[3]/div/div[1]/div[1]/div/div[1]/button'
   #点击选择固定格式表
    choose_guding_table_link = "link_text=>固定格式表"
    #选定某个固定格式表
    choose_one_table_link = 'xpath=>//*[@id="es-body"]/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[2]/div'
    #点击确定按钮
    submit_link = "class_name=>btn-submit"
    #工作表统计页面的查询按钮
    search_link = 'xpath=>//*[@id="es-layout-content-body"]/div/div/div[3]/div/div[3]/div[2]/button[2]'

    #工作表统计页面的断言，是否有“工作表统计横向导航”
    cal_assert_navigation_link = 'xpath=>//*[@id="es-layout-content-body"]/div/div/div[1]/ol/li[2]/a'


    # 点击工作表统计节点的各个按钮
    def click_calc_link(self):
        self.click(self.lay_up_things_link)
        time.sleep(1)
        self.click(self.calc_link)
    def click_calc_worktable_link(self):
        self.click(self.calc_worktable_link)
    def click_choose_table_link(self):
        self.click(self.choose_table_link)
    def click_choose_guding_table_link(self):
        self.click(self.choose_guding_table_link)
    def click_choose_one_table_link(self):
        self.click(self.choose_one_table_link)
    def click_submit_link(self):
        self.click(self.submit_link)
    def click_search_link(self):
        self.click(self.search_link)
