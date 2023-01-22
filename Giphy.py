import json
import urllib.request as url

userInput = input("Enter query : ")
finalInput = userInput.replace(" ", "+")

data = json.load(url.urlopen(f'http://api.giphy.com/v1/gifs/search?q={finalInput}&api_key=bc56161131654faeb550630b83e0c977&limit=10'))

data = data['data']
for i in range(len(data)):
    images = data[i]['images']
    url_2 = images['downsized_large']['url']
    url.urlretrieve(url_2, 'images/gif_{}.gif'.format(i))
