Learn gunicorn how-to:
[logging](http://docs.gunicorn.org/en/latest/settings.html#logging),
[cfg](http://docs.gunicorn.org/en/stable/configure.html),
[signal](http://docs.gunicorn.org/en/stable/signals.html)

### run/stop gunicorn
```shell
# run cmd at top of git directory, as user 'oakridge'

# see if gunicorn is running
ps -ef | grep gunicorn

# develop run 
gunicorn --reload --bind 0.0.0.0:2018 src.server:api
gunicorn -c dev.cfg.py src.server:api

# production check cfg
gunicorn --check-config -c production.cfg.py src.server:api

# production deploy
gunicorn -c production.cfg.py src.server:api

# stop gunicorn
kill -SIGTERM $(cat /tmp/cloud_api.pid)
```

### API usage
[administrator `get API` how-to](doc/api-howto.md)

### To-Dos
[Run unicorn in production mode](http://docs.gunicorn.org/en/stable/deploy.html)
