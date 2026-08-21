# firewall_base

iptables baseline: allow SSH / ICMP / loopback / established, DROP everything else (v4 + v6), persist rules.

**Playbook:** `common.yml`

## Vars

- `sshd_custom_port` — set in the playbook, not here. Unset → opens port 22 instead.

```yaml
vars:
  sshd_custom_port: 2200
```

Pairs with the `sshd` role, which reads the same variable.
