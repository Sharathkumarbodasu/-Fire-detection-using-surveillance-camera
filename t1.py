from twilio.rest import Client
account_sid = 'AC610470b7d696642dc8550d849dd0d2e4'
auth_token = 'e40f6eaa5ec85e916057ef3e69207a5c'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+17622429694',
  body='Alert A fire Accident detected in your room 1',
  to='+918328503106'
)

print(message.sid)