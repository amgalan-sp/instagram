import requests
import os

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def fetch_spacex_last_launch(url):
    os.chdir(filepath)
    response = requests.get(url)
    for id, images_link in enumerate(response.json()['links']['flickr_images'], 1):
        url = images_link
        filename = "Space-{}.jpeg".format(id)
        response = requests.get(url)
        with open (filename, 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    filepath = "{}/images/".format(os.getcwd())
    ensure_dir(filepath)
    url_latest_launch = 'https://api.spacexdata.com/v3/launches/latest'
    fetch_spacex_last_launch(url_latest_launch)
