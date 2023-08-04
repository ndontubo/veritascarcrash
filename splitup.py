import cv2
import os

path = "/Users/nalthan/Desktop/vertiasopencvprojecy/Crash-1500"

crash_file_names = [path + "/" + filename for filename in os.listdir(path) if filename.endswith('.mp4')]
print(crash_file_names)
for vid in crash_file_names:
    cam = cv2.VideoCapture(vid)
    currentframe = 1
    tempdir = "/Users/nalthan/Desktop/vertiasopencvprojecy/crashframes/"
    crashframedir = vid.replace("Crash-1500", "crashframes").replace(".mp4", '')
    os.mkdir(crashframedir)
    while(True):
        # reading from frame
        ret,frame = cam.read()
    
        if ret:
            # if video is still left continue creating images
            name = crashframedir + "/frame" + str(currentframe) + '.jpg'
            print ('Creating...' + name)
    
            # writing the extracted images
            cv2.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    cam.release()
    cv2.destroyAllWindows()

path = "/Users/nalthan/Desktop/vertiasopencvprojecy/Normal"

normal_file_names = [path + "/" + filename for filename in os.listdir(path) if filename.endswith('.mp4')]
print(normal_file_names)
for vid in normal_file_names:
    cam = cv2.VideoCapture(vid)
    currentframe = 1
    tempdir = "/Users/nalthan/Desktop/vertiasopencvprojecy/normalframes/"
    normalframedir = vid.replace("Normal", "normalframes").replace(".mp4", '')
    os.mkdir(normalframedir)
    while(True):
        # reading from frame
        ret,frame = cam.read()
    
        if ret:
            # if video is still left continue creating images
            name = normalframedir + "/frame" + str(currentframe) + '.jpg'
            print ('Creating...' + name)
    
            # writing the extracted images
            cv2.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    cam.release()
    cv2.destroyAllWindows()