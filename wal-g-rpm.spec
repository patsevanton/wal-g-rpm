%global _prefix /usr/local

Name:    wal-g
Version: 0.2.9
Release: 1
Summary: Archival and Restoration for Postgres

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/wal-g/wal-g/releases/download/v0.2.9/wal-g.linux-amd64.tar.gz
Source0: server-s3.conf
BuildRequires:  tree

%description
WAL-G is the successor of WAL-E with a number of key differences. WAL-G uses LZ4, LZMA or Brotli compression, multiple processors
and non-exclusive base backups for Postgres. More information on the design and implementation of WAL-G can be found on the
Citus Data blog post "Introducing WAL-G by Citus: Faster Disaster Recovery for Postgres".

%prep
#curl -o %{_sourcedir}/wal-g.linux-amd64.tar.gz %{url}
curl -L https://github.com/wal-g/wal-g/releases/download/v0.2.9/wal-g.linux-amd64.tar.gz > wal-g.linux-amd64.tar.gz
pwd
ls
tar -zxf wal-g.linux-amd64.tar.gz
tree
tree %{_sourcedir}

%install
ls %{_sourcedir}
ls %{_sourcedir}/v%{version}
%{__install} -m 0755 -d %{buildroot}%{_bindir}
cp wal-g %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
