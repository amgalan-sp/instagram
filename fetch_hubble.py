import requests


def fetch_hubble(id, ext):
    status_ready = None
    response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(id))
    data = response.json()['image_files']
    url = 'file_url'
    image_name = "Hubble-{}.{}".format(id, ext)
    get_load = [download(image['file_url'], image_name) for image in data if image['file_url'].split('.')[-1] == ext]


def get_collection(collection_name, ext):
    response = requests.get('http://hubblesite.org/api/v3/images/{}'.format(collection_name))
    for image_id in response.json():
        fetch_hubble(image_id['id'], ext)


def download(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
