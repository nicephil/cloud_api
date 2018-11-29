### run gunicorn as http/https
see gunicorn how-to: [logging](http://docs.gunicorn.org/en/latest/settings.html#logging)
```shell
# run at top of git directory, as user 'oakridge'

# develop run 
gunicorn --reload --bind 0.0.0.0:2018 src.server:api

# production check cfg
gunicorn --check-config -c production.cfg.py src.server:api

# production deploy
gunicorn -c production.cfg.py src.server:api
```

### API usage
[administrator `get API` how-to](doc/api-howto.md)

### To-Dos
[Run unicorn in production mode](http://docs.gunicorn.org/en/stable/deploy.html)
