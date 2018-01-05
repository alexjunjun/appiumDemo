# encoding = utf-8
from HTMLTestRunner import HTMLTestRunner


class MyRunTest:
    def runTest(self, suite, result_file):
        with open(result_file, 'wb+') as f:
            runner = HTMLTestRunner(stream=f,
                                    title=u'unittestDemo Report',
                                    description='report',
                                    verbosity=2
                                    )
            runner.run(suite)