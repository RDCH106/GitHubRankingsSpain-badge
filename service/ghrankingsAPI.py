# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero
import sys
import traceback
if sys.version_info > (3, 0):           # Python 3 compatibility
    import urllib.request as urllib
else:                                   # Python 2 compatibility
    import urllib
import json

base_url = "https://raw.githubusercontent.com/iblancasa/ghrankings/master/"

class Ranking:
    def __init__(self):
        self.ranking_list = []

    def add_ranking(self, ranking):
        self.ranking_list.append(ranking)

def load_ranking():
    try:
        response = urllib.urlopen(base_url + 'euskadi/euskadi.json')
        data = json.loads(response.read().decode())
        print(data)
    except:
        traceback.print_exc()
        raise

class Position(linkero.Resource):
    def get(self, username):
        return 1

##
## Actually setup the Api resource routing here
##
def load_ghrankingsAPI():
    load_ranking()
    linkero.api.add_resource(Position, '/position/<username>')
