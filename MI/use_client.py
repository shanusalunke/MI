import os, time, smtplib, subprocess
from mock import patch
from pickle import dumps
from sys import path

def t():
	from mailmanclient import Client
	#client = Client('http:127.0.0.1:8001/3.0','restadmin','restpass')
	#var = dumps(client)
	#var = var+ "Currently available lists:\n" , client.lists
	#return var
	return path


MM_PATH = '/root/mailman.client/src/'
if not MM_PATH in path:
    path.append(MM_PATH)
