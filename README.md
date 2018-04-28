# Admin

A tiny authentication server for MathHub written in Python and Django. 
It is expected to be run only inside a MathHub Docker Setup, to be composed with the other components. 
It expects to be run together with an NGINX as auth_server url. 

It consists of only three routes:
* `/admin/` -- a django admin instance to get free and cheap user management
* `/admin/nginx/check` -- an auth_backend for nginx that return `HTTP 200` if a user is authorized and `HTTP 401` if not. 
* `/admin/nginx/login` -- a route that redirects the user to a login page based on the `X-Original-URI` header. 

## Dockerfile

This repository contains a [Dockerfile](Dockerfile) which is designed to run the backend. 
By default, it listens on port 8000 for wsgi connections and uses an sqlite database stored in a volume mounted at `/data/`. 
An automated build is available under [mathhub/admin](https://hub.docker.com/r/mathhub/admin) and can be run with a command like the following:

```
   docker run -e DJANGO_SECRET_KEY=totally_secret_key_here -p 8000:8000 -v data:/data/ mathhub/admin
```