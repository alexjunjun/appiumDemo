# encoding = utf-8
import os

import time

from MyRunTest import MyRunTest
from MyTtestSuite import MyTestSuite
from lib.log_config import get_logger
from lib.send_email import send_mail

_mylogger = get_logger(os.path.basename(__file__))

if __name__ == '__main__':
    rootDir = os.path.dirname(__file__)
    testCaseDir = os.path.join(rootDir,'testCase')
    resultDir = os.path.join(rootDir,'result')
    testNum = time.strftime(('%Y%m%d@%H%M%S'))
    suite = MyTestSuite().suite(testCaseDir)
    _mylogger.info(u'测试序列：{}'.format(testNum))
    resultFile = os.path.join(resultDir, 'UnittestTextReport{}.html'.format(testNum))
    _mylogger.info(u'开始测试')
    MyRunTest().runTest(suite, resultFile)
    # _mylogger.info(u'测试结束，开始发送测试报告')
    # send_mail('UnitTestReport-{}'.format(testNum), resultFile)

