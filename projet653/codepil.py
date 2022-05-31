#Packages

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from scipy import ndimage
import os


#Open the file

im = Image.open('Allemagne2eF.jpg')
channels = im.split()
r = np.array(channels[0])

fig = plt.figure("Red Channel")
plt.imshow(r, origin = "upper", cmap = cm.gray)
plt.colorbar()
plt.show()

#Rotate the image

im_rotate = im.rotate(270)
im_rotate.show()

#Plot the histogram

fig = plt.figure("Histogram")
plt.hist(r.flatten(), bins=np.arange(256), histtype = "stepfilled")
plt.show()

#Tresholding

seuil = 80
ims = r > seuil
binaire = np.where(ims,1,0)

fig = plt.figure("Thresholding")
plt.imshow(binaire, origin = "upper", cmap = cm.gray)
plt.colorbar()
plt.show()

#Erosion and labelling

erod = ndimage.morphology.binary_erosion(binaire, structure=np.ones((10,10)))
lab, number = ndimage.measurements.label(erod)

fig = plt.figure("Erosion effect")
ax = fig.add_subplot(1, 3, 1)
ax.axis("off")
plt.title("Erosion ON")
plt.imshow(erod, origin = "upper", cmap = cm.binary)
ax = fig.add_subplot(1, 3, 2)
ax.axis("off")
plt.title("Erosion OFF")
plt.imshow(binaire, origin = "upper", cmap = cm.binary)
ax = fig.add_subplot(1, 3, 3)
ax.axis("off")
plt.title("Labeling")
plt.imshow(np.where(lab,lab,np.nan), origin = "upper", cmap = cm.jet)
#plt.colorbar()
plt.show()

print(number)

fig = plt.figure("Labeling")
plt.title("Nombre de grains")
plt.imshow(np.where(lab,lab,np.nan), origin = "upper", cmap = cm.inferno)
plt.colorbar()
plt.show()

