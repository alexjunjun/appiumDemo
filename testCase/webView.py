# coding = utf-8
import os
import unittest

import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class WebView(unittest.TestCase):



    def setUp(self):
        realPath = lambda p: os.path.join(os.path.dirname(__file__), p)
        app = realPath('../app/(#456)-app-dev-debug_v4.2.0_20180103165920.apk')
        desired_caps = {'platformName': 'Android', 'platformVersion': '5.1', 'deviceName': 'SGAMHA6D99999999', 'app': app, 'noReset': 'true'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.driver.wait_activity('.module.home.MainActivity', 10)

    def tearDown(self):
        time.sleep(10)
        print('end')
        self.driver.quit()
        # pass

    def testWebView(self):

        print('start test')

        # ele = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TabWidget").childSelector(new UiSelector().className("android.widget.RelativeLayout").childSelector(new UiSelector().text("视频")))')
        ele = self.driver.find_element_by_android_uiautomator('new UiSelector().text("社区")')
        print('切换到社区')
        ele.click()

        # topic = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.LinearLayout").index(2)')
        topic = self.driver.find_element_by_id('tv_community_topic_pv')
        print('点击帖子，查看帖子详情，切换到webView')
        topic.click()

        self.driver.switch_to.context('WEBVIEW_com.jfz.wealth')
        print('currentContext:{}'.format(self.driver.context))


        time.sleep(3)
        print('点击评论按钮')

        commentBtn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/section/div/div/div[2]')
        # 显性等待
        try:
            WebDriverWait(self.driver, 20).until(lambda x:x.find_element_by_xpath('//*[@id="app"]/div/div/div/section/div/div/div[2]'),'控件不存在').click()
            # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(commentBtn))
        except Exception as e:
            print(e)

        print('评论是原生页面，切换到原生')
        self.driver.switch_to.context('NATIVE_APP')
        print('currentContext:{}'.format(self.driver.context))


        commentInputBox = self.driver.find_element_by_id('et_post_topic_content')
        if commentInputBox.is_displayed():
            commentInputBox.send_keys('自动测试提交评论')
            self.driver.keyevent(42)
            self.driver.keyevent(66)


        submitBtn = self.driver.find_element_by_id('tv_titlebar_commit')
        time.sleep(3)
        if submitBtn.is_enabled():
            print('点击提交')
            submitBtn.click()
        else:
            print('提交不可点击')
            time.sleep(10)



if __name__ == '__main__':
    unittest.main()



