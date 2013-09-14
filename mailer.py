#!/usr/bin/env python
#-*-encoding:utf-8-*-

import sys
import os
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from optparse import OptionParser

alias = {'evernote': 'xxxxxxxxxxxx@m.evernote.com'}

def msgger(mail_to = [],subject = '', content = ''):
	today = datetime.datetime.now().strftime("%Y%m%d")
	smtp_host = "smtp.host"
	smtp_user = "email"
	smtp_pswd = "password"
	smtp_postfix = "postfix"

	msg = MIMEText(content, "plain", "utf8")
	msg['Accept-Charset'] = "ISO-8859-1, utf-8"
	msg['Subject'] = '%s_%s' % (today, subject)
	msg['From'] = '%s <%s>' % (Header(u"Mailer", "utf-8"), smtp_user)
	msg['to'] = ";".join(mail_to)
	try:
		s = smtplib.SMTP()
		s.connect(smtp_host)
		s.login(smtp_user, smtp_pswd)
		s.sendmail(smtp_user, mail_to, msg.as_string())
		s.close()
		print u"发送邮件成功"
	except Exception, e:
		print u"发送邮件失败: " + e
if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-t", "--to", dest="mail_to", type="string", help=u"收信人列表")
	parser.add_option("-s", "--subject", dest="subject", type="string", help=u"主题")
	parser.add_option("-c", "--content", dest="content", type="string", help=u"内容")
	parser.add_option("-f", "--file", dest="contain_file", type="string", help=u"从文件中读取内容")
	(options, args) = parser.parse_args()
	if(options.mail_to):
		mail_to = options.mail_to.split(',')
		mail_to = [ receiver in alias.keys() and alias[receiver] or receiver for receiver in mail_to ] 
	else:
		mail_to = []
		subject = options.subject
		content = options.content
	try:
		if options.contain_file:
			with open(options.contain_file) as f:
			file_content = f.read()
		else:
			file_content = ''
	except Exception, e:
		file_content = ''
	if(not os.isatty(0)):
		pip_content = sys.stdin.read()
	else:
		pip_content = ''
	content = options.content and options.content + "\n" or ''
	content += pip_content and pip_content + "\n" or ''
	content += file_content or ''
	if(mail_to):
		msgger(mail_to, subject, content)
	else:
		print u'参数不全'
