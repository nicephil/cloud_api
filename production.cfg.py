import multiprocessing

bind = "0.0.0.0:2018"
workers = multiprocessing.cpu_count() * 2 + 1
daemon = True
pidfile = '/tmp/cloud_api.pid'
accesslog = '/tmp/cloud_api.log'
errorlog = '/tmp/cloud_api.err'
