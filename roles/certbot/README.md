# certbot

Let's Encrypt via apt's `certbot` + `python3-certbot-nginx`, standalone mode, with pre/post iptables hooks for port 80.

**Playbook:** `certbot.yml`

## Vars

None — uses `ansible_host` as both the domain and the `--email` (`root@<ansible_host>`).

## What it does

1. Installs certbot + nginx plugin
2. Deploys pre/post renewal hooks that open/close port 80
3. Issues the cert (`certonly --standalone`) if it doesn't already exist
4. Crons `certbot renew` every 2 days

## Note

Ships the same `certbot-nginx-{pre,post}hook.sh` files as `certbot_nginx` — pick one role, not both, per host.
