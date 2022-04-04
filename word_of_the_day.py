"""In the end, this will import a list from Excel, make a random selection, and then send that to my phone."""
import random
import os
from twilio.rest import Client
import simplejson as json
word_dict = {}

def load_dict():
    global word_dict
    with open('wotd_reference.txt', 'r') as file:
        word_dict = json.load(file)
        return word_dict

def save_dict():
    global word_dict
    with open('wotd_reference.txt', 'w') as file:
        word_dict = json.dump(word_dict, file)

def add_word():
    global word_dict
    load_dict()
    key = input('Enter the word you wish to add: ')
    value = input('Enter the definition: ')
    print(key + ': ' + value)
    confirm = input('Is this correct? Y/N: ')
    if confirm == 'Y':
        word_dict[key] = value
        save_dict()
    else:
        add_word()


def pick_word():
    """Selects the key/value pair for a word, converts to list, and then returns in a clean format."""
    ACCOUNT_SID = os.getenv('ACCOUNT_SID')
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')
    PH_SEND = os.getenv('ph_send')
    PH_RECEIVE = os.getenv('ph_receive')
    word_dict = load_dict()
    selection = random.choice(list(word_dict.items()))
    word_today = ': '.join(selection)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(to=PH_RECEIVE, from_=PH_SEND, body=word_today)

"""Sends the selection to the phone number indicated"""

pick_word()
