# coding=utf-8
import os
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from lib.log_config import get_logger
from lib.read_config import readConfig

_mylogger = get_logger(os.path.basename(__file__))

mailto_list = readConfig('config.ini', 'email', 'mailto_list').replace(' ', '').split(',')  # 收件人列表
mail_host = readConfig('config.ini', 'email', 'mail_host')  # 配置邮件服务器
mail_from = readConfig('config.ini', 'email', 'mail_from')  # 发件人
mail_pass = readConfig('config.ini', 'email', 'mail_pass')  # 密码
mail_postfix = readConfig('config.ini', 'email', 'mail_postfix')  # 密码


def send_mail(sub='UnitTestReport', result_file=None):
    # 读取html文件内容作为邮件正文,以附件发送html文件
    try:
        with open(result_file, 'r', encoding='utf-8') as result:
            mail_body = result.read()
    except Exception as e:
        _mylogger.error('读取html文件失败{}'.format(e))

    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg.attach(MIMEText(_text=mail_body, _subtype='html', _charset= 'utf-8'))
    part = MIMEText(open(result_file, 'rb').read(), 'base64', 'utf-8')
    part["Content-Type"] = 'application/octet-stream'
    part["Content-Disposition"] = 'attachment; filename="%s"'%result_file
    msg.attach(part)

    _mylogger.info(u'开始发送邮件')
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_from, mail_pass)  # 登陆服务器
        s.sendmail(mail_from, mailto_list, msg=msg.as_string())  # 发送邮件
        s.close()
        _mylogger.info(u"邮件发送成功")
    except (Exception) as e:
        _mylogger.error(u'邮件发送失败：%s' % e)


if __name__ == '__main__':
    send_mail(u"unittest自动化测试结果", '../result/UnittestTextReport20171226@150309.html')
