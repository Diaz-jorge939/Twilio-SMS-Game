from flask import Flask, request, redirect, render_template,g
import os
from twilio.rest import Client
from twillio_webhook import handle_request
import yaml


yml_configs = {}
with open('config.yml', 'r') as yml_file:
    config = yaml.safe_load(yml_file)

app = Flask(__name__)

#g is flask for a global var storage 
def init_new_env():
    auth_token = config['twillio']['auth_token']
    account_sid = config['twillio']['account_sid']

    g.sms_client = Client(account_sid, auth_token)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    
    init_new_env()
    handle_request(g.sms_client)

    return ""

if __name__ == "__main__":
    app.run(debug=True)
