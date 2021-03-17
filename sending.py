import smtplib

yandex_mail = 'info40.sgu@mail.ru'
yandex_pass = 'Team40SGU'


def send_emails(mail, msg):
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.ehlo()
    server.login(yandex_mail, yandex_pass)
    server.auth_plain()
    send_to_email = mail
    server.login(yandex_mail, yandex_pass)
    server.sendmail(yandex_mail, send_to_email, msg)
    server.quit()
    print('E-mails successfully sent!')


message = 'Блин блинский'
message = message.encode("utf-8")

mail = 'mr.goat.wot@mail.ru'

send_emails(mail, message)
