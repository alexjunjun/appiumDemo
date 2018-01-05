# coding = utf-8
'''
用于初始化浏览器，并新建浏览器driver
'''
import os

import time
from appium import webdriver

from lib.base_page import BasePage
from lib.log_config import get_logger

_mylogger = get_logger(os.path.basename(__file__))


class init_env(object):
    def __init__(self):
        self.driver = None
        self.basicAct = None

    def install_launch_app(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1',
                        'deviceName': 'SGAMHA6D99999999',
                        'appPackage': 'com.gunxueqiu.activity',
                        'appActivity': '.GxqAppLoginActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.basicAct = BasePage(self.driver)
        # 设置隐性等待
        self.driver.implicitly_wait(3)
        self.driver.wait_activity('.GxqViewHelperActivity', 10)
        guidepage = self.driver.find_element_by_id('new_point_1')
        if guidepage.is_displayed():
            # 滑过引导页，进入登录页面
            _mylogger.info('滑过引导页')
            self.driver.swipe(1032, 870, 80, 870)
            time.sleep(1)
            self.driver.swipe(1032, 870, 80, 870)
            time.sleep(1)
            self.driver.swipe(1032, 870, 80, 870)
            time.sleep(1)

            self.basicAct.click('id=>new_start_bt', '')

        # 如果有升级弹窗，关闭
        try:
            _mylogger.info('检测是否有升级弹窗')
            self.basicAct.click('id=>gxq_dialog_btn_left')
        except:
            _mylogger.warning('无升级弹窗，继续')
        return self.driver

    def launch_app(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1',
                        'deviceName': 'SGAMHA6D99999999',
                        'appPackage': 'com.gunxueqiu.activity',
                        'appActivity': '.GxqAppLoginActivity',
                        'noReset': 'true'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.basicAct = BasePage(self.driver)
        # 设置隐性等待
        self.driver.implicitly_wait(3)

        self.driver.wait_activity('.GxqViewHelperActivity',10)
        return self.driver