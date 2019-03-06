import requests


def fetch_hubble(id, extension):
    status_ready = None
    response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(id))
    for image_url in response.json()['image_files']:
        if image_url['file_url'].split('.')[-1] == extension:
            status_ready = True
        else:
            pass
    if status_ready:
        download(image_url['file_url'], "Hubble-{}.{}".format(id, extension))
    else:
        pass


def get_collection(collection_name, extension):
    response = requests.get('http://hubblesite.org/api/v3/images/{}'.format(collection_name))
    for image_id in response.json():
        fetch_hubble(image_id['id'], extension)


def download(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
