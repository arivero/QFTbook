#!/usr/bin/env bash
set -euo pipefail

cluster_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=rc_common.sh
source "$cluster_dir/rc_common.sh"

remote_repo="$(quote_remote_path "$RC_REMOTE_REPO")"
remote_session="$(quote_remote_path "$RC_TMUX_SESSION")"

"${ssh_base[@]}" -t "mkdir -p $remote_repo && cd $remote_repo && tmux new -A -s $remote_session"
