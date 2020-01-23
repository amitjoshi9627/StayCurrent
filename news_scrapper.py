from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from utils import *

try:
    opts = Options()
    opts.set_headless()
    assert opts.headless
    browser = Firefox()
    start = time.time()
    print('Starting the program. Please wait...\n')
    browser.get('https://news.google.com/')
    end = time.time()
    print(f'Total time to load the page: {round(end - start,5)} seconds.\n')

    weather = get_weather(browser)
    time.sleep(2)
    news = get_headlines(browser)

    print("Choose one:")
    print("1.News\n2.Weather\n3.Both\n4.Leave Program")
    choice = input()
    print()
    if not int(choice) == 4:
        parse_sending_options(int(choice), news, weather)

    time.sleep(2)

    browser.close()
except Exception as error:
    time.sleep(5)
    print("Due to some technical error. The program is exiting...")
    browser.close()
