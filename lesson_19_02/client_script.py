import requests

def upload_get_delete_image(image_path):
    filename = image_path.split('/')[-1]
    url = 'http://127.0.0.1:8080'


    with open(image_path, 'rb') as img:
        response = requests.post(f"{url}/upload", files=({'image': img}))
        print("UPLOAD", response.status_code, response.json())

    res = requests.get(f'{url}/image/{filename}', headers={'Content-Type': 'text'})
    print("GET:", res.status_code, res.json())

    res = requests.delete(f'{url}/delete/{filename}')
    print("DELETE:", res.status_code, res.json())

upload_get_delete_image('nature.jpg')