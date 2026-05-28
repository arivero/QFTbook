#!/usr/bin/env bash
set -euo pipefail

cluster_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$cluster_dir/../.." && pwd)"
env_file="$cluster_dir/rc_env.sh"

if [[ ! -f "$env_file" ]]; then
  cat >&2 <<'MSG'
Missing qft_scripts/cluster/rc_env.sh.
Copy qft_scripts/cluster/rc_env.example to rc_env.sh and edit the user paths.
MSG
  exit 2
fi

# shellcheck disable=SC1090
source "$env_file"

: "${RC_USER:?Set RC_USER in rc_env.sh}"
: "${RC_SSH_HOST:=qft-harvard-rc}"
: "${RC_REMOTE_REPO:?Set RC_REMOTE_REPO in rc_env.sh}"
: "${RC_REMOTE_RESULTS_ROOT:?Set RC_REMOTE_RESULTS_ROOT in rc_env.sh}"
: "${RC_LOCAL_RESULTS_ROOT:=results/cluster}"
: "${RC_TMUX_SESSION:=qft-monograph}"

RC_SSH_CONFIG="$cluster_dir/ssh_config_harvard_rc.conf"

ssh_base=(ssh -F "$RC_SSH_CONFIG" -l "$RC_USER" "$RC_SSH_HOST")
rsync_ssh=(ssh -F "$RC_SSH_CONFIG" -l "$RC_USER")

quote_remote_path() {
  printf "%q" "$1"
}
