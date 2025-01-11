# rbenv Ansible Role

This role installs and manages rbenv and its plugins on a system. It handles the installation of ruby-build and rbenv-vars plugins. Additionally, it sets up the necessary environment configurations within user profiles to ensure rbenv operates correctly.

## Role Variables

- `app_user`: The user for whom the rbenv should be configured. Defaults to `app`.
- `ruby.rbenv_root`: Directory where rbenv is installed. Defaults to `/home/{{ app_user }}/.rbenv`.
- `ruby.rbenv_plugins`: Directory for rbenv plugins. Defaults to `/home/{{ app_user }}/.rbenv/plugins`.
- `ruby.bundler`: Version of bundler to install. Defaults to `2.3.4`.
- `ruby.global`: Default global ruby version. Defaults to `3.0.3`.
- `ruby.versions`: List of ruby versions to install. Defaults are `3.0.3` and `3.3.4`.

## Handlers

- `bash reload`: Reloads the bash profile for changes to take effect.

## Tags

- `rbenv`: Apply to tasks related to rbenv installation and configuration.
- `ruby`: Apply to tasks that handle ruby version management and installation.
- `bundler`: Apply to tasks for setting up ruby environments with bundler.

## Usage

To use this role, include it in your playbook as shown below:

```yaml

- hosts: all
  become: true
  become_user: "{{ app_user }}"
  roles:
    - { role: rbenv, tags: [rbenv] }

```

Configure any necessary variables to fit your environment and requirements.
