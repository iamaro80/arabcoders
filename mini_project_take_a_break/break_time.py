import webbrowser
import time

print time.ctime()

count = 0


while count < 3:
    webbrowser.open('https://goo.gl/9u9E97')
    time.sleep(10)
    count += 1
