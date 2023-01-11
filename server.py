from flask import Flask, render_template,send_from_directory, request
from waitress import serve

from Textwriter import Textwriter

import logging


logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
	print(request)
	return render_template('index.html',last_lineCount = 8,last_topic = "")

@app.route('/handle_data', methods=['POST'])
def handle_data():
	topic = request.form['topic']
	print("topic: "+topic)
	lineCount = request.form['lines']
	writer = Textwriter(topic,int(lineCount))
	text = writer.writeText()
	return render_template('index.html',result=text, last_lineCount = lineCount, last_topic = topic)

@app.route('/index.css')
def css():#
	return send_from_directory("templates", "index.css")

if __name__ == '__main__':
	serve(app, port=50100, threads=1)