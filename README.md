# PneumoniaAIClassifier

A comprehensive project for classifying chest X-ray images to detect pneumonia using a Convolutional Neural Network (CNN). This project includes model training, deployment via Flask, and Docker.

## Table of Contents

1. [Dataset](#dataset)
2. [Model](#model)
3. [Model Training](#model-training)
4. [Model Deployment](#model-deployment)
5. [Additional Information](#additional-information)

## Repository Contents

- **Training_Notebook.ipynb**: Jupyter notebook for training the CNN model on chest X-ray images.
- **Dockerfile**: Docker configuration file for containerizing the application.
- **requirements.txt**: List of Python dependencies required for the project.
- **config.yaml**: Configuration file for setting paths and variables.
- **app.py**: Flask application backend for serving predictions.
- **templates/**: Directory containing HTML templates for the web application.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **Images/**: Directory with sample output screenshots.

## Dataset

The dataset is sourced from Kaggle: [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).

**Citation**: Kermany, Daniel; Zhang, Kang; Goldbaum, Michael (2018). “Labeled Optical Coherence Tomography (OCT) and Chest X-Ray Images for Classification.” Mendeley Data, V2, doi: 10.17632/rscbjbr9sj.2.

## Model

The project employs a Convolutional Neural Network (CNN) for classification. The architecture includes:

- **Convolutional Layers**: 7
- **Pooling Layers**: 7
- **Dense Layers**: 3
- **Dropout Layers**: Several to prevent overfitting

The model, inspired by [ConvNet](https://github.com/Karan-Malik/ConvNet), utilizes 78,017 parameters. Input images are resized to 128x128 pixels for standardization.

## Model Training

1. Open a command line interface at the root of the repository.
2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
3. Open and execute the `Training_Notebook.ipynb` to follow the preprocessing and training steps.

**Note**: Modify paths and variables in the `config.yaml` file as needed.

## Model Deployment

1. **Docker Deployment**:
    - Install Docker from the [official website](https://www.docker.com/).
    - Build the Docker image:
      ```sh
      docker build -t pneumonia_classification_image:v1 .
      ```
    - Run the Docker container:
      ```sh
      docker run -p 5000:5000 pneumonia_classification_image:v1
      ```
    - Access the web application at `http://127.0.0.1:5000/`.

2. **Flask Deployment**:
    - Start the Flask application:
      ```sh
      flask run
      ```

3. **Future Scope**:
    - Plan to integrate cloud storage for models and implement API endpoints for predictions.

## Additional Information

- **Python Version**: 3.7.7
- **Pip Version**: 19.2.3

### Contact

For queries or issues, reach out via LinkedIn:
- [Adnan Karol](https://www.linkedin.com/in/adnan-karol-aa1666179/)
- [Niloy Chakraborty](https://www.linkedin.com/in/niloy-chakraborty/)
