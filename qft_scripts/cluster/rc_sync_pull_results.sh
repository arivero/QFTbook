#!/usr/bin/env bash
set -euo pipefail

cluster_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=rc_common.sh
source "$cluster_dir/rc_common.sh"

mkdir -p "$repo_root/$RC_LOCAL_RESULTS_ROOT"

rsync -az \
  -e "${rsync_ssh[*]}" \
  "$RC_SSH_HOST:$(quote_remote_path "$RC_REMOTE_RESULTS_ROOT")/" \
  "$repo_root/$RC_LOCAL_RESULTS_ROOT/"

echo "Pulled cluster results into $repo_root/$RC_LOCAL_RESULTS_ROOT"
