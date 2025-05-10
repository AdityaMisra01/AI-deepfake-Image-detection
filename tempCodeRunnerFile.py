import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit

# Load trained model
model = load_model('optimized_model1.h5')
IMG_SIZE = (128, 128)  # Must match training size

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0
    if img_array.shape[-1] == 4:  # Handle RGBA images
        img_array = img_array[..., :3]
    return np.expand_dims(img_array, axis=0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if file was uploaded
        if 'file' not in request.files:
            return redirect(request.url)
            
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            # Save uploaded file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Make prediction
            try:
                processed_img = preprocess_image(filepath)
                prediction = model.predict(processed_img)[0][0]
                confidence = round(float(prediction * 100 if prediction > 0.5 else (1 - prediction) * 100), 2)
                result = "AI Generated" if prediction > 0.5 else "Real"
                
                return render_template('index.html',
                                     result=result,
                                     confidence=confidence,
                                     filename=filename)
            except Exception as e:
                return render_template('index.html',
                                     error=str(e))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)