# Recognition of characters from a movie or video

In this project, we will recognize characters from video and store their appearance time from video in a csv file. 
Bellow steps are to follow to run the project

N.B. It is recommended to start with a new virtual environment
## Run Locally

### Clone the project

```bash
  git clone https://github.com/Mustafiz48/recognition_in_video.git
```
or you can also download the project with the gitHub repo link

After you download / clone the project, you need to do some prerequisite tasks.

1. First check the "Appearance" folder. Initially this folder will contain a .csv file. This is the final result file. You should delete the existing csv. It will be generated for your video after you run the program.
2. Second in the "TrainImageLabel" folder, there will be a "Trainer.yml" file. This file stores the training data. Remember the file name. Delete this file and create a new "Trainer.yml" file(The same file, but create it newly). After you create the file, there will be nothing inside it, but after you have trained the model, training data will be stored here. You can check the file size before and after training.
3. Third, check the "TrainingImage" folder. Initially this folder will contain other folders named 1, 2, 3 etc. If you open those folder, you will see extracted faces inside those folders (In one folder, all the faces of one person, in another folder, faces of another person). Remember the folders naming structure(1, 2, 3 etc. just numbers). Now delete all the folders inside "TrainingImage" folder. After you extract faces from your video, you will see all the extracted faces inside this "TrainingImage" folder.
All the faces will be in one place, and they won't be categorized. You have to make new folders as previous (named 1, 2, 3 etc. The folder names must be integer numbers) and arrange the extracted faces according to folders (One folder for one character). I know this is some **boring, manual** task. But this task ensures the accuracy. If I was to automate w.r.t some pictures, accuracy wouldn't be guaranteed. 
4. Now check "Id_Name_Mapping" folder. You will find an id_mapping.csv file. Edit this file where value of 'Id' will be the folder name inside 'TrainingImage' folder(1, 2, 3 etc.) and value of 'Name' will be corresponding character name. Double-check the first line of this file, it should always be "Id,Name".
5. Check the video path in FaceExtractor.py
   * self.video_path = "crush.mp4"
    
    Change this video path accordingly. 


Now let's continue!

### Go to the project directory

```bash
  cd project_directory
```

### Install dependencies

```bash
  pip install -r requirements.txt
```

### Run the code

```bash
  python main.py
```

After you run the code, a GUI will pop up with three options. 
* Extract Faces
* Train the recognizer
* Recognize from the video

You have to follow the options one after another. First Chose **_Extract Faces_**. It will extract all the faces from video in 'TrainingImage' folder. Check step **3** mentioned above.

run _**python main.py**_ again. This time select the second option, **_Train the recognizer_**. It will train the recognition model and store the training data in "Trainer.yml" file. 

Again, run the _**python main.py**_ for third time. This time select the third option **_Recognize from the video_**. It will create an 'Appearance_sheet.csv' file inside "Appearance" folder. This will be our final output. 
After the program is finished, if you open the Appearance_sheet.csv file, you will find it contains character name and their appearance time in the video. 


## Extras
### Convert result format from second to h: m: s 

```
  python seconds_to_minutes.py
```

### See graphs, plots, appeared character in a time slice, appearance counts etc.
```
  python show_plots.py -st 220 -et 242
```
or 
```
  python show_plots.py --start_time 220 --end_time 242
```
the values of start_time and end_time (220 and 241) represents the range of time you want to analyze. 
**_To analyze the complete video, give -1 for any or both options._**
