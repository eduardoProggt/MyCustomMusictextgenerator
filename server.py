from flask import Flask, render_template,send_from_directory, request
from waitress import serve

from Textwriter import Textwriter

import logging


logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("NTV/ntv.html")

@app.route('/<cssFile>.css')
def renderCss(cssFile):
	return send_from_directory("templates/NTV/",cssFile+".css")

@app.route('/<pngFile>.png')
def renderPng(pngFile):
	return send_from_directory("templates/NTV/",pngFile+".png")

@app.route('/<jpgFile>.jpg')
def renderJpg(jpgFile):
	return send_from_directory("templates/NTV/",jpgFile+".jpg")

@app.route('/mcmDB')
def mcmDB():
	print(request)
	print(request.remote_addr, "hat sich raufgeschaltne")
	return render_template('index.html',lineCount = 8,last_topic = "")

@app.route('/handle_data', methods=['POST'])
def handle_data():
	topic = request.form['topic']
	print("topic: "+topic)
	lineCount = request.form['lines']
	#Das wesentliche:
	writer = Textwriter(topic,int(lineCount))
	text = writer.writeText()
	#
	return render_template('index.html',result=text, lineCount = lineCount, last_topic = topic)


if __name__ == '__main__':
	serve(app,port=50100, threads=2,url_scheme='https')