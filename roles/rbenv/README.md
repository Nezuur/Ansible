# rbenv

Installs rbenv + `ruby-build`/`rbenv-vars` plugins for `app_user`, wires `PATH` into `~/.profile`.

**Playbook:** `ruby.yml` (always paired with the `ruby` role — see below)

## Vars

Shares `app_user` and `ruby.*` with the `ruby` role (defined in `roles/ruby/defaults/main.yml`); `rbenv` has no defaults of its own. Run both roles in the same play.

```yaml
roles:
  - role: rbenv
  - role: ruby
```
