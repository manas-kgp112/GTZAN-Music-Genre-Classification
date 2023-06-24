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


### Folder Structure
Here is the screenshot if how the folder structure looks like

![Folder Structure Image](/custom_img/root.jpg)

1) artifacts : Contains all the input and output data related to the project (input data, final models, preprocessor files etc.)

3) notebook : Contains the jupyter notebooks used as the base for creating the models and pipelines.

4) src : This is the main folder of the project, it contains all the scripts for running our project such as data_inigestion pipelines, data_transformation pipelines, model_training pipelines etc.It also contains 
all the custom logs and configuration files.

5) config : Contains configuration and parameters yaml files.


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


> Remember this is a general idea on how to run the project application. Go through your folder structure once and feel free to change the code accordingly.