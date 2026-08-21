# common

Baseline for a fresh Ubuntu box: DNS, packages, timezone, root SSH keys, a couple of shell defaults.

**Playbook:** `common.yml`

## Vars

- `team_ssh_keys` — list of `https://github.com/<user>.keys` URLs added to root's `authorized_keys`

## What it does

- Sets `/etc/resolv.conf` (localhost + Google DNS)
- Installs common CLI packages (curl, git, htop, tcpdump, vim, ...)
- Sets timezone to UTC, locale to `en_US.UTF-8`
- Adds root SSH keys, an `ll` alias, `$EDITOR=vim`
