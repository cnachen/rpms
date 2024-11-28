%define debug_package %{nil}

Name: keyd-chromebook-c1030
Version: 0.1.0
Release: 1%{?dist}
Summary: The keyd config for HP Elite c1030 Chromebook.
License: MIT
URL: https://github.com/cnachen/rpms
Source0: chromebook-c1030.conf
BuildArch: noarch

Requires: keyd

%description
%{summary}

%prep

%build

%install
install -dm755 %{buildroot}%{_sysconfdir}/keyd/
install -m644 %{S:0} %{buildroot}%{_sysconfdir}/keyd/

%files
%config(noreplace) %{_sysconfdir}/keyd/

%changelog
%autochangelog
