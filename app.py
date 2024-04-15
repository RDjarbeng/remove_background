from flask import Flask, render_template, request, redirect, url_for
from rembg import remove  # Import the background removal function
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STATIC_FOLDER'] = STATIC_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Remove background using your remove_bg_safe.py logic
        with Image.open(filename) as input_image:
            output_image = remove(input_image)

        # Save the processed image
        output_filename = os.path.join(app.config['STATIC_FOLDER'], 'output.png')
        output_image.save(output_filename)

        return redirect(url_for('result', filename='output.png'))

@app.route('/result/<filename>')
def result(filename):
    return render_template('result.html', filename=f'{filename}')

if __name__ == '__main__':
    app.run(debug=True)
