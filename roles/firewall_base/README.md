# Ansible Role: Firewall Base

This role configures iptables firewall rules to manage network traffic on a server. It allows specific types of traffic, such as SSH and ICMP, while setting the default policy to DROP for both IPv4 and IPv6. This ensures that only permitted traffic is allowed through, enhancing the security of the server.

## Requirements

This role is designed to work on systems where iptables is available and properly installed. Ensure that your target system meets Ansible's requirements and has iptables installed.

## Role Variables

- `custom_ssh_port`: Define a custom SSH port if different from the default port 22.

## Dependencies

This role has no dependencies on other Ansible roles.

## Tasks

The role performs the following tasks:

- **Allow SSH traffic:** Opens port 22 for incoming SSH connections if `custom_ssh_port` is not defined.
- **Allow SSH on a custom port:** Opens a user-defined custom port for SSH if `custom_ssh_port` is defined.
- **Allow ICMP traffic:** Permits ICMP packets for network diagnostics.
- **Allow loopback traffic:** Ensures that traffic from the loopback interface is not dropped.
- **Set default DROP policy:** Configures iptables to drop all traffic by default for both IPv4 and IPv6.
- **Save firewall configuration:** Ensures that the current iptables configuration is saved and persistent across reboots.

## Example Playbook

Here's an example of how to use this role in a playbook:

```yaml

- hosts: all
  roles:
    - role: firewall_base

```
