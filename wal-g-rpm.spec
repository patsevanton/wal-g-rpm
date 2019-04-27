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
Source1: https://raw.githubusercontent.com/patsevanton/wal-g-rpm/master/SOURCES/server-s3.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
WAL-G is the successor of WAL-E with a number of key differences. WAL-G uses LZ4, LZMA or Brotli compression, multiple processors
and non-exclusive base backups for Postgres. More information on the design and implementation of WAL-G can be found on the
Citus Data blog post "Introducing WAL-G by Citus: Faster Disaster Recovery for Postgres".

%prep
#%setup -c -n wal-g-%{version}-%{release}.x86_64
%setup -q -c

%install
ls
pwd
#cd wal-g-%{version}-%{release}.x86_64
ls %{buildroot}
%{__install} -m 0755 -d %{buildroot}%{_bindir}
ls %{buildroot}
%{__install} -m 0755 -d %{buildroot}/etc/wal-g.d/
ls %{buildroot}
cp wal-g %{buildroot}%{_bindir}/%{name}
%{__install} -m 0644 %{SOURCE1} %{buildroot}/etc/wal-g.d/server-s3.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
/etc/wal-g.d/server-s3.conf
