import os
import zipfile
import time
import pyautogui
import pyperclip
import shutil
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

phone_number = 0

def split(string):
    left, right = string.split(':')
    number = right[1:6]
    return str(number)
    
def get_number():
    global phone_number
    dirfiles = os.listdir('A:/BigDeal/Release/AccsNew')
    arch_path = str(dirfiles[0])
    phone_number = arch_path[0:-4]

def extract_zip():
    global phone_number
    zip_file = zipfile.ZipFile(f'A:/BigDeal/Release/AccsNew/{phone_number}.zip')
    time.sleep(1)
    zip_file.extractall('A:/BigDeal/Release/Tg')
    time.sleep(1)

    zip_file.close()
    time.sleep(1)

def open_browser():
    global phone_number
    app_title = 'winvsdrdjfeww'
    short_name = 'winsgdfgddeqw'
    auth_path = 'https://my.telegram.org/auth'
    path = 'A:/BigDeal/Release/Res/chromedriver.exe'

    os.startfile('A:/BigDeal/Release/Tg/Telegram.exe')
    time.sleep(10)

    pyperclip.copy("Empty")

    pyautogui.moveTo(260, 150, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(x=429, y=150, duration= 0.5)
    pyautogui.scroll(-3000)
    pyautogui.scroll(-3000)
    pyautogui.scroll(-3000)
    pyautogui.dragTo(x=615, y=138, duration= 0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    copy = pyperclip.paste()

    if (str(copy) == "Empty"):
        flag = False
        while (not flag):
            subprocess.run(["powershell", "start A:/BigDeal/Release/Bat/tgKill.bat"], shell=True)
            try:
                shutil.move(f'A:/BigDeal/Release/AccsNew/{phone_number}.zip', 'A:/BigDeal/Release/AccsUsed')
            except:
                os.remove(f'A:/BigDeal/Release/AccsNew/{phone_number}.zip')
            time.sleep(5)
            dirfiles = os.listdir('A:/BigDeal/Release/AccsNew')
            arch_path = str(dirfiles[0])
            phone_number = arch_path[0:-4]
            zip_file = zipfile.ZipFile(f'A:/BigDeal/Release/AccsNew/{phone_number}.zip')
            time.sleep(1)
            zip_file.extractall('A:/BigDeal/Release/Tg')
            time.sleep(1)
            os.startfile('A:/BigDeal/Release/Tg/Telegram.exe')
            time.sleep(10)

            pyperclip.copy("Empty")

            pyautogui.moveTo(260, 150, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(x=429, y=150, duration= 0.5)
            pyautogui.scroll(-3000)
            pyautogui.scroll(-3000)
            pyautogui.scroll(-3000)
            pyautogui.dragTo(x=615, y=138, duration= 0.5)
            pyautogui.hotkey('ctrl', 'c')
            copy = pyperclip.paste()

            if (str(copy) != "Empty"):
                flag = True
    time.sleep(0.5)
    try:
        browser = webdriver.Chrome(executable_path = path)
        time.sleep(0.5)
        browser.get(url=auth_path)
    except:
        print("Browser Error!")
        browser = webdriver.Chrome(executable_path = path)
        time.sleep(0.5)
        browser.get(url=auth_path)

    time.sleep(0.5)
    phone_box = browser.find_element_by_xpath('//*[@id="my_login_phone"]')
    phone_box.send_keys(str(phone_number))
    time.sleep(0.1)
    input_button = browser.find_element_by_xpath('//*[@id="my_send_form"]/div[2]/button')
    input_button.click()
    time.sleep(2)

    login_code = get_code()

    input_code = browser.find_element_by_xpath('//*[@id="my_password"]')
    input_code.send_keys(str(login_code))
    time.sleep(0.1)
    login_button = browser.find_element_by_xpath('//*[@id="my_login_form"]/div[4]/button')
    login_button.click()
    time.sleep(1)

    browser.get('https://my.telegram.org/apps')
    time.sleep(0.5)

    try:
        api_id_full = browser.find_element_by_xpath('//*[@id="app_edit_form"]/div[1]/div[1]/span/strong')
        api_id = api_id_full.text
    except:
        app_title_box = browser.find_element_by_xpath('//*[@id="app_title"]')
        app_title_box.send_keys(str(app_title) + str(bot_counter + 1))
        time.sleep(0.1)
        short_name_box = browser.find_element_by_xpath('//*[@id="app_shortname"]')
        short_name_box.send_keys(str(short_name) + str(bot_counter + 1))
        time.sleep(0.1)
        desktop_box = browser.find_element_by_xpath('//*[@id="app_create_form"]/div[4]/div/div[5]/label/input')
        desktop_box.click()
        time.sleep(0.5)
        create_app_button = browser.find_element_by_xpath('//*[@id="app_save_btn"]')
        create_app_button.click()
        time.sleep(0.5)
    finally:
        api_id_full = browser.find_element_by_xpath('//*[@id="app_edit_form"]/div[1]/div[1]/span/strong')
        api_id = api_id_full.text
        time.sleep(0.1)
        api_hash_full = browser.find_element_by_xpath('//*[@id="app_edit_form"]/div[2]/div[1]/span')
        api_hash = api_hash_full.text
        time.sleep(0.1)

    save_button = browser.find_element_by_xpath('//*[@id="app_save_btn"]')
    save_button.click()
    time.sleep(0.5)
    browser.get('https://my.telegram.org/')
    time.sleep(0.5)
    browser.get('https://my.telegram.org/auth/logout')
    time.sleep(1)
    browser.close()
    browser.quit()

    try:
        fdata = open(f"A:/BigDeal/Release/Bots/bot{str(bot_counter + 1)}/Data.txt", 'w')
        fdata.write(str(bot_counter + 1) + '\n')
        fdata.write(str(api_id) + '\n')
        fdata.write(str(api_hash) + '\n')
        print("Data write done")
    except Exception as ex:
        print(ex)
    finally:
        fdata.close()

def mkdir(flag):
    if (flag == 1):
        shutil.copy(r'A:/BigDeal/Release/Res/Bot.py', f'A:/BigDeal/Release/Bots/bot{str(bot_counter+1)}/Bot.py')
    else:
        os.mkdir(f"A:/BigDeal/Release/Bots/bot{str(bot_counter+2)}")
        shutil.copy(r'A:/BigDeal/Release/Res/botprod.py', f'A:/BigDeal/Release/Bots/bot{str(bot_counter+2)}/botprod.py')
        shutil.copy(r'A:/BigDeal/Release/Res/start.bat', f'A:/BigDeal/Release/Bots/bot{str(bot_counter+2)}/start.bat')
        shutil.copy(r'A:/BigDeal/Release/Res/marker.txt', 'A:/BigDeal/Release/marker.txt')
        try:
            findex = open("A:/BigDeal/Release/BotCounter.txt", 'w')   
            findex.write(str(bot_counter+1) + '\n')
            try:
                shutil.move(f'A:/BigDeal/Release/AccsNew/{phone_number}.zip', 'A:/BigDeal/Release/AccsUsed')
            except:
                os.remove(f'A:/BigDeal/Release/AccsNew/{phone_number}.zip')
        except Exception as ex:
            print(ex)
        finally:
            findex.close()  

def get_code():

    # Point(x=259, y=152) - чат поддержки
    # Point(x=460, y=450) - код входа
    # Point(x=580, y=465) - код подтверждения
    # Point(x=516, y=465) - код подтверждения eng
    # Point(x=428, y=464) - левая сторона кода подтверждения
    # Point(x=605, y=464) - правая сторона кода подтверждения

    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True
    pyautogui.hotkey('alt', 'tab')
    pyautogui.moveTo(260, 150, duration=0.5)
    pyautogui.click()

    pyautogui.moveTo(x=428, y=452, duration= 0.5)
    pyautogui.scroll(-3000)
    pyautogui.scroll(-3000)
    pyautogui.scroll(-3000)
    pyautogui.dragTo(x=550, y=452, duration= 0.5)
    pyautogui.hotkey('ctrl', 'c')

    pyautogui.hotkey('alt', 'tab')
    return (pyperclip.paste())

def first_login():
    subprocess.run(["powershell", "start A:/BigDeal/Release/Bat/tgKill.bat"], shell=True)
    subprocess.Popen(f'start powershell python A:/BigDeal/Release/Bots/bot{str(bot_counter+1)}/Bot.py', shell = True)
    time.sleep(15)
    
    pyperclip.copy(str(phone_number))
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    os.startfile('A:/BigDeal/Release/Tg/Telegram.exe')
    
    time.sleep(10)
    pyautogui.moveTo(260, 150, duration=0.5)
    pyautogui.click()

    pyautogui.moveTo(x=428, y=464, duration= 0.5)
    pyautogui.scroll(-3000)
    pyautogui.scroll(-3000)
    pyautogui.scroll(-3000)
    pyautogui.dragTo(x=605, y=464, duration= 0.5)
    pyautogui.hotkey('ctrl', 'c')

    code_string = pyperclip.paste()
    pyperclip.copy(split(str(code_string)))
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(5)

try:
    f_index = open("A:/BigDeal/Release/BotCounter.txt", "r")
    bot_counter = int(f_index.readline())
    os.remove('A:/BigDeal/Release/marker.txt') 
except Exception as ex:
    print(ex)
finally:
    print("-----------------")
    f_index.close()

subprocess.run(["powershell", "start A:/BigDeal/Release/Bat/tgKill.bat"], shell=True)
get_number()
extract_zip()
open_browser()
mkdir(1)
first_login()
subprocess.run(["powershell", "start A:/BigDeal/Release/Bat/tgKill.bat"], shell=True)
subprocess.run(["powershell", "start A:/BigDeal/Release/Bat/RmDir.bat"], shell=True)
time.sleep(1)
mkdir(0)