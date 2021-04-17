import sys, time
from datetime import date, datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

today = date.today().strftime('%d/%m/%Y')
current_time = datetime.now().strftime("%H:%M:%S")

msgDate = 'TIME'
msgTime = 'DATE'
msg = 'Hello, there!'


def new_chat(user_name):
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"]')
    new_chat.send_keys(user_name)
    time.sleep(2)
    
    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as se:
        print('Username not in contact list')
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()

    
    
if __name__ == '__main__': 
    
    while True:
        if msgDate == today:
            current_time = datetime.now().strftime("%H:%M:%S")
            if current_time >= msgTime:
                options = webdriver.ChromeOptions()
                options.add_argument(r'--user-data-dir=C:ADD PATH HERE')
                options.add_argument('--profile-directory=Default')

                chrome_browser = webdriver.Chrome(executable_path=r'ADD PATH HERE', options=options)
                chrome_browser.get('https://web.whatsapp.com/')
                time.sleep(15)
                
                user_name_list = ['Test']

                for user_name in user_name_list:
                    try:
                        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
                        user.click()
                    except NoSuchElementException as se:
                        new_chat(user_name)
                        time.sleep(1)

                    time.sleep(2)
                    message_box = chrome_browser.find_element_by_xpath('//div[@class="_2A8P4"]')
                    time.sleep(2)
                    
                    message_box.send_keys(msg)
                    time.sleep(1)
                    
                    message_box = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
                    message_box.click()
                    time.sleep(2)
                    chrome_browser.close()
                    sys.exit()
            today = date.today().strftime('%d/%m/%Y')
            time.sleep(10)
