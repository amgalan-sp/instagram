import requests
import os
import json


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_content(url, filepath, id):
    os.chdir(filepath)
    filename = "Space-{}.jpeg".format(id)
    response = requests.get(url)
    with open (filename, 'wb') as file:
        file.write(response.content)

def get_latest_launch_images(url):
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    folder_name = "images"
    filepath = "{}/{}/".format(os.getcwd(),folder_name)
    ensure_dir(filepath)
    url_shattle = 'https://api.spacexdata.com/v3/launches/latest'
    for id, images_url in enumerate(get_latest_launch_images(url_shattle)['links']['flickr_images'], 1):
        url = images_url
        get_content(url, filepath, id)