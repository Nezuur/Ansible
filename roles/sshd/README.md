# Ansible Role: SSHD

This role manages the SSH (Secure Shell) server configuration and firewall rules to secure SSH access to a server. It allows you to configure SSH to listen on a custom port and adjusts the firewall accordingly.

## Requirements

This role requires a system with SSH installed. Ensure that your target system meets Ansible's requirements.

## Role Variables

- `sshd_custom_port`: Defaults to 2200. Use this variable to specify a custom SSH port. The role automatically configures iptables and the SSH daemon to use this port.

## Dependencies

This role has no dependencies on other Ansible roles.

## Tasks

The role performs the following tasks:

- **Allow SSH on custom port:** Configures iptables to allow TCP traffic on the custom SSH port.
- **Configure SSH for Ubuntu <= 22.04:** Uses a template to configure SSH settings in `/etc/ssh/sshd_config`.
- **Configure SSH for Ubuntu == 24.04:** Sets up a systemd socket override configuration to listen on the custom SSH port.
- **Restart services:** Reloads the SSH daemon configuration and ensures iptables rules are saved.

## Handlers

- **restart sshd:** Restarts the SSH service to apply changes.
- **daemon-reload:** Reloads the systemd daemon to recognize new or changed configurations.
- **save iptables:** Saves the current iptables configuration to ensure persistence across reboots.

## Example Playbook

Here's an example of how to use this role in a playbook:

```yaml

- hosts: all
  roles:
    - role: sshd

```
