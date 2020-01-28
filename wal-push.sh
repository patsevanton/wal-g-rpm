#!/bin/bash
set -e

source /etc/wal-g.d/server-s3.conf

if [ ! -z "$WALE_S3_PREFIX" ]; then
  /usr/local/bin/wal-g wal-push $PGDATA/$1
fi
