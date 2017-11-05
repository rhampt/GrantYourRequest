from flask import Flask, render_template, request
from flask.ext.mail import Message, Mail
import os

# EB looks for an 'application' callable by default.
# EB looks for an 'application' callable by default.
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'Templates')
application = Flask(__name__, template_folder=template_path, static_url_path="", static_folder="Static")


application.config["MAIL_SERVER"] = "smtp.gmail.com"
application.config["MAIL_PORT"] = 465
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = 'grantyourreq@gmail.com'
application.config["MAIL_PASSWORD"] = 'Oops'

mail=Mail(application)

# use decorators to link the function to a url
@application.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		msg = Message("Message from website(person = " + str(request.form["name"]) +")", sender='grantyourreq@gmail.com', recipients=['grantyourreq@gmail.com'])
		msg.body = """
		From: %s
		Phone Number: %s
		Email: %s
		Message:
		%s
		""" % (str(request.form["name"]), str(request.form["phone"]), str(request.form["email"]), str(request.form["message"]))
		mail.send(msg)
		return 'Form posted.'
	
@application.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

# run the app.
if __name__ == "__main__":
	# Setting debug to True enables debug output. This line should be removed before deploying a production app.
	application.run(debug=False)  