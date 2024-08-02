__author__ = "Adnan Karol"
__version__ = "1.0.0"
__maintainer__ = "Adnan Karol"
__email__ = "adnanmushtaq5@gmail.com"
__status__ = "DEV"

# Import libraries
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import yaml
from sklearn import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os
import numpy as np


# Initialize the Flask application
app = Flask(__name__, template_folder="templates")
Bootstrap(app)

# Define the Path to the Config File
path_to_config_file = "config.yaml"


def config_params():
    """
    Load and return configuration parameters from the YAML file.

    Returns:
        tuple: Contains the output directory, image size, and model path.
    """
    with open(path_to_config_file, "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    
    output_dir = cfg["output"]["dir"]
    size = cfg["dimension"]["size"]
    model_path = cfg["path"]["model"]

    return output_dir, size, model_path


def make_predictions(filename):
    """
    Preprocess the image and make predictions using the trained model.

    Args:
        filename (str): The name of the image file to be processed.

    Returns:
        int: The predicted class (0 for Normal, 1 for Pneumonia) or -1 if the file is not an image.
    """
    output_dir, size, model_path = config_params()

    # Check if the file is an image
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        return -1

    # Preprocess the image
    image_path = os.path.join(output_dir, filename)
    image = load_img(image_path, target_size=(size, size))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # Make the prediction
    model = load_model(model_path)
    predictions = model.predict(image)
    predictions = np.argmax(predictions[0])

    return predictions


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """
    Handle file upload and display prediction results.

    Returns:
        str: The rendered HTML template based on the request method and file upload status.
    """
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
                output = "Pneumonia Chest X-Ray Image. Please visit a doctor for verification!"
            else:
                output = "Please recheck your input image!"
            
            path_to_image = url_for('static', filename=filename)
            print(path_to_image)
            result = {
                'output': output,
                'path_to_image': path_to_image,
                'size': size
            }

            return render_template('show.html', result=result)
    
    return render_template('index.html')


# Run the application
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
