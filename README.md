# CSCE636-Video-Transfer
Video Style Transfer using CNN


ImageStyleTransfer.ipynb is the file used for doing image style transfer(run on Google colab's GPU).
VideoTransfer.ipynb is the file used for doing video style transfer(run on Google colab's GPU).

1.avi and 2.avi are two original videos.
star.jpg and nahan.jpg are two style refence images.
transfered_1.avi and transfered_2.avi are the corresponding style transferred videos.

GUIdeomo.py is the GUI demo. 
The video frames cannot be processed in real time. So, the demo only can show already transferred videos.
To run the GUIdeomo.py:
1. Put transfered_1.avi and transfered_2.avi under path D:/.
2. Select star.jpg, select 1.avi, click PLAY button.
3. Select nahan.jpg, select 2.avi, click PLAY button.


jpg2video.py is used for save the images into a video. 
Since the frames are precessed seperately, they need to be put into a video later.
