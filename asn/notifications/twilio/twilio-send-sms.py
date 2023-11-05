from twilio.rest import Client

account_sid = 'CHANGEME'
auth_token = 'CHANGEME'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='CHANGEME',
  body='CHANGEME',
  to='CHANGEME'
)

print(message.sid)
