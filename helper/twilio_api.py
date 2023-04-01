import os

from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')
client = Client(account_sid, auth_token)


def send_message(to: str, message: str, image_url: str = None) -> None:
    '''
    Send message to Whatsapp user.
    Parameters:
        - to(str): sender WhatsApp number in this format: whatsapp:+919558515995
        - message(str): text message to send
        - image_url(str): Optional URL of the image to send
    Returns:
        - None
    '''

    if image_url is not None:
        _ = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message,
            media_url=[image_url],
            to=to
        )
    else:
        _ = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message,
            to=to
        )
