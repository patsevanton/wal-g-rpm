#!/bin/bash

list_dependencies=(rpm-build rpmdevtools)

for i in ${list_dependencies[*]}
do
    if ! rpm -qa | grep -qw $i; then
        echo "__________Dont installed '$i'__________"
        #yum -y install $i
    fi
done

mkdir -p ./{RPMS,SRPMS,BUILD,SOURCES,SPECS}
cp server-s3.conf backup-fetch.sh backup-list.sh backup-push.sh wal-push.sh SOURCES
spectool -g -C SOURCES wal-g-rpm.spec
rpmbuild --quiet --define "_topdir `pwd`" -bb wal-g-rpm.spec
