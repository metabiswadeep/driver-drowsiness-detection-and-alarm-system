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
labels = ['awake', 'drowsy']
number_imgs = 20


api_root=tk.Tk()
api_root.geometry("640x608")
api_root.title("Project Accident")
ctk.set_appearance_mode("dark")
api_label=tk.Label(api_root, text="Welcome To Project Accident")
api_label.pack()

def detection_cam():
 camFrame=tk.Frame(height=1280,width=720)
 camFrame.pack()
 cam_vid=ctk.CTkLabel(camFrame)
 cam_vid.pack()
 model=torch.hub.load('ultralytics/yolov5', 'custom', path='../yolov5/runs/train/exp5/weights/last.pt',force_reload=True)
 capture_vid=cv2.VideoCapture(0)
 capture_vid.set(3,640)
 capture_vid.set(4,480)

 def cam_init():
  ret,frame=capture_vid.read()
  frame= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
  results=model(frame)
  img= np.squeeze(results.render())
  imagarr= Image.fromarray(img)
  imgtk=ImageTk.PhotoImage(imagarr)
  cam_vid.imgtk=imgtk
  cam_vid.configure(image=imgtk)
  cam_vid.after(1,cam_init)
		
 cam_init()

train_button=tk.Button(api_root,text="Start Drowsiness Detection",command=detection_cam,padx=6, pady=6, bg='cyan',height=6)
train_button.pack()

api_root.mainloop()
