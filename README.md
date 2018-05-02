# Admin

A small authentication server for MathHub written in Python and Django. 

It is expected to be run only inside a [MathHub Compositor Setup](https://github.com/MathHubInfo/Compositor), to be composed with the other components. 
It expects to be run together with an NGINX as `auth_server` url. 

It contains the following routes:
- `/admin/` - An Admin overview page
- `/admin/login`, `/admin/login_staff` - Login pages for users and staff
- `/admin/django/` - A Django Admin page for cheap user management
- `/admin/nginx/` - An authentication backed used by nginx

Administration is split into two authentication level:
- Users, who can access the MMT Backend(s) in an unrestricted fashion
- Staff, who can manage users, and update components on a docker level. 
These users are created via Django Admin. 


## Dockerfile

This repository contains a [Dockerfile](Dockerfile) which is designed to run the backend. 
By default, it listens on port 80 and uses an sqlite database stored in a volume mounted at `/data/`. 
An automated build is available under [mathhub/admin](https://hub.docker.com/r/mathhub/admin) and can be run with a command like the following:

```
   docker run -e DJANGO_SECRET_KEY=totally_secret_key_here -p 8000:8000 -v data:/data/ mathhub/admin
```

## License

Licensed under AGPL 3.0