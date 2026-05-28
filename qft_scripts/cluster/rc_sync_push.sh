#!/usr/bin/env bash
set -euo pipefail

cluster_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=rc_common.sh
source "$cluster_dir/rc_common.sh"

"${ssh_base[@]}" "mkdir -p $(quote_remote_path "$RC_REMOTE_REPO") $(quote_remote_path "$RC_REMOTE_RESULTS_ROOT")"

rsync -az --delete \
  --exclude '.git/' \
  --exclude '.DS_Store' \
  --exclude 'references/' \
  --exclude 'monograph/tex/*.pdf' \
  --exclude 'monograph/tex/build/' \
  --exclude 'results/cluster/' \
  -e "${rsync_ssh[*]}" \
  "$repo_root/" "$RC_SSH_HOST:$(quote_remote_path "$RC_REMOTE_REPO")/"

echo "Synced source tree to $RC_SSH_HOST:$RC_REMOTE_REPO"
