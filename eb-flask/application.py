from flask import Flask

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', lambda: "Under Construction")

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:"yo"))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be removed before deploying a production app.
    application.run(debug=True)