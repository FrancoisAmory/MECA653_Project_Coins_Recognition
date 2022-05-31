#Coins recognition

#Packages

import skimage                 
from skimage import data, io, color   
from skimage import feature

import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte



#Open the file

image1 = io.imread('Allemagne2eF.jpg')  
io.imshow(image1)
io.show()


#Turn the image into shades of grey

grey_image = color.rgb2grey( image1 )
io.imshow( grey_image )
io.show()


#Detection of circles

# Load picture and detect edges
image = img_as_ubyte(grey_image)
edges = canny(image, sigma=3, low_threshold=0, high_threshold=10)


# Detect two radii
hough_radii = np.arange(200, 350, 20)
hough_res = hough_circle(edges, hough_radii)

# Select the most prominent circle
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii,
                                            total_num_peaks=1)

# Draw them
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
image = color.gray2rgb(image)
for center_y, center_x, radius in zip(cy, cx, radii):
    circy, circx = circle_perimeter(center_y, center_x, radius,
                                    shape=image.shape)
    image[circy, circx] = (220, 20, 20)

ax.imshow(image, cmap=plt.cm.gray)
plt.show()
