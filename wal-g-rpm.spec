%global _prefix /usr/local

Name:    wal-g
Version: 0.2.9
Release: 1
Summary: Archival and Restoration for Postgres

Group:   Development Tools
URL:     https://github.com/wal-g/wal-g
License: ASL 2.0
URL: https://github.com/wal-g/wal-g/releases/download/v%{version}/wal-g.linux-amd64.tar.gz

%description
WAL-G is the successor of WAL-E with a number of key differences. WAL-G uses LZ4, LZMA or Brotli compression, multiple processors
and non-exclusive base backups for Postgres. More information on the design and implementation of WAL-G can be found on the
Citus Data blog post "Introducing WAL-G by Citus: Faster Disaster Recovery for Postgres".

%prep
curl -o %{_sourcedir}/wal-g.linux-amd64.tar.gz %{url}
%setup -q -c

%install
tree
%{__install} -m 0755 -d %{buildroot}%{_bindir}
tree %{_sourcedir}
ls -lh %{_sourcedir}
cp wal-g %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
