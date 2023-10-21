import threading

from startListen import listen_keybord, listen_mouse
from mainWindow import run_main_window
from threading import Thread

if __name__ == '__main__':
    threading.Thread(target=run_main_window).start()
    listen_keybord()
    listen_mouse()
