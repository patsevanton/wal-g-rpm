#!/bin/bash
set -e

source /etc/wal-g.d/server-s3.conf

/usr/local/bin/wal-g backup-fetch /var/lib/pgsql/$PG_VER/data LATEST
