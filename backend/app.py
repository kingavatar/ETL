from flask import Flask, jsonify, render_template, request, make_response
from flask_cors import CORS
import os, requests
from ETL_engine_2 import ETLEngine

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# configuration
# DEBUG = True
ROOT_DIR = os.path.dirname(__file__)
DIST_DIR = os.path.join(ROOT_DIR, 'dist')


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index_html(path):
    # if app.debug:
    #     return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template('index.html')

@app.route("/api/xmlFile",methods=['POST'])
def XmlFile():
    if request.method == 'POST':
      data=request.data
      print(data)
      data1 = data.decode('ascii')
      with open("example_2.xml", "w") as text_file:
        text_file.write(data1)
      e = ETLEngine("example_2.xml")
      e.run()
      return make_response("success")

if __name__ == '__main__':
    app.run("0.0.0.0")