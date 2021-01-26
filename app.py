from flask import Flask, flash, redirect, render_template, \
     request, url_for,Response, jsonify, send_from_directory




UPLOAD_FOLDER = '/var/www/coeaiweb/coeaiweb/static/img'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


application = app = Flask(__name__)

@app.route("/")
def home():

	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)