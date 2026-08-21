# pg_backup_sh

PostgreSQL → S3 backup, bash + `awscli`. See `pg_backup_py` for the Python equivalent — they are not interchangeable (different dump format, S3 prefix).

**Playbook:** `pg_backup.yml -e pg_backup_method=sh`

## Vars (`defaults/main.yml`)

- `db_name_1` / `db_name_2` — databases to dump (only two, by design)
- `pg_backups_dir` — local staging dir
- `pg_backups_time_hour` — cron hour
- `pg_backups_aws_key` / `aws_secret` / `aws_bucket` / `aws_region`

## What it does

1. Installs `awscli`
2. Renders `pg_backup.sh.j2` to `/usr/local/bin/pg_backup`, crons it
3. Script: `pg_dump -F c` each DB → `s3://<bucket>/postgresql/`, tags `KeepAlways` on the 1st else `Keep32`, deletes local dumps older than 12h
