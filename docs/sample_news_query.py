#!/usr/bin/env python
from requests import Session
from pprint import pprint

s = Session()

url = ('http://newsapi.org/v2/everything?'
              'q=Revolut&'
              'pageSize=1&'
              'sortBy=popularity&'
              'apiKey=0bfe1b2ef7f74675bf699f7f17a03459')

response = s.get(url)

pprint(response.json())
