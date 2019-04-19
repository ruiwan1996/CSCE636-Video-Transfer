# CSCE636-Video-Transfer
Video Style Transfer using CNN


ImageStyleTransfer.ipynb is the file used for doing image style transfer(run on Google colab's GPU).
To run ImageStyleTransfer.ipynb:
1. Choose an original image, e.g. base_image_path = 'drive/style_transfer/vedioFrame/665.jpg'
2. Choose a style reference image, e.g. style_reference_image_path = 'drive/style_transfer/star.jpg'
3. Choose a directory to save all the transferred images, e.g. result_prefix = 'drive/style_transfer/frame665/'
4. Set the number of iterations for transferring, e.g. iterations = 2000
5. Set the weights for content loss and style loss(the number is not important, but the ratio is). e.g. content_weight = 1, style_weight = 1000
6. Then we can run all the codes. The transferred results after each iteration will be saved under the path result_prefix.

VideoTransfer.ipynb is the file used for doing video style transfer(run on Google colab's GPU).
To run VideoTransfer.ipynb:
1. Seperate the video you want to transfer into images and save them under the path base_image_path
2. Choose a style reference image, e.g. style_reference_image_path = 'drive/style_transfer/star.jpg'
3. Choose a directory to save all the transferred images, e.g. result_prefix = 'drive/style_transfer/vedioResults3/'
4. Set the number of iterations for each frame, e.g. iterations = 50
5. Set the weights for content loss and style loss(the number is not important, but the ratio is). e.g. content_weight = 1, style_weight = 1000
6. Set the number of frames that we want to transfer, e.g. range(1,500)
7. Then we can run all the codes. The transferred results of each frame will be saved under the path result_prefix.


1.avi and 2.avi are two original videos.
star.jpg and nahan.jpg are two style refence images.
transfered_1.avi and transfered_2.avi are the corresponding style transferred videos.

GUIdeomo.py is the GUI demo. 
The video frames cannot be processed in real time. So, the demo only can show already transferred videos.
To run the GUIdeomo.py:
1. Put transfered_1.avi and transfered_2.avi under path D:/.
2. Select star.jpg, select 1.avi, click PLAY button.
3. Select nahan.jpg, select 2.avi, click PLAY button.

Demo video link: https://www.youtube.com/watch?v=_CorC_JRoXw


jpg2video.py is used for save the images into a video. 
Since the frames are precessed seperately, they need to be put into a video later.
