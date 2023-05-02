import os

class Img_path:
    def __init__(self):
        self.caminho_raiz = os.path.path(os.path.dirname(__file__))
        
    def path_img(self):
        path_img = os.path.join(self.caminho_raiz, "src/img")
        print ('a path img é ' + path_img)
        return path_img
    

    