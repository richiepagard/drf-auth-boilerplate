## DRF Auth Boilerplate

A simple Django Rest Framework project with basic JWT authentication setup.


## Features

- Custom user model (username, email, nickname).
- User registration with automatic JWT token generation.
- Token endpoints using SimpleJWT.
- Clean and minimal project layout.
- User authentication endpoints with best-practices.
- Dockerized the project properly.
- Tied to use best-practices.


## Stack
![Stacks](https://go-skill-icons.vercel.app/api/icons?i=python,django,djangorestframework,postgres,docker)


## Getting Started

### Python Itself
```bash
git clone https://github.com/richiepagard/drf-auth-boilerplate.git
cd drf-auth-boilerplate
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --username <username> --email <email address>
python3 manage.py runserver
```

### Docker
```bash
docker compose up -d --build
docker exec -it boilerplate-app bash
python3 manage.py createsuperuser
```

## Note

This project is just a starting point.
It's not meant for production use out of box.


## Project Status

Active development is ongoing.  
Several improvements and feature updates are currently implemented locally and will be pushed in upcoming revisions.


## License

**MIT**


## Contribution Instruction

[CONTRIBUTING.md](./CONTRIBUTING.md)

---

> "I built this to understand Django REST Framework + JWT better. Might help others too."
