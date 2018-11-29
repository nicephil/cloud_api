Oakridge Cloud RESTful API

# how to
- run gunicorn as http
```shell
# run this cmd at top of git clone directory
gunicorn --reload --bind 0.0.0.0:2018 src.server:api
```