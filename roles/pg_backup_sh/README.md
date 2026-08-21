# Ansible Role: pg_backup_sh

Shell-based PostgreSQL backup to AWS S3 using `pg_dump` and the AWS CLI. Scheduled via cron.

For the Python/boto3 alternative, see `pg_backup_py`. Use `pg_backup.yml` with `pg_backup_method=sh`.

## Role Variables

Defined in `defaults/main.yml`:

- `db_name_1` / `db_name_2`: Databases to dump. Defaults `foo` / `bar`.
- `pg_backups_dir`: Local staging directory. Default `/usr/lib/pg_backups`.
- `pg_backups_time_hour`: Cron hour. Default `"05"`.
- `pg_backups_aws_key`: AWS access key ID.
- `pg_backups_aws_secret`: AWS secret access key.
- `pg_backups_aws_bucket`: S3 bucket name.
- `pg_backups_aws_region`: AWS region.

## Behaviour

1. Installs `awscli`
2. Deploys `/usr/local/bin/pg_backup` from `templates/pg_backup.sh.j2`
3. Dumps databases as custom-format `.dump` files
4. Uploads to `s3://<bucket>/postgresql/`
5. Tags objects (`KeepAlways` on day 1, else `Keep32`)
6. Deletes local `.dump` files older than 12 hours

## Usage

```yaml
- hosts: db
  become: true
  roles:
    - role: pg_backup_sh
  vars:
    db_name_1: app_production
    db_name_2: app_analytics
    pg_backups_aws_key: "{{ vault_aws_access_key }}"
    pg_backups_aws_secret: "{{ vault_aws_secret_key }}"
    pg_backups_aws_bucket: my-pg-backups
    pg_backups_aws_region: eu-central-1
```

Or via the combined playbook:

```bash
ansible-playbook -i inventory/hosts.yml pg_backup.yml -e pg_backup_method=sh
```
