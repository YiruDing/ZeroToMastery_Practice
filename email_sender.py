# # 220-223
# # 22 07/17 To be fixed...
# 534, b'5.7.9 Application-specific password required. Learn more at\n5.7.9  https://support.google.com/mail/?p=InvalidSecondFactor i12-20020a37c20c000000b006a6a6f148e6sm11159446qkm.17 - gsmtp')
import smtplib
# Allow us to build a SMTP server
from email.message import EmailMessage
# The built-in module in Python

email = EmailMessage()
email['from'] = 'Ding'
email['to'] = 'flyswimwalk@yahoo.com.tw'
email['subject'] = 'Hello World!'

email.set_content('Better slow than stop!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    # Check the protocol to learn more
    smtp.starttls()
    smtp.login('dingyr0925@gmail.com', 'yghfzmpchhsrfbbd')
    # ahhh，是授權的十六碼啦！
    smtp.send_message(email)
    print('All good boss!')
