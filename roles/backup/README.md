# Backup Role

This Ansible role manages a backup process that creates compressed archives of files from a specified source directory and stores them in a destination directory. It optionally cleans up the source folder. The backup is scheduled to run as a cron job on the first day of each month.

## Requirements

- Python 3.x
- Ansible

## Role Variables

The following variables can be configured in `defaults/main.yml`:

- `src_path`: The path to the source directory that contains the files to be backed up. Defaults to `/home/user/target/`.
- `dest_path`: The path to the destination directory where the backup archives will be stored. Defaults to `/home/user/backup/`.

## Files

- `backup.py`: The script responsible for compressing the backup files into a `.tgz` archive. It also features an optional cleanup operation that can remove the source directory after backing up, controlled by a command-line flag.

## Tasks

The role performs the following tasks:

1. **Copy Backup Script**: Copies the `backup.py` script to `/opt/backup.py` on the target machine and sets the executable mode.

2. **Setup Cron Job**: Schedules a cron job that runs the backup script at 5:00 AM on the first day of each month. The job uses the paths defined by the `src_path` and `dest_path` variables, and can include the cleanup source folder option if desired.

## Usage

To use this role, include it in your playbook and set the desired variables:

```yaml
- hosts: all
  roles:
    - backup
  vars:
    src_path: "/your/source/directory"
    dest_path: "/your/destination/directory"
```
