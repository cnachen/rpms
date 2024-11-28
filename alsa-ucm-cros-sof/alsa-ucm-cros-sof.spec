%define debug_package %{nil}

Name:			alsa-ucm-cros-sof
Version:		0.7
Release:		1%{?dist}
Summary:		ALSA Use Case Manager configuration
License:		BSD-3-Clause
URL:			https://github.com/WeirdTreeThing/alsa-ucm-conf-cros
Source0:		%{url}/archive/refs/tags/%{version}.tar.gz
Source1:		https://raw.githubusercontent.com/WeirdTreeThing/chromebook-linux-audio/refs/heads/main/conf/common/51-increase-headroom.conf
BuildArch:		noarch

Requires:		alsa-sof-firmware
Requires:		alsa-ucm
Requires:		wireplumber >= 0.5.0

%description
%{summary} for glk/cml/jsl/tgl/adl chromebooks.

%prep
%autosetup -n alsa-ucm-conf-cros-%{version}
rm -r ucm2/conf.d/hdaudioB0D2/
chmod g-w -R ucm2/

%build

%install
install -dm755 %{buildroot}%{_sysconfdir}/wireplumber/wireplumber.conf.d/
install -m644 %{S:1} %{buildroot}%{_sysconfdir}/wireplumber/wireplumber.conf.d/
install -dm755 %{buildroot}%{_datadir}/alsa/
cp -r ucm2 %{buildroot}%{_datadir}/alsa/

%files
%doc README.md
%license LICENSE
%config %{_sysconfdir}/wireplumber/wireplumber.conf.d/
%{_datadir}/alsa/ucm2/

%changelog
%autochangelog
