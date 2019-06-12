import urllib.request
from urllib.parse import quote
from json import loads

def getDefinition(word):
	app_id = 'your app id'
	app_key = 'your app key'
	option = 'entries'
	language_code = 'es'
	word_encoded = quote(word)
	url = f'https://od-api.oxforddictionaries.com/api/v2/{option}/{language_code}/{word_encoded}'
	req = urllib.request.Request(url)
	req.add_header('app_id', app_id)
	req.add_header('app_key', app_key)
	try:
		res = urllib.request.urlopen(req)
	except Exception:
		raise ValueError('No se encontraron resultados')
	data = loads(res.read())
	return data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]