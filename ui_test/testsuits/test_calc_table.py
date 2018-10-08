from pageobjects.calc_table import CalcTableHome
from pageobjects.login import login
from framework.browser_engine import BrowserEngine
from logs.logger import Logger
import time
import unittest

logger = Logger(logger="TestCalcTable").getlog()

# 百度新闻、NBA 实现类
class TestCalcTable(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self) # 赋值浏览器对象
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit() # 退出浏览器

    def test_calc_table(self):
        try:
            # 初始化百度首页，并点击新闻链接
            login(self)
            calctablehome = CalcTableHome(self.driver) # 统计界面实例化
            time.sleep(1)
            calctablehome.click_calc_link()
            logger.info("已点击统计按钮")
            time.sleep(1)
            calctablehome.click_calc_worktable_link()
            logger.info("已点击工作表统计")
            logger.info("已进入工作表统计界面")
            #点击选择工作表
            calctablehome.click_choose_table_link()
            logger.info("已点击选择工作表")
            time.sleep(1)
            # 点击选择固定格式表
            calctablehome.click_choose_guding_table_link()
            logger.info("已点击固定格式表")
            time.sleep(1)
            # 选定某个固定格式表
            calctablehome.click_choose_one_table_link()
            time.sleep(1)
            calctablehome.click_submit_link()
            time.sleep(1)
            calctablehome.click_search_link()
            time.sleep(1)
        except Exception as e:
            logger.error("TestCalcTable Error:%s" %e)

if __name__ == '__main__':
    unittest.main()

