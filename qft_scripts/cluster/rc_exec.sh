#!/usr/bin/env bash
set -euo pipefail

cluster_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=rc_common.sh
source "$cluster_dir/rc_common.sh"

if [[ "$#" -eq 0 ]]; then
  echo "Usage: qft_scripts/cluster/rc_exec.sh <remote command...>" >&2
  exit 2
fi

remote_repo="$(quote_remote_path "$RC_REMOTE_REPO")"
remote_results="$(quote_remote_path "$RC_REMOTE_RESULTS_ROOT")"

"${ssh_base[@]}" "mkdir -p $remote_repo $remote_results && cd $remote_repo && export QFT_CLUSTER_RESULTS=$remote_results && $*"
