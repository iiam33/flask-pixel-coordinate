from importlib.abc import ResourceLoader
from flask import render_template, request
from flask_restful import Api, Resource
from app import app
from file_api import upload_file

api = Api(app)

# class File(Resource):
#     def get():
#         return {}
    
#     def post(self):
#         return {}

# api.add_resource(File, "/")

@app.route('/', methods=['GET','POST'])
def init():
    if request.method == 'POST':
        upload_file()
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)