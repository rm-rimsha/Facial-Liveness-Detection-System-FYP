from PIL import Image
import os
from os import listdir
from pathlib import Path
import PIL



def resizeImages(folderDirectory):
    images = Path(folderDirectory).glob("*.jpg")
    size = (112,112)
    for i in images:
        image = Image.open(i)
        image = image.convert("RGB")
        image.thumbnail(size)
        image.save(i)
        image.close()

def getSize(folderDirectory):
    images = Path(folderDirectory).glob("*.jpg")
    for i in images:
        image = Image.open(i)
        print(image.size)
        image.close()  
        
def labelImages(folderDirectory):
    images = Path(folderDirectory).glob("*.jpg")
    print("labedimdsfsd")
    for i in images:
        print("in for loop")
        filename = os.path.basename(i)
        name, extension = os.path.splitext(filename)
        updatedName = name + "-1" + extension
        updatedPath = os.path.join(os.path.dirname(i), updatedName)
        os.rename(i, updatedPath)
        print(updatedPath)
        
def verticalImages(folderDirectory):
    images = Path(folderDirectory).glob("*.jpg")
    x = 0
    for i in images:
        filename = os.path.basename(i)
        name, extension = os.path.splitext(filename)
        updatedName = name + str(x) + "-1" + extension
        updatedPath = os.path.join(os.path.dirname(i), updatedName)
        image = Image.open(i)
        vImage = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        vImage = vImage.convert("RGB")
        vImage.save(updatedPath)
        vImage.close()
        x = x+1


directory = "C:/Users/dell/FYP/Dataset(Processed)/a"
#verticalImages(directory)
for folders in os.listdir(directory):
    filePath = os.path.join(directory, folders)
    label = filePath + "-1"
    if os.path.isdir(filePath):
        #os.rename(filePath, label)
        #print("1")
        #resizeImages(filePath)
        #print("2")
        #getSize(filePath)
        labelImages(filePath)
        #verticalImages(filePath)

