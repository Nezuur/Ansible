# pg_backup_py

PostgreSQL → S3 backup, Python venv + boto3. See `pg_backup_sh` for the bash equivalent — they are not interchangeable (different dump format, S3 prefix).

**Playbook:** `pg_backup.yml -e pg_backup_method=py`

## Vars (`defaults/main.yml`)

- `bucket_name` / `region_name` — required, no default
- `pg_backup.databases` — list of DBs to dump
- `pg_backup.retention` — local retention in days
- `pg_backup.hour` — cron hour
- `vault_aws_access_key` / `vault_aws_secret_key` — read by the env template, not defined here

## What it does

1. Builds a venv, pip-installs boto3 + deps
2. Copies `pg_db_backup.py`, renders `/opt/pg_backup_env`
3. Crons: `pg_dump` \| gzip each DB → `s3://<bucket>/pg_backup/`, tags `KeepAlways` on the 1st else `Keep32`, deletes local files past retention
