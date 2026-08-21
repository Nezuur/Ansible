# mysql_backup_py

Dumps MySQL/Percona databases and uploads them to S3. Runs in a Python venv, scheduled via cron.

**Playbook:** `mysql_backup_py.yml`

## Vars (`defaults/main.yml`, override in playbook)

- `mysql_backup.databases` — list of DBs to dump
- `mysql_backup.aws_access_key` / `aws_secret_key` / `bucket_name` / `aws_region` / `s3_folder`
- `mysql_backup.mysql_user` / `mysql_password`
- `mysql_backup.retention` — local retention in days
- `mysql_backup.hour` — cron hour
- `db_backup_env_dest` — where the env file with the above gets written

## What it does

1. Creates a venv, installs boto3 + deps
2. Copies `db_backup.py` and renders its env file
3. Crons the dump → S3 upload → local cleanup

## Note

Default `db_backup_env_dest` is `/etc/zabbix/scripts/db_backup.env` — leftover from where this was originally deployed. Set it to something like `/opt/db_backup.env` if you don't run Zabbix (the playbook already does this).
