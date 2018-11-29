### run gunicorn as http
```shell
# run this cmd at top of git clone directory
gunicorn --reload --bind 0.0.0.0:2018 src.server:api
```

### API usage
[administrator `get API` how-to](doc/api-howto.md)

### To-Dos
[Run unicorn beind proxy server](http://docs.gunicorn.org/en/stable/deploy.html)
