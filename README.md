# senicad-tools

A personal Claude Code marketplace. It holds three plugins: **factory**, **spec** and **domain**.

## domain

Company domain knowledge for Claude. The knowledge itself lives in a separate git repo
(`domain-knowledge`: one markdown note per system, concept, flow or decision); this plugin
reads it and helps grow it.

```
/plugin install domain@senicad-tools
/domain <question>    answer from the notes, citing them; says "not documented" rather than guess
/domain add <fact>    record a fact in the right note, through a pull request
/domain curate        turn inbox dumps into proper notes, through a pull request
/domain sync          update the local clone
/domain check         validate the notes and the generated index
```

The skill also triggers on its own when a question needs company-specific facts.

Requires `git`, `gh` (authenticated, with access to the knowledge repo) and `python3` with
PyYAML. On first use the plugin clones the repo to `~/.cache/domain-knowledge` and
fast-forwards it at most once an hour. To use a clone you already work in, set
`DOMAIN_KB_PATH` or write `~/.config/domain/config.json`:

```json
{ "path": "/path/to/domain-knowledge", "repo": "git@github.com:<org>/domain-knowledge.git" }
```

A clone with local changes, or on a non-default branch, is never updated.

## factory

A software factory for GitHub issues. `/factory run` takes every open issue labeled
`factory` through intake, spec, build, gate, review and approve, one pull request per
issue, each job in its own git worktree. Several windows can run it at once.

### Install

```
/plugin marketplace add <your-github-user>/<this-repo>
/plugin install factory@senicad-tools
```

Requires `git`, `gh` (authenticated), `python3`, and a GitHub remote.

### Set up a repo

Run `/factory init` in the repo. It creates `factory/checks.sh` (the gate: put your tests
and build here), `factory/PROJECT.md` (what the agents should know about the project),
the dashboard, the GitHub labels and the `.gitignore` entries. Then label an issue
`factory` and run `/factory run`. See `examples/cardvault-PROJECT.md` for a filled-in
PROJECT.md.

### Defaults and overrides

Agents run on sonnet (intake, spec-writer, approver and analyst on opus) with the effort
levels in `plugins/factory/agents/*.md`. Routing, limits, labels and prices are in
`plugins/factory/defaults/config.json`. To override any key for one repo, copy that file
to `factory/config.json` in the repo and edit it; its keys replace the defaults.

State lives in the repo (`factory/jobs/`, `.worktrees/`), never in the plugin.

## spec

`/spec:spec <proposition>` (or just `/spec`) works a proposition into a reviewed spec: it
reads the repo, asks one batch of scoping questions, drafts, revises with you, saves
`docs/specs/<slug>.md`, then files a GitHub issue after you confirm. The `factory` label is
only added if you say so. Works in any repo; needs `gh` for the issue step.

```
/plugin install spec@senicad-tools
```

### Test locally

```
claude plugin validate .
claude plugin marketplace add ./
claude plugin install factory@senicad-tools
```
