import requests

URLS = [
	  'https://commondreams.org',
    'https://adbusters.org',
]

for url in URLS:
    response = requests.get(url)
    filename = url.replace('https://', '') + '.html'
    with open(filename, 'w') as f:
        f.write(response.text)
    print('Wrote file to ' + filename)