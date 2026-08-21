# ruby

Installs one or more Ruby versions + Bundler via rbenv, for `app_user`.

**Playbook:** `ruby.yml` — depends on `rbenv` running first in the same play.

## Vars (`defaults/main.yml`)

- `app_user` — default `app`
- `ruby.versions` — list to install, e.g. `[3.0.3, 3.3.4]`
- `ruby.global` — which one becomes global
- `ruby.bundler` — bundler version installed for each

## What it does

Installs each version with `rbenv install`, sets the global one, then installs `bundler` per version under a temp `.ruby-version` directory.
