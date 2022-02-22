# Test Sending SMS Messages:

import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

client.messages.create(
	to = os.environ["My_PHONE_NUM"]
	from_ = "PHONE_NUM_FROM_TWILIO"
	body = "test, this was sent with python"
)