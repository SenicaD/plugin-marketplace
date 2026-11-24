# senicad-tools

A personal Claude Code marketplace. It currently holds one plugin, **factory**.

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

### Test locally

```
claude plugin validate .
claude plugin marketplace add ./
claude plugin install factory@senicad-tools
```
