from image import Image

def models_reading(path):
    files= ['1c.png','2c.png','10c.png','20c.png','50c.png','1e.png', 
            '2e.png']
    list_models = []
    for file in files:
        model = Image()
        model.load(path + file)
        list_models.append(model)
    return list_models


def coins_recognition(image, list_models, S):
    files= ['1c.png','2c.png','10c.png','20c.png','50c.png','1e.png', 
            '2e.png']
    b_a_w_image=image.binarization(S)
    localized_image = b_a_w_image.localization()
    
    simili=[]
    for x in range(len(list_models)):
        im=localized_image.resize(list_models[x].H,list_models[x].W)
    
        simili.append(im.similarity(list_models[x]))
        
        simili_m=max(simili)
        simili_index=simili.index(simili_m)
        
    return files[simili_index][0:-4]
    



