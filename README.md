# GrantYourRequest
Website Design for GrantYourRequest.com

Resources:
1) https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
2) https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
3) https://console.aws.amazon.com/route53
4) https://console.aws.amazon.com/elasticbeanstalk

Instructions:

Download/Install
1) Python 2.7 for Macbook Pro
2) Pip for terminal; ON MAC: sudo easy_install pip
3) Install GIT via pip
3) Install virtualenv via pip
4) Install awsebcli via pip
5) Clone Repo; ON MAC: git clone {REPO}

Commands:
# Create a virtualenv
virtualenv eb-virt

# Activate the virtual environment
Windows: eb-virt\Scripts\Activate
Mac:    source eb-virt/bin/activate

# Install packages
pip install -r requirements.txt

# Navigate to the flask application directory
cd eb-flask

# Test Flask Application before deploying
python application.py

# deploy the applicatino on elastic beanstalk to 
eb deploy

# Launch the Application
eb open 

# Deactivate the Virtual Environment
deactivate

If you accidently hit ctrl-Z on mac instead of ctrl-C to stop flask app.
You will need to kill the process;
1) lsof -i :5000  <---get the PID (second from left)
2) kill -9 PID
