# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero

class Position(linkero.Resource):
    def get(self, username):
        return 1

##
## Actually setup the Api resource routing here
##
def load_ghrankingsAPI():
    linkero.api.add_resource(Position, '/position/<username>')
