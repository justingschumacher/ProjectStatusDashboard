bind = "127.0.0.1:8000"                   # Don't use port 80 becaue nginx occupied it already. 
errorlog = '/home/ubuntu/logs/gunicorn-goaldashboard-error.log'
accesslog = '/home/ubuntu/logs/gunicorn-goaldashboard-access.log'
loglevel = 'debug'
workers = 3     # the number of recommended workers is '2 * number of CPUs + 1' 
