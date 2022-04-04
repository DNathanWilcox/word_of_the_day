
import random
import os
import pandas as pd
from twilio.rest import Client
word_list = []
count = 0

def load_dictionary():
    separator = ': '
    with open ('wotd_pandas_reference.csv', 'r') as file:
        for i in file:
            i = i.strip('\n')
            i = i.split(',')
            word_and_def = separator.join(i)
            word_list.append(word_and_def)

def pick_word():
    """pulls words from the csv file, picks one, and sends it"""
    load_dictionary()
    ACCOUNT_SID = os.getenv('ACCOUNT_SID')
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')
    PH_SEND = os.getenv('ph_send')
    PH_RECEIVE = os.getenv('ph_receive')
    selection = random.choice(word_list)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(to=PH_RECEIVE, from_=PH_SEND, body=selection)

"""Sends the selection to the phone number indicated"""
pick_word()