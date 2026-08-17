#!/usr/bin/env bash
set -euo pipefail

: "${SPECIALIST_ROOT:=/opt/earthscientist-specialists}"
: "${WRF_TAG:=v4.6.1}"

mkdir -p "${SPECIALIST_ROOT}"

if [[ ! -d "${SPECIALIST_ROOT}/WRF/.git" ]]; then
  git clone --depth 1 --branch "${WRF_TAG}" https://github.com/wrf-model/WRF.git "${SPECIALIST_ROOT}/WRF"
fi

cat <<'EOF'
WRF source has been pinned and downloaded but is not compiled automatically.
Compilation requires site-specific NetCDF, MPI, compiler, nesting, and physics choices.

HYSPLIT is intentionally not downloaded by this script. Install the official NOAA
distribution and expose hyts_std and hycs_std on PATH. The EarthVerse runtime records
the exact executable path and refuses to emulate either program.
EOF
