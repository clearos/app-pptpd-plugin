
Name: app-pptpd-plugin
Epoch: 1
Version: 2.1.6
Release: 1%{dist}
Summary: PPTP Server Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-pptpd-plugin-%{version}.tar.gz
Buildarch: noarch

%description
PPTP Server Policies provide access control for the PPTP server app.

%package core
Summary: PPTP Server Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
PPTP Server Policies provide access control for the PPTP server app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/pptpd_plugin
cp -r * %{buildroot}/usr/clearos/apps/pptpd_plugin/

install -D -m 0644 packaging/pptpd.php %{buildroot}/var/clearos/accounts/plugins/pptpd.php

%post core
logger -p local6.notice -t installer 'app-pptpd-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/pptpd_plugin/deploy/install ] && /usr/clearos/apps/pptpd_plugin/deploy/install
fi

[ -x /usr/clearos/apps/pptpd_plugin/deploy/upgrade ] && /usr/clearos/apps/pptpd_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-pptpd-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/pptpd_plugin/deploy/uninstall ] && /usr/clearos/apps/pptpd_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/pptpd_plugin/packaging
%dir /usr/clearos/apps/pptpd_plugin
/usr/clearos/apps/pptpd_plugin/deploy
/usr/clearos/apps/pptpd_plugin/language
/var/clearos/accounts/plugins/pptpd.php
