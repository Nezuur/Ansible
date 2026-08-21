# certbot_nginx

Same goal as `certbot`, but certbot runs from a Python venv instead of the apt package — for when you want it isolated from system Python.

**Playbook:** `certbot_nginx.yml`

## Vars (`defaults/main.yml`)

- `certbot_email` — required, no default
- `web_domain` — defaults to `{{ domain_name }}` (set `domain_name` in the playbook)
- `python_ver` — default `3.8`
- `venv_dir` — default `/opt/certbot/`

## What it does

1. Builds a venv, pip-installs `certbot` + `certbot-nginx`
2. Opens 80/443 via iptables
3. Issues the cert (`certonly --standalone`) if missing
4. Crons renewal every 2 days with the same pre/post hooks as `certbot`

## Note

Ships the same hook scripts as `certbot` — pick one role, not both, per host.
