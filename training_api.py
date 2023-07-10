import uuid 
import os
import time
import cv2
import torch
import matplotlib.pyplot as plt
from time import sleep
import tkvideo as tkv
import tkinter as tk
from tkinter import *
import customtkinter as ctk
import numpy as np
import pandas as pd

from PIL import Image, ImageTk



img_path = os.path.join('data', 'images')
img_labels = ['awake', 'drowsy']
number_imgs = 20



api_root=tk.Tk()
api_root.geometry("640x608")
api_root.title("Project Accident")
ctk.set_appearance_mode("dark")
api_label=tk.Label(api_root, text="Welcome To Project Accident")
api_label.pack()

def train_data():
 camFrame=tk.Frame(height=1280,width=720)
 camFrame.pack()
 cam_vid=ctk.CTkLabel(camFrame)
 cam_vid.pack()
 capture_vid=cv2.VideoCapture(0)
 capture_vid.set(3,640)
 capture_vid.set(4,480)

 for label in img_labels:
  print('Image Collection for < >'.format(label))
  time.sleep(5)
	    
  for img_num in range(number_imgs):
	   
   print('Image Collection for < >, image number < >'.format(label, img_num))
					
   ret, frame = capture_vid.read()
						
   imgname = os.path.join(img_path, label+'.'+str(uuid.uuid1())+'.jpg')
						
   cv2.imwrite(imgname, frame)
					
   cv2.imshow('Collection of Images', frame)
				
   time.sleep(1)
				
   if cv2.waitKey(10) & 0xFF == ord('q'):
    break
 capture_vid.release()
 cv2.destroyAllWindows()
 for label in img_labels:
  print('Image Collection for < >'.format(label))
  for img_num in range(number_imgs):
   print('Image Collection for < >, image number < >'.format(label, img_num))
   imgname = os.path.join(img_path, label+'.'+str(uuid.uuid1())+'.jpg')
   print(imgname)
   
   
train_button=tk.Button(api_root,text="Train Model for Drowsiness",command=train_data,padx=6, pady=6, bg='cyan',height=6)
train_button.pack()

api_root.mainloop()   
