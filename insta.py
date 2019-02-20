import requests
import os

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    for id, images_link in enumerate(response.json()['links']['flickr_images'], 1):
        url = images_link
        filename = "Space-{}.jpeg".format(id)
        response = requests.get(url)
        with open (filename, 'wb') as file:
            file.write(response.content)


def get_links(url):
    response = requests.get(url)
    for id, image_links in enumerate(response.json()['image_files'], 1):
        url = image_links['file_url']
        return url

def get_link(url, payload):
    response = requests.get(url, params=payload)
    return response.json()

def get_expansion(url):
    return url.split('.')[-1]

def get_download(url, expansion, id):
    if get_expansion(url) == expansion:
        filename = "Hubble-{}.{}".format(id, expansion)
        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        pass


def get_linked(url):
    response = requests.get(url)
    print(response.json()['image_files'])


if __name__ == "__main__":
    filepath = "{}/images/".format(os.getcwd())
    ensure_dir(filepath)
    os.chdir(filepath)
    url_latest_launch = 'https://api.spacexdata.com/v3/launches/latest'
    url_hubble = 'http://hubblesite.org/api/v3/images/'
    url_hubble2 = 'http://hubblesite.org/api/v3/image/{}'
#   fetch_spacex_last_launch(url_hubble)

    for id, images in enumerate(get_link(url_hubble, {'image_id': 1}), 1):
        get_download(get_links(url_hubble2.format(images['id'])), 'tiff', id)