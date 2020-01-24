from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from utils import *

try:
    opts = Options()
    opts.headless = True
    browser = Firefox(options=opts)
    print('Starting the program. Please wait...\n')
    browser.get('https://news.google.com/')

    weather = get_weather(browser)
    time.sleep(2)
    news = get_headlines(browser)

    print("Choose one:")
    print("1.News\n2.Weather\n3.Both\n4.Leave Program")
    choice = input()
    print()
    if not int(choice) == 4:
        parse_sending_options(int(choice), news, weather)
    browser.close()
    time.sleep(2)
except Exception as error:
    print("Due to some technical error. The program is exiting...")
    browser.close()
