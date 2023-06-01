# import yaml
from os.path import exists
from flask import request, g
from character import player

import json 
import pickle
import yaml

yml_configs = {}
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

def handle_request(sms_client):
    
    act = None
    if exists(f"users/{request.form['From']}.pkl") :
        
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            act = pickle.load(p)
            output = act.get_output(request.form['Body'])

        for o_msg in output:
            
            message = sms_client.messages.create(
                     body=o_msg,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])

    else:
        act = player(request.form['From'],0,100)
        
        om_menu = act.get_mm()
        
        message = sms_client.messages.create(
                     body=om_menu,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])

    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(act, p)

