# firewall_base

iptables baseline: allow SSH / ICMP / loopback, DROP everything else, persist rules.

## Variable

- `sshd_custom_port` — set in the playbook. If unset, opens port 22. If set, opens that port instead.

Used together with `sshd` from `common.yml`:

```yaml
vars:
  sshd_custom_port: 2200
```
