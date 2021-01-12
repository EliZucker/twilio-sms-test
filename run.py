import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']


def get_user_input():
    recipient = input("Enter the number you would like to text: ")
    message = input("Enter your message: ")
    return recipient, message

def send_message(sender, recipient, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_=sender,
        to=recipient)

if __name__ == "__main__":
    recipient, message = get_user_input()
    send_message(TWILIO_PHONE_NUMBER, recipient, message)


