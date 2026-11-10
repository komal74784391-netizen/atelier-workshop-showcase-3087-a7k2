# Larkspur Fieldworks — Workshop Showcase

Source of truth for the public workshop showcase. Each workshop lives in
`src/workshops/<slug>.md` and starts with a YAML front matter block.

Front matter keys:

- `workshop_code` — internal workshop identifier
- `title` — public workshop title
- `status` — `published` or `draft`
- `resource_link` — optional URL of the workshop's released companion repository
- `session_date` / `session_time` / `session_duration` — optional, may be recorded
  in whatever notation the coordinator used at the time

The generated public index is stored at `catalog/workshop-index.csv`.
