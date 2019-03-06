import os
from instabot import Bot
from dotenv import load_dotenv
from fetch_spacex import fetch_spacex
from fetch_hubble import get_collection
import argparse

def make_dir():
    foldername = 'images'
    os.makedirs(foldername)
    filepath = "{}/{}/".format(os.getcwd(), foldername)
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
    make_dir()
    parser = argparse.ArgumentParser(description='This is a description')
    parser.add_argument('-e','--extension', type=str, help='you can give extension(format) of a photo like jpeg, png, jpg, tiff' )
    parser.add_argument('definite', help='you have 2 defs: spacex or hubble')
    parser.add_argument('-c', '--collection', help='if you use hubble, yo need to input name of collection')
    args = parser.parse_args()
    collection_name = args.collection
    extension = args.extension
    definition = args.definite
    if definition == 'spacex':
        fetch_spacex()
    elif definition == 'hubble':
        get_collection(collection_name, extension)
    else:
        print('choose a definition: download spacex or huuble shoots')
    upload_photos()
