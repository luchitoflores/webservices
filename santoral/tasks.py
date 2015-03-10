__author__ = 'LFL'

from celery import Celery
app = Celery('tasks', broker='amqp://',backend='amqp')
from urllib2 import urlopen
from urllib import urlencode
import urllib2
import json
from time import sleep
from django.conf import settings
