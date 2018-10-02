# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero
from flask import redirect, abort
import sys
import traceback
if sys.version_info > (3, 0):           # Python 3 compatibility
    import urllib.request as urllib
else:                                   # Python 2 compatibility
    import urllib
    import codecs
import json

ranking = None


class Ranking:
    def __init__(self):
        self.__config = self.__load_config()
        self.ranking_list = self.__load_ranking()

    def add_ranking(self, ranking):
        self.ranking_list.append(ranking)

    @staticmethod
    def __load_config():
        try:
            if sys.version_info > (3, 0):  # Python 3 compatibility
                with open(file='config/api_config.json', encoding="utf-8") as config_file:
                    config = json.load(config_file)
                    return config
            else:  # Python 2 compatibility
                with codecs.open(filename='config/api_config.json', encoding="utf-8") as config_file:
                    config = json.load(config_file)
                    return config
        except:
            traceback.print_exc()
            raise

    def __load_ranking(self):
        try:
            ranking_list = {}
            for ranking in self.__config["json_list"]:
                print("Loading... " + self.__config["base_url"] + ranking["path"])
                response = urllib.urlopen(self.__config["base_url"] + ranking["path"])
                data = json.loads(response.read().decode())
                ranking_list[ranking["name"]] = {"good_name": ranking["good_name"], "ranking": data}
            #print(ranking_list)
            return ranking_list
        except:
            traceback.print_exc()
            raise

    def get_user_position(self, region, username):
        try:
            for pos in ranking.ranking_list[region]["ranking"]["users"]:
                if pos["name"] == username:
                    return pos["position"]
        except KeyError:
            pass


class Position(linkero.Resource):
    def get(self, username):
        return 1


class Badge(linkero.Resource):
    def get(self, region, username):
        try:
            return redirect("https://img.shields.io/badge/Ranking " +
                            ranking.ranking_list[region]["good_name"] + "-" +
                            str(ranking.get_user_position(region, username)) +
                            "-blue.svg?maxAge=3600&logo=github")
        except KeyError:
            return abort(400)   # Bad Request

##
## Actually setup the Api resource routing here
##
def load_ghrankingsAPI():
    global ranking
    ranking = Ranking()
    linkero.api.add_resource(Badge, '/badge/<region>/<username>')
    linkero.api.add_resource(Position, '/position/<username>')
