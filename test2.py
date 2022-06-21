import smtplib


def send():
    from_addres = 'denischicherov@yandex.ru'
    to_addres = 'kirillfedichkin667@gmail.com'
    website = 'vk.com/babyjon_0'
    friend_name = 'Артем'
    sender_name = 'Денис'
    titles = f"""From: {from_addres}
    To: {to_addres}
    Subject: Приглашение!
    Content-Type: text/plain; charset="UTF-8";"""

    pattern = """{0}
    
    Научим монтажу по ссылку за 3400 руб, %website%""".format(titles)

    letter = pattern.replace('%friend_name%', friend_name).replace('%my_name%', sender_name).replace('%website%', website)

    login = 'denischicherov'
    password = 'Wsx54321'

    letter = letter.encode('UTF-8')
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(login, password)
    server.sendmail(from_addres, to_addres, letter)
    server.quit()


for i in range(15):
    from_addres = 'denischicherov@yandex.ru'
    to_addres = 'kirillfedichkin667@gmail.com'
    website = 'vk.com/babyjon_0'
    friend_name = 'Артем'
    sender_name = 'Денис'
    titles = f"""From: {from_addres}
    To: {to_addres}
    Subject: Приглашение!
    Content-Type: text/plain; charset="UTF-8";"""

    pattern = """{0}

    Научим монтажу по ссылку за 3400 руб, %website%""".format(titles)

    letter = pattern.replace('%friend_name%', friend_name).replace('%my_name%', sender_name).replace('%website%',
                                                                                                     website)

    login = 'denischicherov'
    password = 'Wsx54321'

    letter = letter.encode('UTF-8')
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(login, password)
    server.sendmail(from_addres, to_addres, letter)
    server.quit()

