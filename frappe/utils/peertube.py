import time
import requests
import os

url = 'http://peertube.localhost:9000'
# url = 'http://legion.tailaadcc.ts.net:9000/'

def upload_to_peertube(file_content, vid_name):
    api_url = url + '/api/v1'
    api_user = 'root'
    api_pass = 'root@123'
    response = requests.get(api_url + '/oauth-clients/local')
    data = response.json()
    client_id = data['client_id']
    client_secret = data['client_secret']
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'password',
        'response_type': 'code',
        'username': api_user,
        'password': api_pass
    }
    response = requests.post(api_url + '/users/token', data=data)
    data = response.json()
    token_type = data['token_type']
    access_token = data['access_token']

    headers = {
        'Authorization': 'Bearer ' + access_token,
    }
    files = {
        'videofile': (vid_name, file_content, 'video/mp4'),
    }
    data = {
        'channelId': '1',
        'name': vid_name,
        'privacy': '1',

    }
    send_url = url + "/api/v1/videos/upload"
    response = requests.post(send_url, headers=headers, files=files, data=data)
    data = response.json()
    uuid = data['video']['uuid']
    return uuid

# debug delete later
# if __name__ == "__main__":
#     file_path = '/home/raxen/Videos/Weired/Programmers anthem-vcz273os5jf61.mp4'
#     res = upload_to_peertube(file_path, "programmers anthem")
