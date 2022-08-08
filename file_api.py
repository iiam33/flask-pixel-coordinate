import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		response = jsonify({'message' : 'No file part in the request'})
		response.status_code = 400
		return response
	file = request.files['file']
	if file.filename == '':
		response = jsonify({'message' : 'No file selected for uploading'})
		response.status_code = 400
		return response
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		response = jsonify({'message' : 'File successfully uploaded'})
		response.status_code = 201
		return response
	else:
		response = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		response.status_code = 400
		return response