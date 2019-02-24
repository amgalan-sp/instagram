import requests
import os
from instabot import Bot
from dotenv import load_dotenv
from fetch_spacex import fetch_spacex
from fetch_hubble import get_collection


def ensure_dir(foldername):
    filepath = "{}/{}/".format(os.getcwd(), foldername)
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(filepath)


def upload_photos(extension='jpeg'):
    username = os.getenv('username')
    password = os.getenv('password')
    bot = Bot()
    bot.login(username=username, password=password)
    files = os.listdir()
    picture_list = list(filter(lambda pics: pics.endswith('.{}'.format(extension)), files))
    for pic in picture_list:
        bot.upload_photo(pic, caption='Nice Pic')


if __name__ == "__main__":
    load_dotenv()
    ensure_dir('image')
    fetch_spacex()
    extension = str(input("введите расширение файлов для скачивания и загрузки ", ))
    get_collection('stsci_gallery', extension)
    upload_photos(extension='jpeg')