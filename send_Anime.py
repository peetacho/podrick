import requests
import random
# from twilio.rest import Client


class sendAnime():
    def __init__(self):
        # self.all_anime_info = {}
        # Here we define our query as a multi-line string
        self.query = '''
        query ($id: Int) {
        Media (id: $id,type: ANIME, isAdult:false) {
            id
            coverImage {
                extraLarge
            }
            source
            title {
                romaji
                english
                native
            }
        }
        }
        '''
        self.anilist_url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    def get_random_anime(self):

        variables = {'id': random.randint(1, 3200)}
        response = requests.post(
            self.anilist_url, json={'query': self.query, 'variables': variables})

        print("got response!")
        try:
            response_json = response.json()
            # print("successful!")
        except:
            variables = {'id': random.randint(1, 3200)}
            response = requests.post(
                self.anilist_url, json={'query': self.query, 'variables': variables})
            response_json = response.json()
            # print("error!")

        response_json_media = response_json['data']['Media']

        title = response_json_media["title"]["native"] if None else response_json_media["title"]["romaji"]
        message_body = "Check out {}!".format(title)
        message_url = response_json_media["coverImage"]["extraLarge"]

        message_components = [message_body, message_url]

        return message_components
