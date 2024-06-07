import importlib.util
import subprocess
import webbrowser
import threading
import time

def launch():
    subprocess.call(['python', 'manage.py', 'runserver', '0.0.0.0:8014'])


lc = threading.Thread(target=launch)
lc.start()


time.sleep(1)
webbrowser.open("http://127.0.0.1:8014/")
