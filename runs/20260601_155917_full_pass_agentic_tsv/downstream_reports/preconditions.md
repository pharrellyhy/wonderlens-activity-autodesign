# Downstream Preconditions

Run: `20260601_155917_full_pass_agentic_tsv`

Checked by master agent before downstream load/live validation.

## Fullstack Demo

- Required worktree exists:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game`
- Branch: `feat/activity-text-game`
- Status: `## feat/activity-text-game...origin/feat/activity-text-game [ahead 1]`
- Credential source exists without printing values:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/.env`
- Service account source exists without printing values:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/.elaborate-baton-480304-r8-a8a39bcb34f1.json`

Note: the worktree is clean but one commit ahead of remote. This run will not
alter downstream repo history unless the user explicitly expands scope.

## WonderLens AI

- Required repo exists:
  `/Users/pharrelly/codebase/gitlab/wonderlens-ai`
- Branch: `main`
- Status: `## main...origin/main`
- Credential source exists without printing values:
  `/Users/pharrelly/codebase/gitlab/wonderlens-ai/.env`
- Service account source exists without printing values:
  `/Users/pharrelly/codebase/gitlab/wonderlens-ai/.elaborate-baton-480304-r8-a8a39bcb34f1.json`

## Commands

```bash
test -d /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game
git -C /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game branch --show-current
git -C /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game status --short --branch
test -f /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/.env
test -f /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/.elaborate-baton-480304-r8-a8a39bcb34f1.json

test -d /Users/pharrelly/codebase/gitlab/wonderlens-ai
git -C /Users/pharrelly/codebase/gitlab/wonderlens-ai branch --show-current
git -C /Users/pharrelly/codebase/gitlab/wonderlens-ai status --short --branch
test -f /Users/pharrelly/codebase/gitlab/wonderlens-ai/.env
test -f /Users/pharrelly/codebase/gitlab/wonderlens-ai/.elaborate-baton-480304-r8-a8a39bcb34f1.json
```
