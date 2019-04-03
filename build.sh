#!/bin/bash

list_dependencies=(rpm-build rpmdevtools)

for i in ${list_dependencies[*]}
do
    if ! rpm -qa | grep -qw $i; then
        echo "__________Dont installed '$i'__________"
        #yum -y install $i
    fi
done

rm -rf ~/rpmbuild/
mkdir -p ~/rpmbuild/{RPMS,SRPMS,BUILD,SOURCES,SPECS}
cd SOURCES
cp server-s3.conf ~/rpmbuild/SOURCES
cd ..
spectool -g -R wal-g-rpm.spec
rpmbuild -bb wal-g-rpm.spec
