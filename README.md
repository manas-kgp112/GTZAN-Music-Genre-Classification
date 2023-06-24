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

Download the dataset using the [link](https://storage.googleapis.com/kaggle-data-sets/568973/1032238/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230621%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230621T041125Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=36c6abd37d031ca21b47f2831420fb9593b6d2b74871d17dc7c284c076899584846f21236f8ba40d862dffd1df5e752d86ea999aa3e6ced71e96fdc91d977d7b229d59061a6bb05e0e2cb426e168806c816e4cc933b693977230e17874b5ef3e3dc205f9a8be0bb2b0d26195209ccdda718f1bbfcbe310061a2ad3c3100eba38b6593fd5adb2662645c8f7c29c1e0f632de4ad4ad8867c90d449993470106203a8c643adaef071a8a8bb089e26dbc5e8aee2fdc87f773f8195bf26953033ce5813481494d0b6266ab2475f2ae5d91adebc4deaa2c01c0d4ba202844fbaa77db5061dc981f9aae76cb59938d9f87972265ba2aa173f009b6c37b74b92faf2e161) 
below and place the extracted file in
artifacts/data folder. Delete the temp.txt file.


> Remember this is a general idea on how to run the project application. Go through your folder structure once and feel free to change the code accordingly.