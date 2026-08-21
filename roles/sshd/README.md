# sshd

Moves SSH off the default port: `sshd_config` +, on Ubuntu 24.04, the `ssh.socket` override that `sshd_config`'s `Port` directive can't reach.

**Playbook:** `common.yml`

## Vars (required, no default)

- `sshd_custom_port` — set in the playbook (see `common.yml`). The role asserts it's set before doing anything.

```yaml
vars:
  sshd_custom_port: 2200
```
