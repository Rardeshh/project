def get_chat_id(update):
	chat_id = update['message']['chat']['id']
	return chat_id

def send_mess(chat,text):
	params = {'chat_id': chat, 'text': text}
	response = requests.post(url + 'sendMessage', data=params)
	return response

chat_id = get_chat_id(last_update(get_updates_json(url)))
send_mess(chat_id, 'Your message goes here')	
