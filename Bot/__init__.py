import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID',28837889 )) #API ID
API_HASH = environ.get('API_HASH', '9d5e9c5b8abcf8b7b930abd259de254e') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '6655774727:AAGsUPOSWeVnpzwd4ME7rvBs5dNAMNViur0') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://Hackx:Hackx@hackx.6flteju.mongodb.net/?retryWrites=true&w=majority&appName=Hackx') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', '1910728581')) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', '-1002106866999'))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', '-1002007169772' ))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', '-1001732273753')) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
