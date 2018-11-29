import falcon
import requests
import json
import pickle
from dbwrapper import DB
import util

def validate_batch_get_params (req, resp, resource, params):
    for i in ('org_id','page','page_size'):
        if i not in req.params:
            raise falcon.HTTPBadRequest('Bad request', 'Missing param <%s>' % i)
    for i in ('page','page_size'):
        if not util.is_positive_int (req.params[i]):
            raise falcon.HTTPBadRequest('Bad request', '<%s> must be positive int' % i)
    if int(req.params['page_size']) > 1024:
        raise falcon.HTTPBadRequest('Bad request', 'page_size %s too big(max 200)' % req.params['page_size'])
    if 'sort_key' not in req.params:
        req.params['sort_key'] = 'id'   #default sort by id
    if 'order' not in req.params:
        req.params['order'] = 'ASC'   #default sort by id

def validate_api_key (req, resp, resource, params):
    if 'key' not in req.params or req.params['key'] != 'Oakridge' :
        raise falcon.HTTPBadRequest('Bad request', 'Authentication fail')


# handle batch admin ops
@falcon.before (validate_api_key)
class Admins (object):
    @falcon.before (validate_batch_get_params)
    def on_get (self, req, resp):
        try:
            with DB('127.0.0.1','root','oakridge','authc') as db:
                # recursively find all user_id given a site's org_id
                # https://stackoverflow.com/questions/20215744/how-to-create-a-mysql-hierarchical-recursive-query
                sql = """
                        SELECT * FROM user_info WHERE id in (
                            SELECT user_id FROM user_organization_permission WHERE org_id in (
                                SELECT id FROM (
                                    SELECT id, parent_id FROM organization_info ORDER BY id DESC) dummy1, (SELECT @cid := %s) dummy2
                                    WHERE find_in_set(id, @cid) and length(@cid := concat(@cid, ',', parent_id)
                                )
                            )
                        ) ORDER BY %s %s LIMIT %s,%s
                      """ % (req.params['org_id'], req.params['sort_key'], req.params['order'], int(req.params['page']) * int(req.params['page_size']), req.params['page_size'])

                dict_array = db.query_and_fetchall_json (sql, exclude_column=('password', 'wechat_openid', 'user_label'))

                if not dict_array:
                    error = (2,'no record found')
                else:
                    error = (0,'')
                result= {
                    'error': error,
                    'data': dict_array 
                }
                resp.status = falcon.HTTP_200
        except Exception as e:
            result= { 'error': (100, str(e)) }
            resp.status = falcon.HTTP_500

        resp.body=json.dumps(result)


# handle ops on one admin
@falcon.before (validate_api_key)
class OneAdmin (object):
    def on_get (self, req, resp, uid):
        try:
            with DB('127.0.0.1','root','oakridge','authc') as db:
                sql = """SELECT * FROM user_info WHERE id = %s""" % uid
                dict_array = db.query_and_fetchall_json(sql, exclude_column=('password', 'wechat_openid', 'user_label'))
                if not dict_array:        
                    error = (2,'no uid %s found' % uid)
                else:
                    error = (0,'')
                result= {
                    'error': error,
                    'data': dict_array 
                }
                resp.status = falcon.HTTP_200
        except Exception as e:
            result= { 'error': (101, str(e)) }
            resp.status = falcon.HTTP_500

        resp.body=json.dumps(result)
