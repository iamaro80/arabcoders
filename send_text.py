from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC2651f07719626a680134b890b563cef4"
# Your Auth Token from twilio.com/console
auth_token  = "ab05a1d1c9074abe0047bcea0c719381"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+962780039327",
    from_="+12602388269",
    body="Hello from Python!")

print(message.sid)
