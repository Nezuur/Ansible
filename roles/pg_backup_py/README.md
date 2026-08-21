# Ansible Role: pg_backup_py

Python-based PostgreSQL backup to AWS S3 using `pg_dump`, gzip, and boto3. Scheduled via cron.

For the shell/AWS CLI alternative, see `pg_backup_sh`. Use `pg_backup.yml` with `pg_backup_method=py`.

## Role Variables

Defined in `defaults/main.yml`:

- `pg_venv`: Virtualenv path. Default `/var/lib/pg_backup/venv/`.
- `pip_packages`: boto3 and related packages for S3 upload.
- `bucket_name`: S3 bucket name. Default `infra-backups-main`.
- `region_name`: AWS region. Default `eu-central-1`.
- `pg_backup.retention`: Local retention in days. Default `0`.
- `pg_backup.databases`: List of databases to dump. Default `[template1]`.
- `pg_backup.path`: Local backup path. Default `/var/lib/pg_backup`.
- `pg_backup.hour`: Cron hour. Default `1`.

Vault variables required by the env template:

- `vault_aws_access_key`
- `vault_aws_secret_key`

## Behaviour

1. Creates a Python 3.8 virtualenv and installs pip dependencies
2. Deploys `/opt/pg_db_backup.py` and `/opt/pg_backup_env`
3. Dumps databases as gzipped SQL (`.sql.gz`)
4. Uploads to `s3://<bucket>/pg_backup/`
5. Tags objects (`KeepAlways` on day 1, else `Keep32`)
6. Deletes local files older than `pg_backup.retention` days

## Usage

```yaml
- hosts: db
  become: true
  roles:
    - role: pg_backup_py
  vars:
    bucket_name: my-pg-backups
    region_name: eu-west-1
    pg_backup:
      retention: 7
      databases:
        - app_production
      path: /var/lib/pg_backup
      hour: 2
```

Or via the combined playbook:

```bash
ansible-playbook -i inventory/hosts.yml pg_backup.yml -e pg_backup_method=py
```
