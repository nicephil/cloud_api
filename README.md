### run gunicorn as http
```shell
# run this cmd at top of git clone directory
gunicorn --reload --bind 0.0.0.0:2018 src.server:api
```

### API usage
[administrator `get API` how-to](doc/api-howto.md)