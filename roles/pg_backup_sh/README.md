# Ansible Role: PostgreSQL Backup shell

This Ansible role automates the backup of PostgreSQL databases to an AWS S3 bucket. It installs necessary tools, manages a backup script, and schedules it via a cron job and a bash script.

## Role Variables

Define these variables in your playbook or inventory to customize the behavior of the role:

- `pg_backups_dir`: Directory where backups are temporarily stored before uploading. Default is `/usr/lib/pg-backups`
- `pg_backups_time_hour`: Hour at which the backup cron job will run. Default is `"05"`
- `pg_backups_aws_key`: AWS Access Key ID for accessing S3
- `pg_backups_aws_secret`: AWS Secret Access Key for accessing S3
- `pg_backups_aws_bucket`: Name of the S3 bucket for backup storage
- `pg_backups_aws_region`: AWS region where the S3 bucket is located. Default is `eu-central-1`

## Setup

1. Ensure AWS credentials are securely set either in the playbook or by configuring your environment to use IAM roles.
2. Populate necessary variables as described above. Ensure they are defined in your Ansible inventory or playbook.

## Usage

- This role installs the AWS CLI if necessary, creates a backup script from the template, and configures a cron job to run the script daily at the specified hour.
- Backups are stored in the specified S3 bucket, and the local copies are deleted after 12 hours by default to save space.

## Backup Script

The backup script performs the following:

1. Dumps specified PostgreSQL databases to the local filesystem
2. Uploads the dump files to an S3 bucket
3. Tags the S3 objects for retention based on the day of the month
4. Cleans up old local dump files

## Security Considerations

- Avoid hardcoding AWS credentials in variables
- Review the cron job schedule
