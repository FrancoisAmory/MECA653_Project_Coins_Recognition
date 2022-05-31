# Packages
import matplotlib.pyplot as plt
from image import Image
from reconnaissance import *


if __name__ == '__main__':

    # Useful variables
    path_to_assets = '../assets/'
    plt.ion()


    # Reading and opening the picture

    image = Image()
    image.load(path_to_assets + '2e_test.png')
    #image.display("Exemple d'image")


    # Binarization of the picture

    S = 0.7
    image_binarised = image.binarization(S)
    image_binarised.display("Binarized Image")


    # Location of the picture

    image_localized = image_binarised.localization()
    image_localized.display("Localized Image")
    
    new_w,new_h = image_localized.W ,image_localized.H
    #print(new_w,new_h)
    
    
    
    image2 = Image()
    image2.load(path_to_assets + '2e_test.png')
    h, w = image2.H, image2.W 
    


    # Resizing of the picture

    image_cropped = image2.crop(new_h, new_w)
    image_cropped.display("Cropped Image")


    # Reading models and recognition

    models_list = models_reading(path_to_assets)
    result = coins_recognition(image_cropped, models_list,220)
    print("The coin recognized is : ", result)

    
    
  
