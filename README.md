## DRF Auth Boilerplate

A simple Django Rest Framework project with basic JWT authentication setup.


## Features

- Custom user model (username, email, nickname)
- User registration with automatic JWT token generation
- Token endpoints using SimpleJWT
- Clean and minimal project layout


## Stack
[![My Skills](https://skillicons.dev/icons?i=py,django&perline=3)](https://skillicons.dev)


## Getting Started
```bash
git clone https://github.com/r-pagard/drf-auth-boilerplate.git
cd drf-auth-boilerplate
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser --username <username> --email <email address>
python3 manage.py runserver
```


## Endpoints

| TITLE                 | METHOD |            URL                    |                            DESCRIPTION                                |
|-----------------------|--------------------------------------------|-----------------------------------------------------------------------|-
| Get JWT Tokens        |  POST  | `api/auth/token/`                 | Get access and refresh tokens.                                        |
| Get Access Token      |  POST  | `api/auth/token/refresh/`         | Refresh access token.                                                 |
| User Register         |  POST  | `api/auth/users/register/`        | Register new user + get JWT tokens.                                   |
| User Login            |  POST  | `api/auth/users/login/`           | Login a new user with getting its **access** and **refresh** tokens.  |
| User Logout           |  POST  | `api/auth/users/logout/`          | Logout user with the provided **refresh** token. Blacklists the token |
| User Profile Retrieve |  GET   | `api/auth/users/<user-pk>/profile`| Retrieves a user profile with no permissions.                         |
| User Profile Update   |  PATCH | `api/auth/users/profile/update/`  | Updating a user profile by its owner (partial update).                |


## Note

This project is just a starting point.
It's not meant for production use out of box.


## License

**MIT**

---

> "I built this to understand DRF + JWT better. Might help others too."
