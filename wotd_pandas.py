
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
import pandas as pd
from twilio.rest import Client
load_dotenv(find_dotenv())
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
    ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
    PH_SEND = os.environ.get('PH_SEND')
    PH_RECEIVE = os.environ.get('PH_RECEIVE')
    selection = random.choice(word_list)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(to=PH_RECEIVE, from_=PH_SEND, body=selection)

"""Sends the selection to the phone number indicated"""
pick_word()