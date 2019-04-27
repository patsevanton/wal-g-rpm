Name:    wal-g
Version: 0.2.7
Release: 1
Summary: Archival and Restoration for Postgres

Group:   Development Tools
URL:     https://github.com/wal-g/wal-g
License: ASL 2.0
Source0: https://github.com/wal-g/wal-g/releases/download/v0.2.7/wal-g.linux-amd64.tar.gz
BuildRequires:  tree

%description
WAL-G

%prep
tree
%setup -q -c
tree

%install
tree
ls
pwd
ls %{buildroot}
tree
cp wal-g %{buildroot}%{_bindir}/%{name}
