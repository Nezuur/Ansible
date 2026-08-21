# Ansible Role: Certbot

Installs Certbot with the Nginx plugin via apt and configures Let's Encrypt renewal hooks that manage iptables around certificate renewals.

## Role Variables

None required. The role uses the target host's `ansible_host` as the certificate domain and `root@{{ ansible_host }}` as the Let's Encrypt email.

## Tasks

1. Install `certbot` and `python3-certbot-nginx`.
2. Create `/etc/letsencrypt/renewal-hooks/{pre,post}/` directories.
3. Deploy pre- and post-renewal hook scripts.
4. Obtain an SSL certificate for `ansible_host` via the Nginx plugin.

## Usage

```yaml
- hosts: web
  become: true
  roles:
    - role: certbot
```

For a virtualenv-based Certbot install with explicit email and domain, use the `certbot_nginx` role instead.
