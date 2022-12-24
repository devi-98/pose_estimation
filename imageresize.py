from PIL import Image
import os, sys
#path = r'C://Users/Create/Desktop/testre/'
path = r'C://Users/Create/Desktop/adho mukha svanasana/'
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            im=im.convert('RGB')
            f, e = os.path.splitext(path+item)
            imResize = im.resize((512,512), Image.Resampling.LANCZOS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()