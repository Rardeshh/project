import requests

url = "https://api.telegram.org/bot1341481078:AAHvCgVLeEnhlsXN7Y3kD9vSt8ydX3ZeUwM/"


def get_updates_json(request):
	response = requests.get(request + 'getUpdates')
	return response.json()


def last_update(data):
	results = data['result']
	total_updates = len(results) - 1
	return results[total_updates]
