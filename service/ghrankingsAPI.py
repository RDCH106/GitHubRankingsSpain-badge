# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero
import sys
import traceback
if sys.version_info > (3, 0):           # Python 3 compatibility
    import urllib.request as urllib
else:                                   # Python 2 compatibility
    import urllib
import json

ranking = None


class Ranking:
    def __init__(self):
        self.__config = self.__load_config()
        self.ranking_list = self.__load_ranking()

    def add_ranking(self, ranking):
        self.ranking_list.append(ranking)

    def __load_config(self):
        try:
            with open('config/api_config.json') as config_file:
                config = json.load(config_file)
                return config
        except:
            traceback.print_exc()
            raise

    def __load_ranking(self):
        try:
            ranking_list = []
            for ranking in self.__config["json_list"]:
                response = urllib.urlopen(self.__config["base_url"] + ranking["path"])
                data = json.loads(response.read().decode())
                #print(data)
                ranking_list.append({"name": ranking["name"], "ranking": data})
            print(ranking_list)
            return ranking_list
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
