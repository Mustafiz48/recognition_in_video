import csv
import os
import cv2
import numpy as np


class FaceExtractor:
    def __init__(self):
        self.modelFile = r"Models/res10_300x300_ssd_iter_140000.caffemodel"
        self.configFile = r"Models/deploy.prototxt.txt"
        self.net = cv2.dnn.readNetFromCaffe(self.configFile, self.modelFile)
        self.trainimage_path = "TrainingImage/"
        self.trainimagelabel_path = "TrainingImageLabel/Trainner.yml"
        self.student_detail_path = "StudentDetails/studentdetails.csv"
        self.attendance_sheet = "Attendance/Attendance_sheet.csv"
        self.video_path = "crush.mp4"

    # take Image of user
    def extract_face(self):
        frame_num = 0
        try:
            cam = cv2.VideoCapture(self.video_path)
            # detector = cv2.CascadeClassifier(self.haarcasecade_path)
            sample_num = 0
            path = self.trainimage_path
            ok, img = cam.read()

            while ok:

                ok, img = cam.read()
                frame_num += 1
                if frame_num % 50 == 0:
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    h, w = img.shape[:2]
                    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
                    self.net.setInput(blob)
                    faces = self.net.forward()
                    for i in range(faces.shape[2]):
                        confidence = faces[0, 0, i, 2]
                        if confidence > 0.6:
                            sample_num = sample_num + 1
                            box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                            (x, y, x1, y1) = box.astype("int")
                            try:
                                cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
                                cv2.imwrite(f"{path}" + str(sample_num) + ".jpg", gray[y:y1, x: x1], )
                            except:
                                continue

            cam.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(e)
