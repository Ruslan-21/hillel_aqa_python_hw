import json
from os import write

import requests

response = requests.get(url='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos',
                   params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'})


data = response.json()
print(json.dumps(data, indent=4))

img_url_1 = data['photos'][0]['img_src']
img_url_2 = data['photos'][1]['img_src']

img_response_1 = requests.get(img_url_1)
img_response_2 = requests.get(img_url_2)

with open('mars_photo1.jpg', 'wb') as f1:
    f1.write(img_response_1.content)

with open('mars_photo2.jpg', 'wb') as f2:
    f2.write(img_response_2.content)


