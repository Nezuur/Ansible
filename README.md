# Description

This repository contains a collection of Ansible roles and playbooks for managing various tasks on Linux servers. Feel free to use and modify.

## Table of Contents

- [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Common](#common)
  - [Firewall](#firewall)
  - [SSH](#ssh)
  - [Backup](#backup)
  - [Certbot with Nginx](#certbot-with-nginx)
  - [MySQL Backup](#mysql-backup)
  - [Python from sources](#python-from-sources)
  - [Rbenv](#rbenv)
  - [Ruby](#ruby)
  - [PostgreSQL Backup with Bash](#postgresql-backup-with-bash)

## Common

This role performs common configuration tasks, such as setting up essential packages, configuring system settings, and adding SSH keys for server management.

## Firewall

This role configures iptables firewall rules to manage network traffic on a server. It allows specific types of traffic, such as SSH and ICMP, while setting the default policy to DROP for both IPv4 and IPv6. This ensures that only permitted traffic is allowed through, enhancing the security of the server.

## SSH

This role manages the SSH (Secure Shell) server configuration and firewall rules to secure SSH access to a server. It allows you to configure SSH to listen on a custom port and adjusts the firewall accordingly.

## Backup

Simple Ansible role that manages a backup process which creates compressed archives of files from a specified source directory and stores them in a destination directory. The backup is scheduled to run as a Cron job on the first day of each month.

## Certbot with Nginx

This Ansible role automates the deployment and renewal of Let's Encrypt SSL certificates for Nginx on Linux servers using Certbot, and is configured to run within a Python virtual environment.

## MySQL Backup

This Ansible role automates the process of creating and managing MySQL database backups. It sets up a Python environment on the target system, installs the necessary dependencies, and configures a script that performs the database backups. The backups are then compressed and uploaded to an AWS S3 bucket.

## Python from sources

This Ansible role installs a specific version of Python from source and manages certain package dependencies on a target system.

## Rbenv

This role installs and manages rbenv and its plugins on a system. It handles the installation of ruby-build and rbenv-vars plugins. Additionally, it sets up the necessary environment configurations within user profiles to ensure rbenv operates correctly.

## Ruby

This Ansible role manages the installation and configuration of Ruby using rbenv. It allows you to specify multiple Ruby versions to be installed, set a global Ruby version, and manage Ruby gems with Bundler.

## PostgreSQL Backup with Bash

This Ansible role automates the backup of PostgreSQL databases to an AWS S3 bucket. It installs necessary tools, manages a backup script, and schedules it via a cron job and a bash script.
