# coding = utf-8
import os
import unittest

import time

from lib.base_page import BasePage
from lib.init_env import init_env
from lib.log_config import get_logger

_mylogger = get_logger(os.path.basename(__file__))

class GxqWebPageTest(unittest.TestCase):

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

        # cls.driver.WebView.setWebContentsDebuggingEnabled(True)

    @classmethod
    def tearDownClass(cls):
        print('tearDown ...')
        time.sleep(5)
        # cls.driver.close_app()
        # cls.driver.quit()

    def testWebPage(self):
        self.openWebPage()


    def openWebPage(self):
        ele = self.driver.find_elements_by_class_name('android.widget.ImageView')[4]
        if ele.is_displayed():
            ele.click()
        print(self.driver.contexts)
        # self.driver.switch_to.context()




if __name__ == '__main__':
    unittest.main()