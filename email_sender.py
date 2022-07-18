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
    smtp.login('dingyr0925@gmail.com', 'Bddongding1!')
    smtp.send_message(email)
    print('All good boss!')
