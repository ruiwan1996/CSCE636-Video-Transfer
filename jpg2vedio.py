import os
import cv2

# same images into a video
def picvideo(path, size):
    filelist = os.listdir(path)  # get all the file under the folder
    fps = 24
    file_path = 'D:/original2.avi'   # path for saving
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  #  save as avi

    video = cv2.VideoWriter(file_path, fourcc, fps, size)

    for i in range(500, 873, 1):
        item = path + '/' + str(i) + '.jpg'
        img = cv2.imread(item)  # using opencv to read the image, return numpy.ndarray，the sequence is BGR ，range is 0-255
        video.write(img)  # write the image into video

    video.release()  # release

picvideo("D:/vedioFrame", (1920,1080)) # set the size