# -*- coding: utf-8 -*-

# モジュールのインポート
import webbrowser
import time

url ="https://www.youtube.com/user/Bz"

#Pythonではループなどは0から始まることに注意！

# for loopで回数を明示的 or 変数で指定
for num in range(2):
    time.sleep(10)
    #webbrowser.open(url)
    print 'loop =', num + 1

# while loopを用いる方法
total_breaks = 3
break_count = 0
while (break_count < total_breaks):
    time.sleep(10)
    #webbrowser.open(url)
    print 'loop =', break_count + 1
    break_count = break_count + 1

print 'loop end'
