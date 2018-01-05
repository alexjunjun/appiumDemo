# encoding = UTF-8
import os
import unittest
import sys

import time
from appium import webdriver

from lib.base_page import BasePage
from lib.init_env import init_env
from lib.log_config import get_logger

_mylogger = get_logger(os.path.basename(__file__))


class GxqLoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _mylogger.info('安装，启动应用中')
        cls.driver = init_env().install_launch_app()
        cls.basicAct = BasePage(cls.driver)
        # 如果有红包引导页，点击我已注册
        cls.basicAct.click('id=>gxq_has_reg_ed')
        try:
            cls.basicAct.click('id=>gxq_new_user_close')
        except:
            _mylogger.warning('无需二次关闭，继续')

    @classmethod
    def tearDownClass(cls):
        print('tearDown ...')
        time.sleep(2)
        cls.driver.close_app()
        cls.driver.quit()

    def test_login(self):
        _mylogger.info('start login')
        try:
            self.basicAct.click('id=>my_money_head')
        except:
            _mylogger.warning('无需点击头像，继续')
        self.basicAct.input('id=>gxq_write_phone_num_username', '15768896473')
        self.basicAct.click('id=>gxq_write_phone_num_next_btn', '')
        self.basicAct.input('id=>gxq_more_new_login_password', '123456')
        self.basicAct.click('id=>gxq_more_new_login_next_btn', '')


if __name__ == '__main__':
    unittest.main()
