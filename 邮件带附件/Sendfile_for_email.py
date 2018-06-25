from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
def format_addr(s):
    name,addr= parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
for_addr = '13286825158@163.com'
passwd = 'w930708'
to_addr = '724432436@qq.com'
smtp_server = 'smtp.163.com'
msg = MIMEMultipart()
msg['From']=format_addr('一号爬虫<%s>'%for_addr)
msg['To']=format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('一号爬虫运行','utf-8').encode()
msg.attach(MIMEText('hello ,this is axin','plain','utf-8'))
part = MIMEApplication(open('D:\python3.6.5\day1.py','rb').read())
part.add_header('Content-Disposition','attachment',filename='邮件.py')
msg.attach(part)
server=smtplib.SMTP(smtp_server,25)
server.login(for_addr,passwd)
server.sendmail(for_addr,[to_addr],msg.as_string())
print('邮件发送成功')
server.quit()