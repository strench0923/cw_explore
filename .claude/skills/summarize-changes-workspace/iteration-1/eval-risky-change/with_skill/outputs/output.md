- Added a hardcoded `API_KEY` constant in `app.py` containing what looks like a live-style secret key.
- Updated `fetch_user` to send this API key as a `Bearer` token in the `Authorization` header on requests to the users endpoint.
- Added a new `delete_all_users` function that sends a POST request to a `delete_all` endpoint, also authenticated with the hardcoded key.

Risks:
- Hardcoded secret: The API key is committed directly in source code rather than loaded from an environment variable or secrets manager — this is a credential leak risk, especially if this repo is pushed anywhere shared.
- Destructive, unguarded function: `delete_all_users` calls a "delete all" endpoint with no confirmation, authorization check, dry-run option, or error handling — easy to trigger accidentally with irreversible consequences.
- No error handling: Neither `fetch_user` nor `delete_all_users` checks the response status code or handles request failures (e.g., network errors, 401/403 from a bad/expired key).
- No tests: There don't appear to be any tests covering the new `delete_all_users` behavior or the auth header change.
