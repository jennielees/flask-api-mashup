import requests
from config import (TWILIO_ACCOUNT_ID, TWILIO_AUTH_TOKEN,
                    TWILIO_NUMBER, DEFAULT_SMS_NUMBER)


def send_sms(msg):
    url = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".\
        format(TWILIO_ACCOUNT_ID)
    message = {
        'Body': msg,
        'To': DEFAULT_SMS_NUMBER,
        'From': TWILIO_NUMBER
    }

    r = requests.post(url, auth=(TWILIO_ACCOUNT_ID, TWILIO_AUTH_TOKEN),
                      data=message)
    return r.json()
