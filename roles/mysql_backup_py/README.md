# Ansible Role: MySQL Backup

This Ansible role automates the process of creating and managing MySQL database backups. It sets up a Python environment on the target system, installs the necessary dependencies, and configures a script that performs the database backups. The backups are then compressed and uploaded to an AWS S3 bucket.

## Main Features

Automated Backup Setup: Installs Python, virtualenv, and all required Python packages to manage the database backup process.

MySQL Backup Script: Utilizes a Python script `(db_backup.py)` that handles database dumps, compressions, and uploads to S3.

Configurable via Variables: All significant parameters like AWS credentials, database details, backup retention, and scheduling can be configured through default variables.

`Scheduling:` Integrates with cron to schedule backups at specified intervals, ensuring regular backup operations.

`Environment Configuration:` Uses a Jinja2 template to configure environment variables needed by the backup script.

## Requirements

This role requires Python and several Python packages which are handled by the role itself. Ensure that the target system has internet connectivity to download necessary packages.

## Example Configuration

Below is an example configuration snippet from the defaults/main.yml:

```yaml

mysql_backup:
  retention: 7  # days for backup retention
  databases:
    - mydatabase
  aws_access_key: 'AKIAIOSFODNN7EXAMPLE'
  aws_secret_key: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
  bucket_name: 'my-bucket'
  aws_region: 'us-west-2'
  s3_folder: 'mydatabase_backups'
  path: '/var/lib/mysql_backup'
  hour: 3  # Scheduled backup hour
  mysql_user: 'db_user'
  mysql_password: 'db_pass'

```

This role is designed to simplify the management of database backups for MySQL, utilizing AWS S3 as a remote storage solution. It is not a well written program, but it is working.
