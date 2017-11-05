from flask import Flask, render_template, request
import os

# EB looks for an 'application' callable by default.
# EB looks for an 'application' callable by default.
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'Templates')
application = Flask(__name__, template_folder=template_path, static_url_path="", static_folder="Static")

mail=Mail(application)

# use decorators to link the function to a url
@application.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
	
@application.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

# run the app.
if __name__ == "__main__":
	# Setting debug to True enables debug output. This line should be removed before deploying a production app.
	application.run(debug=False)  