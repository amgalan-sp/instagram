import requests
import os
from instabot import Bot


def ensure_dir(foldername):
    filepath = "{}/{}/".format(os.getcwd(), foldername)
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(filepath)

def download(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    for id, images_link in enumerate(response.json()['links']['flickr_images'], 1):
        download(images_link, "Space-{}.jpeg".format(id))


def fetch_hubble_images(id, extension):
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

def get_collection(collection, extension):
    response = requests.get('http://hubblesite.org/api/v3/images/{}'.format(collection))
    for image_id in response.json():
        fetch_hubble_images(image_id['id'], extension)
        print(image_id['id'])


def upload_photos():
    bot = Bot()
    bot.login(username='', password='')
    bot.upload_photo('111.jpg', caption='Nice Pic')



if __name__ == "__main__":
    ensure_dir('image')
 #   fetch_spacex_last_launch()
  #  fetch_hubble_images(1, 'jpg')
   # get_collection('printshop', 'jpg')
    upload_photos()