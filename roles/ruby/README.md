# Ruby Role

This Ansible role manages the installation and configuration of Ruby using rbenv. It allows you to specify multiple Ruby versions to be installed, set a global Ruby version, and manage Ruby gems with Bundler.

## Dependencies

This role relies on the `rbenv` role to be installed first.

## Role Variables

- **app_user**: The user under which rbenv and Ruby are installed. Default is `app`.
- **ruby.rbenv_root**: The root directory for rbenv. Default is `/home/{{ app_user }}/.rbenv`.
- **ruby.rbenv_plugins**: The directory for rbenv plugins. Default is `/home/{{ app_user }}/.rbenv/plugins`.
- **ruby.bundler**: The version of Bundler to install. Default is `2.3.4`.
- **ruby.global**: The global Ruby version to set. Default is `3.0.3`.
- **ruby.versions**: A list of Ruby versions to install. Default is `[3.0.3, 3.3.4]`.

## Handlers

- **rbenv rehash**: Runs the `rbenv rehash` command to update rbenv's shims.

## Tasks

- Fetch the current global Ruby version.
- Set global variables for rbenv environment path.
- Install specified Ruby versions using rbenv.
- Set the specified global Ruby version.
- Create temporary directories for the Ruby versions.
- Set up local `.ruby-version` files in temporary directories.
- Install the specified version of Bundler in each Ruby environment.

## Templates

- A template for `.ruby-version` files is provided to specify local Ruby versions in the created directories.

## Usage

To use this role, include it in your playbook as shown below:

```yaml

- hosts: all
  become: true
  become_user: "{{ app_user }}"
  roles:
    - { role: rbenv, tags: [rbenv] }
    - { role: ruby, tags: [ruby] }

```

Configure any necessary variables to fit your environment and requirements.
