%global _prefix /usr/local
%global __strip /bin/true

Name:    wal-g-pg
Version: 1.0
Release: 1
Summary: Archival and Restoration for Postgres

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/wal-g/wal-g/releases/download/v1.0/wal-g-pg-ubuntu-18.04-amd64.tar.gz
Source0: build.sh

%description
WAL-G is the successor of WAL-E with a number of key differences. WAL-G uses LZ4, LZMA or Brotli compression, multiple processors
and non-exclusive base backups for Postgres. More information on the design and implementation of WAL-G can be found on the
Citus Data blog post "Introducing WAL-G by Citus: Faster Disaster Recovery for Postgres".

%prep
curl -L %{url} -o wal-g-pg-ubuntu-18.04-amd64.tar.gz
tar -zxf wal-g-pg-ubuntu-18.04-amd64.tar.gz
ls

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
cp wal-g-pg-ubuntu-18.04-amd64 %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
