# Packages
from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0


    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions
        du tableau 2D (tab_pixels)
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name, as_gray = True)
        self.H, self.W = self.pixels.shape
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")



    # Binarization method
    # 2 parameters :
    #   self : picture to binarize
    #   S : threshold of binarization
    #   we return a binarized picture

    def binarization(self, S):
        img_bin = Image()
        img_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))

        for y in range(len(self.pixels)):
            for x in range(len(self.pixels[y])):
                if self.pixels[y][x] >= S:
                    img_bin.pixels[y][x] = 255

        return img_bin




    # In a binarized picture with a black form on a white background
    # The 'location' method help to limit the picture in a rectangle with
    # the black form
    # 1 parameter :
    #   self : the binarized image that we want to reframe
    #   we return the reframed image

    def localization(self):

        x_min = min(np.where(self.pixels==0)[1])
        x_max = max(np.where(self.pixels==0)[1])

        y_min = min(np.where(self.pixels==0)[0])
        y_max = max(np.where(self.pixels==0)[0])




        new_img = Image()
        new_img.set_pixels(np.zeros((y_max-y_min+1, x_max-x_min+1)))
        new_img.pixels=np.array(self.pixels[y_min:(y_max+1),x_min:(x_max+1)])
        return new_img


    # Resizing of the picture

    def resize(self, new_H, new_W):
        i = Image()
        pixels_resized = resize(self.pixels, (new_H, new_W))
        i.set_pixels(np.uint8(pixels_resized*255))
        return i

    # Croping the edge of the picture

    def crop(self, new_H, new_W):
        i = Image()
        i.set_pixels(np.zeros((new_H, new_W)))
        i.pixels=self.pixels[(self.H-new_H)//2:(self.H+new_H)//2, (self.W-new_W)//2:(self.W+new_W)//2]
        return i


    # Measurement of similarity between two pictures

    def similarity(self, im):
        img_sub = self.pixels - im.pixels
        nb_non_zero = np.count_nonzero(img_sub)
        nb_pixels = self.pixels.size

        return (nb_pixels-nb_non_zero)/nb_pixels

