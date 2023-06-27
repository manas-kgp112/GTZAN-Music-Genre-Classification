# GTZAN-Music-Genre-Classification


### Outlines of the project
1) Setup github repository and virtual environment (extras : requirements.txt, setup.py, template.py, main.py)
2) Creating aligned folder structure (src, components) to build packages
3) Custom Exception , Logger and utilities script.
4) All sub-modules of project are in form Jupyter Notebook @{res/}
5) Creating "data_ingestion" and "data_transformation" etc. modules.
6) Saving vizualizations/performance in @{artifacts/plots} and @{artifacts/performance}
7) Creating pipelines for train and validation sets.
8) Model creation and training on all the sets available.
9) Saving models as .pkl file


### Agenda/Procedure

This project/classifier is broadly divided into 2 sub-parts, data_extraction and model_fitting. Firstly 
features are extracted using the "librosa" library and stored separately. Then they are used to train custom Concoluational Network(s).

*This project has 2 sides:*

-> This project has been trained on the csv files given with dataset already having the extracted features. The complete code for that project lies in the [res/genreClassification](./res/GenreClassification.ipynb) file.

-> This project has also been trained on the features extracted from the audio files and using custom CNN models. The main project itself is the code for this.


### Folder Structure
Here is the screenshot if how the folder structure looks like

![Folder Structure Image](/custom_img/root.jpg)

Below are the detailed descriptions of the sub-directories of the project.

<------   EOS   -------->

1. artifacts : Contains all the input and output data related to the project (input data, final models, preprocessor files etc.).

>This github repository doesn't contain the folder "artifacts". While cloning the repository, create a folder named "artifacts" and structure it using the steps given below.

![artifacts folder structure](/custom_img/artifacts.jpg)

**-> data : 3 folders & 2 files**

- features (folder) : contains the extracted features {spectrogram, mfcc, zcr etc.} in .npz format

- genres_original : contains all the audio files in .mp3 format

- images_original : some extracted feature images given with extracted dataset.

- 2 csv's already with dataset


**-> models : 3 models**

- contains the saved models after training.

**-> performance : .txt files**

- contains performance metrics for models trained on data using the csv's (not the extracted features)

**-> plots : .png files**

- contains confusion matrix for the final ensemble model trained on extracted features.

** -> transformed_data : 2 .csv **

- contains csv files of transformed data while training models using csv data.

<------   EOS   -------->

2. res : Contains the jupyter notebooks used as the base for creating the models and pipelines. Contains 4 notebooks. [GenreClassification.ipynb](./res/GenreClassification.ipynb) is trained with dataset csv's and rest are with extracted features.

<------   EOS   -------->

3. src : This is the main folder of the project, it contains all the scripts for running our project such as data_inigestion pipelines, data_transformation pipelines, model_training pipelines etc.It also contains 
all the custom logs and configuration files.

<------   EOS   -------->

4. config : Contains configuration and parameters .yaml files.

<------   EOS   -------->

5. logs: contains all the log files


### How to test the project application?

Open Gitbash in the directory in which you want the project to be placed.

Write the following commands in the bash terminal : 

```
git clone git@github.com:manas-kgp112/GTZAN-Music-Genre-Classification.git .
conda create -p venv python=3.9.16 -y
conda activate venv/
touch artifacts/data/temp.txt
```

Download the dataset using the [link](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification/download?datasetVersionNumber=1) 
below and place the extracted file in
artifacts/data folder. Delete the temp.txt file.


> Remember this is a general idea on how to run the project application. Go through your folder structure once and feel free to change the code accordingly. Add all the folders accoring to descriptions given above.