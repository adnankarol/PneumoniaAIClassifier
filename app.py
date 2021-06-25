# Import libraries
from flask import Flask, render_template, request, url_for
from numpy.core.numeric import outer
import pandas as pd
import yaml
from sklearn import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import flask
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os
import numpy as np


# Initialize the flask App
app = Flask(__name__, template_folder = "templates")
Bootstrap(app)

# Define the Path to the Config File
path_to_config_file = "config.yaml"


def config_params():

    with open(path_to_config_file, "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    
    output_dir = cfg["output"]["dir"]
    size = cfg["dimension"]["size"]   
    model_path = cfg["path"]["model"]               

    return output_dir, size, model_path


# Function to get Last 48 hours data for all households and Predict for the next hour
def make_predictions(filename):

    output_dir, size, model_path = config_params()

    # Check if File is an Image
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        return -1

    # Preprocess the Image
    image = load_img(os.path.join(output_dir, filename), target_size = (size, size))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # Make the Prediction
    model = load_model(model_path)
    predictions = model.predict(image)
    predictions = np.argmax(predictions[0])

    return predictions


# Default page of the web-app
@app.route('/', methods=['GET', 'POST'])
def upload_file():

    output_dir, size, model_path = config_params()

    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print('No selected file')
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            file.save(os.path.join(output_dir, filename))
            output = make_predictions(filename)

            if output == 0:
                output = "NORMAL Chest X-Ray Image ;)"
            elif output == 1:
                output = "Pneumonia Chest X-Ray Image. Please visit a Doctor and Verify !! "
            else:
                output = "Please Recheck your input Image !!"
            path_to_image = url_for('static', filename = filename)
            print(path_to_image)
            result = {
                'output': output,
                'path_to_image': path_to_image,
                'size': size
            }

            return render_template('show.html', result=result)
            
    return render_template('index.html')


# To use the Submit button in the web-app
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)