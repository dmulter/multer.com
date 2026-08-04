#!/bin/bash
# USAGE: ./deploy.sh
set -e

echo "Upload to S3..."
s3deploy \
    -source public \
    -bucket multer.com \
    -distribution-id xxxxx \
    -region us-west-2
