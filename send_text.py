# https://www.twilio.com

from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+*********327",
    from_="+12602388269",
    body="Hello from Python!")

print(message.sid)
