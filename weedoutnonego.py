import cv2
import os
import shutil

path = "/Users/nalthan/Desktop/vertiasopencvprojecy/crashframes"

with open("Crash-1500.txt",'r') as file:
    for line in file:
        crash_data = line.strip().split(',')
        '''try:
            if crash_data[-1] == "No":
                os.remove(path + "/" + crash_data[0])
        except:
            continue'''
        if crash_data[-1] == "No":
            if os.path.exists(path + "/" + crash_data[0]) == True:
                shutil.rmtree(path + "/" + crash_data[0])
