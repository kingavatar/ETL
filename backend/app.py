from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os, requests

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


if __name__ == '__main__':
    app.run("0.0.0.0")