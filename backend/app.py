from flask import Flask, jsonify, render_template, request, make_response
# from flask.helpers import flash
from flask_cors import CORS
import os, requests
from ETL_engine_2 import ETLEngine
from flask_socketio import SocketIO,send,emit

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.secret_key = "KingAvatar secret key"
app.config['SECRET_KEY'] = 'KingAvatar secret key'
# app.config['SERVER_NAME']="ETLServer"
# configuration
# DEBUG = True
ROOT_DIR = os.path.dirname(__file__)
DIST_DIR = os.path.join(ROOT_DIR, 'dist')

jinja_options= app.jinja_options.copy()
jinja_options.update(dict(
  variable_start_string="(%",
  variable_end_string="%)",
))

app.jinja_options = jinja_options
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
# @socketio.on('message')
# def handle_message(message):
#     send(message)

# @socketio.on('json')
# def handle_json(json):
#     send(json, json=True)


# sanity check route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index_html(path):
    # flash(u'Flash Trying Blah', 'success')
    # if app.debug:
    #     return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template('index.html')



@app.route("/api/toast")
def Toast(msg="Sending Ping from Server",typ="success"):
      socketio.emit('toast', {'msg':msg,'type':typ})
      return make_response("success")

@app.route("/api/xmlFile",methods=['POST'])
def XmlFile():
    if request.method == 'POST':
      data=request.data
      print("Running on ",data)
      data1 = data.decode('ascii')
      with open("example_2.xml", "w") as text_file:
        text_file.write(data1)
      e = ETLEngine("example_2.xml",socketio)
      msg,typ = e.run()
      Toast(msg,typ)
      return make_response("success")

if __name__ == '__main__':
    # app.run("0.0.0.0")
    socketio.run(app, host="localhost")