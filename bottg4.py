def get_updates_json(request):
	params = {'timeout': 100, 'offset': None}
	response = requests.get(requests + 'get_updates', data=params)
	return response.json()