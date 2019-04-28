%global _prefix /usr/local

Name:    wal-g
Version: 0.2.9
Release: 1
Summary: Archival and Restoration for Postgres

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/wal-g/wal-g/releases/download/v%{version}/wal-g.linux-amd64.tar.gz
Source0: https://raw.githubusercontent.com/patsevanton/wal-g-rpm/master/SOURCES/server-s3.conf

%description
WAL-G is the successor of WAL-E with a number of key differences. WAL-G uses LZ4, LZMA or Brotli compression, multiple processors
and non-exclusive base backups for Postgres. More information on the design and implementation of WAL-G can be found on the
Citus Data blog post "Introducing WAL-G by Citus: Faster Disaster Recovery for Postgres".

%prep
curl -o %{_sourcedir}/wal-g.linux-amd64.tar.gz %{url}
pwd
ls
tar -zxf wal-g.linux-amd64.tar.gz

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
ls -lh %{_sourcedir}
cp wal-g %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
