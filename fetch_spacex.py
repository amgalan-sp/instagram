import requests


def fetch_spacex():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    for id, images_link in enumerate(response.json()['links']['flickr_images'], 1):
        download(images_link, "Space-{}.jpeg".format(id))

def download(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)


