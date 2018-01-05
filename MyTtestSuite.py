# coding = UTF-8
import os
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from testCase.testGxqLogin import GxqLoginTests
from testCase.testGxqTab import GxqTabTest
from testCase.testWebPage import GxqWebPageTest


class MyTestSuite:

    def __init__(self):
        pass

    # 构造测试集
    def suite(self, testCaseDir):

        suite = unittest.TestSuite()

        # add test 方法添加用例，支持单个方法
        # suite.addTest(GxqAndroidTests("test_login"))
        # suite.addTest(GxqAndroidTests("testFundTab"))

        # fromTestCase和makeSuite方法添加用例，支持整个类全部添加
        loginCase = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=GxqLoginTests)
        tabCase = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=GxqTabTest)
        # webCase = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=GxqWebPageTest)
        suite.addTests([loginCase, tabCase])
        # suite = unittest.TestSuite(unittest.makeSuite(Myclass_Test))

        # discover方法添加用例，支持整个目录全部添加
        # # discover = unittest.defaultTestLoader.discover('testCase')
        # discover = unittest.TestLoader().discover(testCaseDir)
        # for s in discover:
        #     suite.addTests(s)
        return suite


if __name__ == '__main__':
    fileName = os.path.join(os.path.dirname(__file__),
                            './result/UnittestTextReport{}.html'.format(time.strftime('%Y%m%d@%H%M%S')))
    print(fileName)
    with open(fileName, 'wb+') as f:
        runner = HTMLTestRunner(stream=f,
                                title=u'unittestDemo Report',
                                description='report',
                                verbosity=2
                                )
        runner.run(MyTestSuite().suite('testCase'))
