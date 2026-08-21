# sshd

Hardens SSH: custom listen port in `sshd_config`, plus Ubuntu 24.04 `ssh.socket` override.

## Variable (required)

- `sshd_custom_port` — set in the playbook (see `common.yml`). No role default.

```yaml
- hosts: all
  become: true
  vars:
    sshd_custom_port: 2200
  roles:
    - role: sshd
```
