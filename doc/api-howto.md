- API list

Sample:     http GET 'cloud.oakridge.vip:2018/user?org_id=14&page=0&page_size=10&sort_key=email&order=desc&key=Oakridge'
Function:   batch get administrators from DB 'user_info' table
Parameters:
            org_id=<site_id>
            page=<int>                                      # start point
            page_size=<int>                                 # query size
            sort_key=[any field of DB 'user_info' table]    # default 'id'
            order=[asc | desc]                              #default 'asc'
            key=<tmp hardcode as 'Oakridge'>
            
Sample:     http GET 'cloud.oakridge.vip:2018/user/123?key=Oakridge'
Function:   get 1 entry from DB 'user_info'
Parameters:
            /user/{id}  ...  'id' is the target user <id>
            key=<tmp hardcode as 'Oakridge'>


- Note:
some sensitive field of from 'user_info' table is hided: ('password', 'wechat_openid', 'user_label')
