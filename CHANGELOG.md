# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/).

## [1.4.0] - 2026-12-01

### Added
- Health check endpoints: `health/live/` (liveness) and `health/ready/` (readiness, checks the database).
- JWT token blacklist, so logout invalidates the refresh token.
- Swagger response schemas for register and login.
- Regression tests for the auth fixes.
- `.env.example` file.

### Changed
- Login now returns `200 OK` instead of `202 Accepted`.
- Registration now rejects weak passwords (Django password validators).
- Usernames and emails are now normalized to lowercase.

### Fixed
- Logout crashed with a 500 error when the refresh token was invalid or expired; it now returns 400.
- Registering with a different letter case (`Richie` vs `richie`) caused a server error instead of a validation error.
- Login failed when the username was typed with different letter case.
- Swagger showed wrong status codes for register and logout.
