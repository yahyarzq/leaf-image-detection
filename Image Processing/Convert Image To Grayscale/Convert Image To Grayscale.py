import cv2
import glob
import re
import os
from pathlib import Path
import numpy as np

PATH = dir_path = os.path.dirname(os.path.realpath(__file__)).replace("\\",'/')
#PATH = str(Path(__file__).resolve().parent).replace("\\",'/')
PATH_CWD = os.getcwd().replace("\\",'/')

imdirDaunJambu = PATH_CWD +'/Dataset/Daun Jambu/'
imdirDaunNangka = PATH_CWD + '/Dataset/Daun Nangka/'
file_tag = 'Grayscale'

def getAllFileInFolder(imdir,file_tag,fuct):
    # get all files in a folder
    leaf_name = re.search("Daun\s[a-zA-Z]+",imdir).group()
    ext = ['png', 'jpg', 'gif']    # Add image formats here
    files = []
    [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]
    images = [cv2.imread(file) for file in files]
    # Directory
    directory = leaf_name +" - " + file_tag
    # Parent Directory path
    path = os.path.join(PATH+"/Output/", directory)
    # Create the directory
    try:
      os.mkdir(path)
    except OSError as error:
      print(error)
    # adjust images to all of them and save to different location
    i = 1
    for img in images:
        im_name =  path + "/" + str(i) + ".jpg"
        print(im_name)
        cv2.imwrite(im_name, fuct(img))
        i+=1


def imageConvertGrayscale(image):
    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return im_gray

def main():
    getAllFileInFolder(imdirDaunJambu,file_tag,imageConvertGrayscale)
    getAllFileInFolder(imdirDaunNangka,file_tag,imageConvertGrayscale)

if __name__ == "__main__":
    main()
