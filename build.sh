#!/bin/bash
# USAGE: ./build.sh
set -e

echo "Build static website..."
rm -rf public
hugo --config "hugo.toml"

# echo "Check HTML..."
# htmlproofer public \
#     --allow-hash-href \
#     --check-html \
#     --empty-alt-ignore \
#     --disable-external
