# MECA653-Project
Here is the repo for our Project - Coins recognition

  Hello,
  
You can find here the project of François Amory, Nathan Bignon and Vincent Criscuolo.
The idea was borned with the collection of Euro coins of one of the member of the group. After a small reflexion, the three students wanted to try to code a recognition programm of these coins, using some methods of Image processing and machine learning.
During their work, they tried to use different modules of image processing like skimage or pillow, in order to detect circles, rotate the images, plot histograms, and other useful tools for this task.
They also tried to use cv2, but it didn't work on the computer. All the attempts are in the projet653 folder.

But after some reflexions, they tried to create a 'image' class (with skimage) to make their own method of Image processing. You can see by yourself the result of this work, with all the result (binarization of the image, resizing of the image ...). This works better than the codes with modules like pillow and skimage. They didn't manage to recognize the coins because the resized picture was only in shades of grey.
This issue could be fixed by modifying the "Recognition.py" programm.

However, when they started to work on the machine learning, they met some problems. Too few information and help can be found on the Internet to help using machine learning in the project. They made a dataset, (in the asset file) with pictures from the internet. Nothing was working in what they tried about machine learning, instead of image processing, where they manage almost all what they tried (some photos will be put in this git to illustrate).


We hope the work done on this project will be as interesting as possible.

The Coins recognition team

 
