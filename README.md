# Admin

A tiny authentication server for MathHub written in Python and Django. 
It expects to be run together with an NGINX as auth_server url. 

It consists of only three routes:
* `/admin/` -- a django admin instance to get free and cheap user management
* `/admin/nginx/check` -- an auth_backend for nginx that return `HTTP 200` if a user is authorized and `HTTP 401` if not. 
* `/admin/nginx/login` -- a route that redirects the user to a login page based on the `X-Original-URI` header. 