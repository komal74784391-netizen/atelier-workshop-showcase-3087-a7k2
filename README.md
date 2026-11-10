# Larkspur Fieldworks — Workshop Showcase

Source of truth for the public workshop showcase. Each workshop lives in
`src/workshops/<slug>.md` and starts with a YAML front matter block.

Front matter keys:

- `workshop_code` — internal workshop identifier
- `title` — public workshop title
- `status` — `published` or `draft`
- `resource_link` — optional public URL of the workshop's companion lab folder
- `session_date` / `session_time` / `session_duration` — optional, may be recorded
  in whatever notation the coordinator used at the time

Companion lab materials live under `labs/`, one folder per workshop that has
them. Each lab folder carries its own README, which states the lab's release
status. The generated public index is stored at `catalog/workshop-index.csv`.
