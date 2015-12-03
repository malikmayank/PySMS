from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "enter your twilio account id"
auth_token  = "enter your auth token here"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello Jiggy",
    to="+19999999999",    # Replace with your phone number
    from_="+19999999999") # Replace with your Twilio number
print message.sid
