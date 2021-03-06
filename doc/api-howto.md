### Batch get administrators from DB **user_info** table
API:
```shell
$ http GET 'https://cloud.oakridge.vip:2018/user?org_id=14&page=0&page_size=2&sort_key=email&order=desc&key=Oakridge'
```
Parameters:
```shell
    org_id=<site_id>
    page=<int>                                      # start point
    page_size=<int>                                 # query size
    sort_key=[any field in 'user_info' table]       # default 'id'
    order=[asc | desc]                              # default 'asc'
    key=<tmp hardcode as 'Oakridge'>
```
Output:
```http
HTTP/1.1 200 OK
Connection: close
Date: Thu, 29 Nov 2018 19:56:40 GMT
Server: gunicorn/19.9.0
content-length: 600
content-type: application/json; charset=UTF-8
```
```json
{
    "data": [
        {
            "active": 1,
            "country": null,
            "create_at": null,
            "email": "bbb@oakridge.io",
            "expire_at": null,
            "first_login": 1,
            "first_name": null,
            "id": 10,
            "inviter": null,
            "last_name": null,
            "phone": null,
            "role_type": 3,
            "state": 1,
            "type": 1,
            "username": null,
            "version": 1532540761.0
        },
        {
            "active": 1,
            "country": null,
            "create_at": null,
            "email": "aaa@oakridge.io",
            "expire_at": null,
            "first_login": 1,
            "first_name": null,
            "id": 2,
            "inviter": null,
            "last_name": null,
            "phone": null,
            "role_type": 3,
            "state": 1,
            "type": 1,
            "username": null,
            "version": 1541061505.0
        }
    ],
    "error": [
        0,
        ""
    ]
}
```
### Get 1 entry from DB **user_info** table  
API:
```shell
$ http GET 'https://cloud.oakridge.vip:2018/user/123?key=Oakridge'
```
Parameters:
```shell
    /user/{id}                                      # must have valid user id
    key=<Oakridge>                                  # tempoary hardcoded
```
Output:
```http
HTTP/1.1 200 OK
Connection: close
Date: Thu, 29 Nov 2018 19:38:08 GMT
Server: gunicorn/19.9.0
content-length: 344
content-type: application/json; charset=UTF-8
```
```json
{
    "data": [
        {
            "active": 0,
            "country": null,
            "create_at": null,
            "email": "aaa@xyz.com",
            "expire_at": null,
            "first_login": 1,
            "first_name": null,
            "id": 123,
            "inviter": "280d3eba8553433ba1c520717d0cbe7b",
            "last_name": null,
            "phone": null,
            "role_type": 0,
            "state": 1,
            "type": 301,
            "username": null,
            "version": 1539275772.0
        }
    ],
    "error": [
        0,
        ""
    ]
}
```
- Note:  
    - Sensitive field (**password**, **wechat_openid**, **user_label**) in **user_info** table are hided  
    - Try to play with parameter to see returned error ouput