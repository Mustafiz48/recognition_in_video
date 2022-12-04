import warnings
import csv

from tkinter import *
from tkinter import messagebox
import numpy as np
import cv2
import pandas as pd
import datetime
import time

import moviepy.editor as mpy


warnings.filterwarnings("ignore")


class Recognizer:
    def __init__(self):
        self.modelFile = r"Models/res10_300x300_ssd_iter_140000.caffemodel"
        self.configFile = r"Models/deploy.prototxt.txt"
        self.net = cv2.dnn.readNetFromCaffe(self.configFile, self.modelFile)
        self.trainimagelabel_path = "TrainingImageLabel/Trainer.yml"
        self.mapping_path = ("Id_Name_Mapping/id_mapping.csv")
        self.appearance_path = "Appearance/Appearance_sheet.csv"
        self.video_path = "crush.mp4"
        self.name = None
        self.id_ = None

    def recognize(self):
        print("Starting recording timestamp...")
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            try:
                recognizer.read(self.trainimagelabel_path)
            except:
                e = "Model not found,please train model"
                print(e)
            df = pd.read_csv(self.mapping_path)

            video_ = mpy.VideoFileClip(self.video_path)
            for i, (tstamp, im) in enumerate(video_.iter_frames(with_times=True)):
                if i % 5 == 0:
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    h, w = im.shape[:2]
                    try:
                        blob = cv2.dnn.blobFromImage(cv2.resize(im, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
                        self.net.setInput(blob)
                        faces = self.net.forward()
                    except Exception as e:
                        print(e)
                        continue
                    for i in range(faces.shape[2]):
                        confidence = faces[0, 0, i, 2]
                        if confidence > 0.5:
                            box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                            (x, y, x1, y1) = box.astype("int")
                            try:
                                temp_id, distance = recognizer.predict(gray[y: y1, x: x1])
                            except Exception as e:
                                print(e)
                                continue
                            if distance < 55:
                                self.id_ = temp_id
                                try:
                                    self.name = df.loc[df["Id"] == self.id_]["Name"].values[0]
                                except Exception as e:
                                    print("No entry found at id_mapping.csv", e)

                                try:
                                    with open(self.appearance_path, 'a') as f:
                                        writer = csv.writer(f)
                                        writer.writerow([self.name, tstamp])
                                except Exception as e:
                                    print("Error in reading csv file. Exception: ", e)
                            else:
                                continue
        except Exception as e:
            print(e)
