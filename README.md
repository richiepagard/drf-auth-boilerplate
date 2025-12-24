## DRF Auth Boilerplate

A simple Django Rest Framework project with basic JWT authentication setup.


## Features

- Custom user model (username, email, nickname)
- User registration with automatic JWT token generation
- Token endpoints using SimpleJWT
- Clean and minimal project layout


## Stack
- Python
- Django
- Django Rest Framework
- SimpleJWT


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

| Method |          URL             |             Description            |
|--------|--------------------------|------------------------------------|
|  POST  | `api/auth/register/`     | Register new user + get JWT tokens.|
|  POST  | `api/auth/token/`        | Get access and refresh tokens.     |
|  POST  | `api/auth/token/refresh/`| Refresh access token.              |


## Note

This project is just a starting point.
It's not meant for production use out of box.


## License

**MIT**


## TODO
- [x] Setup Django project and structure
- [x] Create custom user model
- [x] Add user registration endpoint
- [x] Generate JWT tokens after successful registration
- [x] Setup SimpleJWT token endpoints
- [x] Add login endpoint using JWT 
- [x] Add user logout and token blacklist
- [ ] Add password reset (via email or OTP)
- [x] Add user profile endpoint
- [ ] Write unit tests for authentication

---

> "I built this to understand DRF + JWT better. Might help others too."
