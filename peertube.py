from __future__ import print_function
import time
import peertube
from peertube.rest import ApiException
import requests

def upload_to_peertube(file_path, vid_name):

	api_url = 'http://peertube.localhost:9000/api/v1'
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



	configuration = peertube.Configuration(
		host = "http://peertube.localhost:9000/api/v1"
	)

	configuration.access_token = access_token


	# with peertube.ApiClient(configuration) as api_client:
	#     api_instance = peertube.AccountsApi(api_client)
	#     name = "root"
	#     try:
	#         # List video channels of an account
	#         api_response = api_instance.accounts_name_video_channels_get(name)
	#     except ApiException as e:
	#         print("Exception when calling AccountsApi->accounts_name_video_channels_get: %s\n" % e)

	with peertube.ApiClient(configuration) as api_client:
		api_instance = peertube.VideoApi(api_client)
		videofile = file_path
		channel_id = 1
		name = vid_name
		privacy = '1'

		try:
			api_response = api_instance.videos_upload_post(videofile, channel_id, name, privacy=privacy)
			return api_response
		except ApiException as e:
			print("Exception when calling VideoApi->videos_upload_post: %s\n" % e)
			return None

