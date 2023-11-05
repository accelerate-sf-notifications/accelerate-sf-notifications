import sys
sys.path.append('../../')
import config

from twilio.rest import Client

account_sid = config.vars["twilio"]["account_sid"]
auth_token = config.vars["twilio"]["auth_token"]
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=config.vars["twilio"]["message_from"],
  body=config.vars["twilio"]["message_body"],
  to=config.vars["twilio"]["message_to"]
)

print(message.sid)
