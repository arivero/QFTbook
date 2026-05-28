#!/usr/bin/env bash
set -euo pipefail

cluster_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=rc_common.sh
source "$cluster_dir/rc_common.sh"

ssh -F "$RC_SSH_CONFIG" -l "$RC_USER" -O exit "$RC_SSH_HOST" || true
echo "Closed SSH master for $RC_USER@$RC_SSH_HOST if it was active."
