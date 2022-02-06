import os

from requests import post, auth


class SpotifyAPI:
    def __init__(self):
        client_id = os.environ['SPOTIFY_CLIENT_ID']
        client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
        self.basic_auth = auth.HTTPBasicAuth(client_id, client_secret)
        self.base_url = 'https://accounts.spotify.com/api/'
        self.token = None

        self.get_token()

    def get_token(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {'grant_type': 'client_credentials'}
        response = post(self.base_url + 'token', auth=self.basic_auth, headers=headers, data=body)
        self.token = response.json()['access_token']
