from send_Covid import *
from send_Quote import *
from send_Meme import *
from send_Fact import *
from send_Weather import *
from twilio.rest import Client
import datetime

###### dotenv variables ########
from dotenv import load_dotenv
import os
load_dotenv()

from_whatsapp_number = os.getenv("from_whatsapp_number")
to_whatsapp_number = os.getenv("to_whatsapp_number")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


def send_through_twilio_image(message_body, message_url):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body=message_body,
        media_url=message_url,
        from_=from_whatsapp_number,
        to=to_whatsapp_number)

    print(message.sid)


def send_through_twilio(message_body):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body=message_body,
        from_=from_whatsapp_number,
        to=to_whatsapp_number)

    print(message.sid)


if __name__ == '__main__':

    # time
    dt = datetime.datetime.now()

    #### COVID ####
    sc = sendCovid()
    messageCovid = sc.get_hk_stats()

    #### QUOTE ####
    sq = sendQuote()
    messageQuote = sq.get_quote()

    sw = sendWeather()
    messageWeather = sw.get_weather()

    sf = sendFact()
    messageFact = sf.get_fact()

    print(dt.hour)
    if dt.hour < 12:
        greeting = "Good Morning"
    else:
        greeting = "Sweet Dreams"

    main_message = '''

*{}, _ser Peter!_*

*Current Weather Description:*
{}

*COVID 19 Updates:*
{}

*An Inspirational quote:*
{}

*A Random Fun Fact:*
{}

    '''.format(greeting, messageWeather, messageCovid, messageQuote, messageFact)

    send_through_twilio(main_message)

    #### MEME ####
    sm = sendMeme()
    messageMeme = sm.get_random_meme()
    send_through_twilio_image(
        "Here is a random cat picture ser Peter of House Chow!", messageMeme)
