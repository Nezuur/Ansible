# python_old

Compiles a specific CPython version from source into `/opt` and symlinks it into `/usr/bin`. For when the distro package is too old and you don't want deadsnakes.

**Playbook:** `python_old.yml`

## Vars (`defaults/main.yml`)

- `python_ver` — e.g. `3.9.17`
- `python_install_dir` — default `/opt/python<major.minor>`

## Requires

`community.general` collection (`ansible-galaxy collection install -r requirements.yml`).
