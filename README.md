# Pneumonia_XRay_Classification
A project to classify Chest X-Ray images, to detect if Pneumonia is present or not, and to deploy it using Flask and Docker.


# Table of Contents
1. [ Dataset ](#data)
2. [ Model ](#model)
3. [ Model Training ](#Using)
4. [ Model Deployment ](#Future_scope) 
5. [ Additional Information ](#info)

## Repository Contents
The repository contains the following Files and Folders

1. Training_Notebook.ipynb: Notebook containing training codes for Chest X-Ray images classification, to detect if Pneumonia is present or not.
2. Dockerfile: Docker File for Deployment.
3. requirements.txt: Contains various packages and dependencies required for the project.
4. config.yaml: Configuration file for changing variables and paths of the project.
5. app.py: Backend for web application deployment using flask.
6. templates: Frontend for web application deployment using flask.
7. .gitignore: List of Files or Folders to be ignored by git.
8. Images: Sample Output Screenshots.


<a name="data"></a>
# Dataset

Dataset is taken from Kaggle: https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

    Kermany, Daniel; Zhang, Kang; Goldbaum, Michael (2018), “Labeled Optical Coherence Tomography (OCT) and Chest X-Ray Images for Classification”, Mendeley Data, V2, doi: 10.17632/rscbjbr9sj.2

<a name="model"></a>
# Model

A Convolutional Neural Network (CNN) based deep-learning architecture is used to solve the classification problem. The overall number of paramaters in the the training network are 78,017. This architecture consists of Convolutional (7)
and Pooling Layers (7). Towards the end there are 3 Dense and Dropout layers to solve the classification problem.
The model is taken from https://github.com/Karan-Malik/ConvNet .

## Input Images
The Input images are converted to 128 * 128 sized images for standarization purpose. The end goal is to classify if the X-Ray image is of a normal person or with a person suffering with pneunomia. 


<a name="using"></a>
# Model Training

1.  Open command line cmd at the root of the repository.

2.  Run the command   

    `pip install -r requirements.txt` 

3. Open the Notebook `Training_Notebook.ipynb` to follow all the preprocessing and training steps of the model.


NOTE:  In order to make path, variables or any related change, please change the `config.yaml` file. 

<a name="Model Deployment"></a>
# Model Deployment

1. A `Dockerfile` is provided which can be used for deployment. From this `Dockerfile` a docker image can be created and deployed in cloud, etc.

    1. To create a docker image, first download docker for your OS from the official docker website.
    
    2. Then, open a command line cmd at the root of the repository, and run the command: `docker build -t pneumonia_classification_image:v1 .`

    3. Once the image is created, you can push the docker image to the docker hub after signing in, from where the image can be used.

    4. To run the docker image, open a command line cmd at the root of the repository, and run the command: `docker run -p 5000:5000 pneumonia_classification_image:v1`

    5. Open the link on your preffered browser: `http://127.0.0.1:5000/`, or check the logs provided by Docker in command line, to find the link.

2. Also a seperate `templates` and `app.py` is provided which can serve as frontend and backend for uploading an image on a web application and getting back a prediction.

    To run the application, open a command line cmd at the root of the repository, and run the command: `flask run`

3. In the future all models can be stored on cloud for sending a `request` and getting a `response` for demand prediction.

4. Samples of deployed images are shown below.


<a name="Version"></a>

<a name="info"></a>
# Additional Information
## Python Version
The whole project is developed with python version `Python 3.7.7` and pip version `pip 19.2.3`.
## Contact
In case of error, feel free to contact us over Linkedin at [Adnan](https://www.linkedin.com/in/adnan-karol-aa1666179/) and [Niloy](https://www.linkedin.com/in/niloy-chakraborty/).
