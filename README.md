# GrantYourRequest
Website Design for GrantYourRequest.com

Resources:
1) https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
2) https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
3) https://console.aws.amazon.com/route53
4) https://console.aws.amazon.com/elasticbeanstalk

Instructions:

Download/Install
1) Python 3.4 for Macbook Pro
2) Pip for terminal
3) virtualenv
4) awsebcli
5) GIT

Clone Repo

Commands:
# Create a virtualenv
virtualenv eb-virt

# Activate the virtual environment
eb-virt\Scripts\Activate

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