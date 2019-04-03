%global _prefix /usr/local
%global __strip /bin/true

Name:    wal-g
Version: 0.2.7
Release: 1
Summary: Archival and Restoration for Postgres

Group:   Development Tools
URL:     https://github.com/wal-g/wal-g
License: ASL 2.0
Source0: https://github.com/wal-g/wal-g/releases/download/v%{version}/wal-g.linux-amd64.tar.gz
Source1: server-s3.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
WAL-G is the successor of WAL-E with a number of key differences. WAL-G uses LZ4, LZMA or Brotli compression, multiple processors
and non-exclusive base backups for Postgres. More information on the design and implementation of WAL-G can be found on the
Citus Data blog post "Introducing WAL-G by Citus: Faster Disaster Recovery for Postgres".

%prep
%setup -q -c -n wal-g.linux-amd64

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -m 0755 -d %{buildroot}%{_bindir}
%{__install} -m 0755 -d %{buildroot}/etc/wal-g.d/
cp wal-g %{buildroot}/%{_bindir}/%{name}
%{__install} -m 0644 %{SOURCE1} %{buildroot}/etc/wal-g.d/server-s3.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
/etc/wal-g.d/server-s3.conf
