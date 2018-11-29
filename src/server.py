import sys
import falcon
import admin


# GET  /user          batch get for table list
# GET  /user/{id}     get one admin detail


many_admin = admin.Admins ()
one_admin = admin.OneAdmin()
api = falcon.API()
api.add_route ('/user',many_admin)
api.add_route ('/user/{uid}',one_admin)
