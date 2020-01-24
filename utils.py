import smtplib
import time
import getpass


def parse_sending_options(opt, msg1, msg2):
    sender_email, sender_pwd, sender, receiver_email, receiver = take_credentials()
    if opt == 1:
        message_type = "News Headlines"
        send_mail(msg1, message_type, sender_email,
                  sender, receiver_email, receiver, sender_pwd)
    elif opt == 2:
        message_type = "Weather Forecast"
        send_mail(msg2, message_type, sender_email,
                  sender, receiver_email, receiver, sender_pwd)
    else:
        message_type1 = "News Headlines"
        message_type2 = "Weather Forecast"
        send_mail(msg1, message_type1, sender_email,
                  sender, receiver_email, receiver, sender_pwd)
        send_mail(msg2, message_type2, sender_email,
                  sender, receiver_email, receiver, sender_pwd)
    print("Success!!")


def take_credentials():
    sender_email = input("Enter Sender's email id: ")
    sender_pwd = getpass.getpass(f"Enter password for {sender_email}: ")
    receiver_email = input("Enter receiver's email id: ")
    receiver = receiver_email.split('@')[0]
    receiver = "".join([i for i in receiver if not i.isdigit()])
    sender = sender_email.split('@')[0]
    return sender_email, sender_pwd, sender, receiver_email, receiver


def send_mail(message, message_type, sender_email, sender, receiver_email, receiver, sender_pwd):

    message = f"""From: {sender} <{sender_email}>
To: {receiver} <{receiver_email}>
Subject: {message_type}

{message}
"""
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    message = message.encode("utf8")
    s.login(sender_email, sender_pwd)
    s.sendmail(sender_email, receiver_email, message)
    s.quit()


def get_weather(browser):
    time.sleep(3)

    weather_message = "Weather details for "
    print("Getting", weather_message, end='')

    city_name = browser.find_element_by_xpath(
        "/html/body/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div[1]/div[1]/div/div[1]/div/div[1]/h2").text
    weather_message += city_name + '.\n\n'
    print(city_name)
    print()
    today_weather = browser.find_element_by_xpath(
        "/html/body/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div[1]/div[1]/div/div[2]/div[1]/div[1]/div").text
    today_temp = browser.find_element_by_xpath(
        "/html/body/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div[1]/div[1]/div/div[2]/div[1]/div[1]/span").text
    curr_weather = "Current Weather: " + '.\n'
    str(today_weather) + " : " + str(today_temp) + '.\n'
    print(curr_weather)

    weather_message += curr_weather

    today_weather = browser.find_element_by_xpath(f"/html/body/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div[1]/div[1]/div/div[2]/div[2]/div/div[{1}]").get_attribute("aria-label")
    print(today_weather)
    print()

    weather_message += today_weather + '.\n\n'

    weather_message += 'Upcoming Days:\n\n'

    print("Upcoming Days\n")
    for i in range(1, 4):
        weather = browser.find_element_by_xpath(f"/html/body/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div[1]/div[1]/div/div[2]/div[2]/div/div[{i+1}]").get_attribute("aria-label")
        print(weather)

        weather_message += weather + '.\n'
    print()

    return weather_message


def get_headlines(browser):

    headlines = "Here are the Current News Headlines for you\n"
    print("Headlines\n")
    news = browser.find_element_by_xpath(
        "/html/body/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[1]/h2/span/a").click()
    time.sleep(5)
    for i in range(10):
        head = browser.find_element_by_xpath(f"/html/body/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[2]/span[1]/div/div/main/c-wiz/div/div/main/div[1]/div[{i+1}]/div/article/h3/a")
        if '...' in head.text:
            head = browser.find_element_by_xpath(f"/html/body/c-wiz[2]/div/div[2]/c-wiz/div/div[2]/div[2]/span[1]/div/div/main/c-wiz/div/div/main/div[1]/div[{i+1}]/div/article/a").get_attribute("href")
            browser.execute_script("window.open('');")
            browser.switch_to.window(browser.window_handles[1])
            browser.get(head)
            time.sleep(3)
            headline = browser.title
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
        else:
            headline = head.text
        headline = f'{i+1}'+': '+headline
        print(headline)
        print()
        headlines += headline+'.\n'
        time.sleep(1)
    return headlines.strip()
