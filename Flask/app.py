from flask import Flask, request, render_template, jsonify
import os
import numpy as np
from tensorflow.keras.preprocessing import image
import tensorflow as tf

# Initialize Flask app
app = Flask(__name__)

# Ensure 'uploads' directory exists
if not os.path.exists('./uploads'):
    os.makedirs('./uploads')

# Load the pre-trained model
model = tf.keras.models.load_model('dog1_bree d_cnn_model.h5')

# Class names (your list remains unchanged)
class_names = ['affenpinscher', 'Afghan_hound', 'African_hunting_dog', 'Airedale',
               'American_Staffordshire_terrier', 'beagle', 'boxer', 'bulldog', 'chihuahua',
               'golden_retriever', 'labrador_retriever', 'poodle', 'pug', 'rottweiler',
               'siberian_husky', 'yorkshire_terrier']

# Allowed image extensions
allowed_extensions = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/breed')
def breed_info():
    return render_template('breed.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')

    if request.method == 'POST':
        try:
            img_file = request.files.get('image')
            if not img_file or not allowed_file(img_file.filename):
                return jsonify({'error': 'Please upload a valid image (jpg, jpeg, png).'})

            img_path = './uploads/' + img_file.filename
            img_file.save(img_path)

            img = image.load_img(img_path, target_size=(150, 150))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)
            predicted_class_index = np.argmax(prediction, axis=1)
            predicted_class_name = class_names[predicted_class_index[0]]

            os.remove(img_path)

            return render_template('result.html', prediction=predicted_class_name)

        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

