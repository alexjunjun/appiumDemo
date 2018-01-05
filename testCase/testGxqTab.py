# coding = utf-8
import os
import unittest

import time
from appium import webdriver

from lib.base_page import BasePage
from lib.init_env import init_env
from lib.log_config import get_logger

_mylogger = get_logger(os.path.basename(__file__))


class GxqTabTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _mylogger.info('打开应用')
        cls.driver = init_env().launch_app()
        cls.basicAct = BasePage(cls.driver)
        # 如果有升级弹窗，关闭
        try:
            _mylogger.info('检测是否有升级弹窗')
            cls.basicAct.click('id=>gxq_dialog_btn_left')
        except:
            _mylogger.warning('无升级弹窗，继续')

    @classmethod
    def tearDownClass(cls):
        print('tearDown ...')
        time.sleep(5)
        # cls.driver.close_app()
        cls.driver.quit()

    def test_change_tab(self):
        _mylogger.info('start test fund tab')
        self.basicAct.click('id=>main_activity_fund_btn')
        time.sleep(2)
        self.basicAct.click('id=>main_activity_market_btn', '')
        time.sleep(2)
        self.basicAct.click('id=>main_activity_discovery_btn', '')
        time.sleep(2)
        self.basicAct.click('id=>main_activity_hot_btn', '')
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
