from FaceExtractor import FaceExtractor
from Trainer import Trainer
from Recognizer import Recognizer
from tkinter import *

win = Tk()
win.title('Recognizer')
win.geometry("700x350")

radio = IntVar()
Label(text="Candidate recognition system from movie!\n\n", font=('Aerial 14')).pack()
Label(text="Select one of the following action you want to perform:", font=('Aerial 11')).pack()
label = Label(win)
label.pack()


def start():
    # Define radiobutton for each options
    r1 = Radiobutton(win, text="Extract Faces", indicatoron=0, width=30, padx=40, pady=5, border=3,
                     variable=radio, value=1, command=selection)
    r1.pack(anchor=N)
    r2 = Radiobutton(win, text="Train the Recognizer", indicatoron=0, width=30, padx=40, pady=5, border=3,
                     variable=radio, value=2, command=selection)
    r2.pack(anchor=N)
    r3 = Radiobutton(win, text="Recognize from the Video", indicatoron=0, width=30, padx=40, pady=5, border=3,
                     variable=radio, value=3, command=selection)
    r3.pack(anchor=N)

    exit_button = Button(win, text="Exit", width=30, padx=40, pady=5, border=3, command=win.destroy,
                         bg='gray80', activebackground='red')
    exit_button.pack(pady=50)
    win.update()
    win.mainloop()


# Define a function to get the output for selected option
def selection():
    selected = radio.get()
    win.update()

    win.destroy()

    if selected == 1:
        print("\nStarting Face Extractor Module...\n")
        face_extractor = FaceExtractor()
        face_extractor.extract_face()

    elif selected == 2:
        print("\nStarting model training...\n")
        trainer = Trainer()
        trainer.train_model()

    elif selected == 3:
        print("\nStarting Recognition module...\n")
        recognizer = Recognizer()
        recognizer.recognize()

    else:
        print("Something is not right. Please try again")
        win.destroy()


if __name__ == '__main__':
    # register = Register()
    # register.take_image()
    # trainer = Trainer()
    # trainer.train_model()
    # tester = Tester()
    # tester.test()
    start()
