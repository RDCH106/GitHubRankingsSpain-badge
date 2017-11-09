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
ranking = None

class Ranking:
    def __init__(self):
        self.__config = self.load_config()
        self.ranking_list = []


    def add_ranking(self, ranking):
        self.ranking_list.append(ranking)

    def load_config(self):
        try:
            with open('config/api_config.json') as config_file:
                config = json.load(config_file)
        except:
            traceback.print_exc()
            raise

    def load_ranking(self):
        try:
            response = urllib.urlopen(self.__config["base_url"] + 'euskadi/euskadi.json')
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
    #load_ranking()
    global ranking
    ranking = Ranking()
    linkero.api.add_resource(Position, '/position/<username>')
