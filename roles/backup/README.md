# backup

Tars up `<source>/<year>/<month>/` into `<dest>/<year>/<year>-<month>.tgz`, monthly, via cron.

**Playbook:** `backup.yml`

## Vars

- `src_path` — source root (default `/home/user/target/`)
- `dest_path` — destination root (default `/home/user/backup/`)

## Notes

- Expects a `<year>/<month>` layout under `src_path` — not a generic directory backup
- Won't overwrite an existing archive for the month; fails instead
- `backup.py` supports `--cleanup` to delete the source folder after archiving, but the role doesn't pass it
