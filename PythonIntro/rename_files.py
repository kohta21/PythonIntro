# -*- coding: utf-8 -*-

# ライブラリのインポート
import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r".\prank")
    print (file_list)
    saved_path = os.getcwd()
    print ("Current working directory is " + saved_path)
    os.chdir(r".\prank")

    #(2) for each file, rename filename    
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

def rename_files2():
    #(1) get file names from a folder
    p_dir = (r".\prank")
    file_list = os.listdir(p_dir)
    print (file_list)
    #saved_path = os.getcwd()
    #print ("Current working directory is " + saved_path)
    #os.chdir(r".\prank")

    #(2) for each file, rename filename
    p_dir = p_dir + "\\"    
    for file_name in file_list:
        os.rename(p_dir + file_name, p_dir + file_name.translate(None, "0123456789"))
    #os.chdir(saved_path)

rename_files2()