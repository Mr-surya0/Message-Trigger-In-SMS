from twilio.rest import Client

twilio_sid = ''
twilio_auth_token = ''
twilio_phone_number = ''
phone = 'your_number_with_countrycode'
booking_number = '3456'

client = Client(twilio_sid, twilio_auth_token)
message = client.messages.create(
    body=f"Your OT booking (number: {booking_number}) was successful!",
    from_=twilio_phone_number,
    to=phone
)
print(message.sid)
