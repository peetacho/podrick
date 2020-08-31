import requests
import json


class sendMeme():
    def __init__(self):
        pass

        # Make the HTTP Api request
    def get_random_meme(self):

        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url)
        response_json = response.json()

        message_url = response_json[0]["url"]

        return message_url
