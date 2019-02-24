import requests


def fetch_hubble(id, extension):
    ready_image = None
    response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(id))
    for final_images in response.json()['image_files']:
        if final_images['file_url'].split('.')[-1] == extension:
            ready_image = True
        else:
            pass
    if ready_image:
        download(final_images['file_url'], "Hubble-{}.{}".format(id, extension))
    else:
        print('No images with {} extension, or with {} id, please try with another one'.format(extension, id))
        pass


def get_collection(collection_name, extension):
    response = requests.get('http://hubblesite.org/api/v3/images/{}'.format(collection_name))
    for image_id in response.json():
        fetch_hubble(image_id['id'], extension)
        print('successful loading ', image_id['id'])


def download(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
