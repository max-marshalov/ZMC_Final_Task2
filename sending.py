import smtplib

yandex_mail = 'info40.sgu@yandex.ru'
yandex_pass = 'Team40SGU'



def send_emails(title, msg):
    print('ok')
    server = smtplib.SMTP_SSL('smtp.yandex.com')
    print('ok')
    server.ehlo()

    server.ehlo(yandex_mail)
    server.login(yandex_mail, yandex_pass)
    server.auth_plain()
    send_to_email = 'costa.spy@yandex.ru'
    server.login(yandex_mail, yandex_pass)
    message = 'Subject: {}\n\n{}'.format(title, msg)
    server.sendmail(yandex_mail, send_to_email, message)
    server.quit()
    print('E-mails successfully sent!')


# message = 'Блин блинский'
# message = message.encode("utf-8")
#
# theme = 'Ага'
# theme = theme.encode("utf-8")

theme = 'dasd'
message = 'asdsafasfasfasf'

send_emails(theme, message)
