# -*- coding: utf-8 -*-

# ���W���[���̃C���|�[�g
import webbrowser
import time

url ="https://www.youtube.com/user/Bz"

#Python�ł̓��[�v�Ȃǂ�0����n�܂邱�Ƃɒ��ӁI

# for loop�ŉ񐔂𖾎��I or �ϐ��Ŏw��
for num in range(2):
    time.sleep(10)
    #webbrowser.open(url)
    print 'loop =', num + 1

# while loop��p������@
total_breaks = 3
break_count = 0
while (break_count < total_breaks):
    time.sleep(10)
    #webbrowser.open(url)
    print 'loop =', break_count + 1
    break_count = break_count + 1

print 'loop end'
