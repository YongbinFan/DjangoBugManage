from twilio.rest import Client
from django.conf import settings

# https://console.twilio.com/us1/develop/sms/try-it-out/send-an-sms
# https://www.twilio.com/docs/messaging/tutorials/how-to-send-sms-messages/python

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


# message = client.messages.create(
#     from_='+12296196599',
#     body='hello word',
#     to='+61434402728'
# )


def send_single_sms(content, phone_no='+61434402728'):
    message = client.messages.create(
        from_='+12296196599',
        body=content,
        to=phone_no
    )

    return message

# send_single_sms("Love you")


# print(message.sid)
