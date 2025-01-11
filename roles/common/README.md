# Ansible Role: Common

This role performs common configuration tasks, such as setting up essential packages, configuring system settings, and adding SSH keys for server management.

## Requirements

This role is tested on various Debian-based systems and is intended for use in similar environments. Ensure that the target machine meets Ansible's minimum requirements for managed hosts.

## Role Variables

Variables that can be customized in this role:

- `team_ssh_keys`: A list of URLs to SSH public keys. The keys specified here will be added to the root user's authorized keys.

Example configuration in `group_vars`:

```yaml

team_ssh_keys:
  - https://github.com/alice.keys
  - https://github.com/bob.keys

```

## Dependencies

This role has no dependencies on other Ansible roles.

## Tasks

The role performs the following tasks:

`Set resolv.conf:` Configures DNS by setting the resolv.conf to use local and Google's DNS servers.

`Install common packages:` Installs essential utilities required for system management and development.

`Set timezone:` Configures the server to use the UTC timezone.

`Add ssh keys for root:` Adds SSH keys to the root user's authorized_keys for remote access.

`Add bash alias:` Adds an alias for ll to list directory contents in color.

`Set default editor:` Sets vim as the default editor.

`Fix locale setup:` Ensures the locale is configured to en_US.UTF-8.

## Example Playbook

Here's an example of how to use this role in a playbook:

```yaml

- hosts: all
  roles:
    - role: common

```
