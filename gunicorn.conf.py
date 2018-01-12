bind = "127.0.0.1:8000"                   # Don't use port 80 becaue nginx occupied it already. 
errorlog = '/Users/justin/logs/gunicorn-projectstatusdashboard-error.log'  
accesslog = '/Users/justin/logs/gunicorn-projectstatusdashboard-access.log'
loglevel = 'debug'
workers = 1     # the number of recommended workers is '2 * number of CPUs + 1' 
