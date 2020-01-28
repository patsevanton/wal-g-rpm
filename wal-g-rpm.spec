%global _prefix /usr/local
%global __strip /bin/true

Name:    wal-g
Version: 0.2.14
Release: 9
Summary: Archival and Restoration for Postgres

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/wal-g/wal-g/releases/download/v%{version}/wal-g.linux-amd64.tar.gz
Source0: server-s3.conf
Source1: backup-fetch.sh
Source2: backup-list.sh
Source3: backup-push.sh
Source4: wal-push.sh

%description
WAL-G is the successor of WAL-E with a number of key differences. WAL-G uses LZ4, LZMA or Brotli compression, multiple processors
and non-exclusive base backups for Postgres. More information on the design and implementation of WAL-G can be found on the
Citus Data blog post "Introducing WAL-G by Citus: Faster Disaster Recovery for Postgres".

%prep
curl -L %{url} > wal-g.linux-amd64.tar.gz
tar -zxf wal-g.linux-amd64.tar.gz

%install
%{__install} -m 0755 -d %{buildroot}/etc/wal-g.d/
%{__install} -m 0644 %{SOURCE0} %{buildroot}/etc/wal-g.d/server-s3.conf
%{__install} -m 0755 -d %{buildroot}%{_bindir}
cp wal-g %{buildroot}%{_bindir}/%{name}
cp %{SOURCE1} %{buildroot}%{_bindir}/backup-fetch.sh
cp %{SOURCE2} %{buildroot}%{_bindir}/backup-list.sh
cp %{SOURCE3} %{buildroot}%{_bindir}/backup-push.sh
cp %{SOURCE4} %{buildroot}%{_bindir}/wal-push.sh

%files
%{_bindir}/%{name}
%{_bindir}/backup-fetch.sh
%{_bindir}/backup-list.sh
%{_bindir}/backup-push.sh
%{_bindir}/wal-push.sh
/etc/wal-g.d/server-s3.conf
