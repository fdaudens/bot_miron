#!/usr/bin/python
# -*- coding: utf-8 -*-

# Inspiré d'un tutoriel de @robincamille http://emerging.commons.gc.cuny.edu/2013/10/making-twitter-bot-python-tutorial/

import tweepy, time

CONSUMER_KEY = '' # Créer une nouvelle application à dev.twitter.com 
CONSUMER_SECRET = '' # Niveau d'accès requis : read and write 
ACCESS_KEY = '' # Créer un "access token"
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('chemin_du_fichier.txt','r') #insérer chemin ici
f=filename.readlines()
filename.close()

for line in f: 
    api.update_status(status=line)
    print line
    time.sleep(3600) # intervalles de veille d'une heure (3600 secondes)
