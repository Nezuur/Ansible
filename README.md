# Personal Ansible notes / lab roles

Lab roles and playbooks I use on Ubuntu boxes. Not a framework. Copy what you need into your own inventory and set the variables for your environment.

## Quick start

```bash
# inventory is local / gitignored — create inventory/hosts.yml yourself
ansible-playbook -i inventory/hosts.yml common.yml
```

Set shared values in the playbook `vars:` (see `common.yml` for `sshd_custom_port`), not by editing role defaults when you can avoid it.

## Playbooks → roles

| Playbook | Role(s) | Why it exists |
|----------|---------|---------------|
| `common.yml` | `common`, `firewall_base`, `sshd` | Base host: packages, DROP firewall, SSH on a non-default port |
| `ruby.yml` | `rbenv`, `ruby` | App-user Ruby via rbenv + bundler |
| `pg_backup.yml` | `pg_backup_sh` **or** `pg_backup_py` | Postgres → S3; pick one method (`-e pg_backup_method=sh\|py`) |
| `mysql_backup_py.yml` | `mysql_backup_py` | MySQL/Percona → S3 via Python |
| `backup.yml` | `backup` | Simple file-tree tarball on a monthly cron |
| `certbot.yml` | `certbot` | Let's Encrypt via apt certbot + nginx plugin |
| `certbot_nginx.yml` | `certbot_nginx` | Same goal in a venv (when apt certbot is not enough) |
| `python_old.yml` | `python_old` | Build a pinned Python from source into `/opt` |

## Roles (what / why)

| Role | What | Why |
|------|------|-----|
| `common` | Packages, timezone, root SSH keys from URLs | Minimal baseline every lab host needs |
| `firewall_base` | iptables ACCEPT for SSH/ICMP/lo, else DROP | Lock down a fresh VM without ufw |
| `sshd` | `sshd_config` + Ubuntu 24.04 `ssh.socket` port | Move SSH off 22; requires `sshd_custom_port` |
| `rbenv` | Clone rbenv + plugins for `app_user` | Prerequisite for `ruby` |
| `ruby` | Install Ruby versions + bundler via rbenv | App runtime without system Ruby |
| `pg_backup_sh` | `pg_dump -F c` + awscli → S3 | Lightweight PG backup (custom format) |
| `pg_backup_py` | `pg_dump`\|gzip + boto3 → S3 | Same idea when you prefer Python/venv |
| `mysql_backup_py` | mysqldump-style flow + boto3 → S3 | MySQL backups without shell glue |
| `backup` | Cron + Python tarball of a directory | Ad-hoc file backups |
| `certbot` | apt certbot + renew hooks | Fast TLS on nginx |
| `certbot_nginx` | venv certbot + iptables hooks | TLS when you need an isolated certbot |
| `python_old` | Compile CPython from source | When distro Python is too old |

**SSH port:** one variable, `sshd_custom_port`, set in `common.yml`. `firewall_base` and `sshd` both read it. Do not set two different names.

**PG backups:** same job, different dump format and S3 prefix — use one method per host. See role READMEs for vars.

## Not published

Local-only / ignored: `strong_swan`, inventory, secrets. Do not expect them in the remote repo.
