import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os

train_name_list= train_df["image_name"]
test_name_list= test_df["image_name"]
    
        
    
for i in train_name_list:
    image_name = "../7001/input/jpeg/train/" + i
    # Resize image and maintain aspect ratio
    img = Image.open(image_name)
    width, height = img.size
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    new_dir = "../7001/input/new/train/" + i
    img.save(new_dir)
    
for i in test_name_list:
    image_name = "../7001/input/jpeg/train/" + i
    # Resize image and maintain aspect ratio
    img = Image.open(image_name)
    width, height = img.size
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    new_dir = "../7001/input/new/test/" + i
    img.save(new_dir)
      
