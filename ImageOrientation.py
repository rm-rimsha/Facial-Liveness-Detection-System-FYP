from PIL import Image
import os
from os import listdir
from pathlib import Path


def rotateImages(folderDirectory, rotationAmt):
    images = Path(folderDirectory).glob("*.jpg")
    for i in images:
        image = Image.open(i)
        image.rotate(180).save(i)
        image.close()

directory = "C:/Users/dell/Downloads/CollectionFrames/CollectionFrames/indoor"
for folders in os.listdir(directory):
    filePath = os.path.join(directory, folders)
    if os.path.isdir(filePath):
        print(filePath)
        rotateImages(filePath, 180)

