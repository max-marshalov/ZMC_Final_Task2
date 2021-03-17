import smtplib


def send_message(email, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("limonadov44@gmail.com", "1980limon44")
    server.sendmail("limonadov44@gmail.com", email, message)
    server.quit()


send_message("ctvbxm@mail.ru", "Three hundred backs")
