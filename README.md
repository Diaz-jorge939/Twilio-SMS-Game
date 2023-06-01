# Flask App with Twilio Integration

This repository contains a Flask application integrated with Twilio for handling SMS messages. Follow the instructions below to set up and run the application.

## Instructions
Create a Twilio Account: Sign up for a Twilio account at https://www.twilio.com/. Note down the following credentials: phone_number, auth_token, and account_sid. These will be used in the configuration.

### Install Dependencies: 
Install the required dependencies by running the following command:
``` 
pip install -r requirements.txt 
```
### Download Ngrok 
Download Ngrok from the official website at [https://ngrok.com/](https://ngrok.com/). Ngrok is used to create a secure tunnel to your local Flask app so you can run locally

### Configuration
Create YAML Configuration: Create a config.yml file in the project directory and add the following content:

```
twilio:
  phone_number: "<your_twilio_phone_number>"
  auth_token: "<your_twilio_auth_token>"
  account_sid: "<your_twilio_account_sid>"
```
Replace <your_twilio_phone_number>, <your_twilio_auth_token>, and <your_twilio_account_sid> with the corresponding values from your Twilio account.
 
Note: Do not upload this file to version control or public repositories as it contains sensitive information.


### Run Flask App
Start the Flask app by running the following command:

```
python app.py 
```

### Run Ngrok in separate terminal 
Open a new terminal or command prompt window, navigate to the directory where Ngrok is located, and run the following command to expose your local server:

```
./ngrok http 5000
```
### Twilio Message Configuration

In your Twilio account dashboard, go to the "Phone Numbers" section, select the phone number you want to use, and configure the Messaging webhook to the Ngrok forwarding URL (https://<INSERT YOUR NGROK URL HERE>/sms).

This is so when your twilio phone number recieves a message twilio sends an HTTP request to your local computer 

## Usage 
 With the Flask app running and Ngrok tunnel active, you can now send SMS messages to your Twilio phone number and receive them in your Flask app. The incoming messages will be processed based on your app logic.

## Acknowledgments

Thank you to Professor Cary Jardin for Project idea. As well as a special thank you to contributors Chloe Aromin @C-PU and Kyle Garrett @ayirac
