
%global packagename storm-bes-config
%global version     %{?VERSION}
%global release     %{?RELEASE}
%global buildroot %{_tmppath}/%{packagename}-%{version}-%{release}-build-%(%{__id_u} -n)


Summary:        Tools to configure BES-specific insallation of StoRM
Name:           %{packagename}
Version:        %{version}
Release:        %{release}

License:        GPLv3
Group:          Applications/System
URL :           http://bes3.ihep.ac.cn/
Vendor:         BES Collaboration, http://bes3.ihep.ac.cn/
BuildRoot:      %{buildroot}
BuildArch:      noarch

Source0:        %{packagename}-%{version}.tar.gz

Requires:       ca-policy-egi-core
Requires:       emi-storm-backend-mp
Requires:       emi-storm-frontend-mp
Requires:       emi-storm-globus-gridftp-mp

Requires:       acl
Requires:       attr
Requires:       ntp
Requires:       java7
Requires:       httpd
Requires:       mod_ssl

Conflicts:      emi-storm-gridhttps-mp
Conflicts:      storm-gridhttps-server


%description
Tools to configure installation of StoRM specific to BES VO.

%prep
%setup -q -n %{packagename}-%{version}


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} -p %{buildroot}

%{__mkdir_p} %{buildroot}/etc/
%{__cp} -r etc/* -t %{buildroot}/etc/

%{__mkdir_p} %{buildroot}/etc/storm-bes/httpd/conf.d/bes-webdav

%{__mkdir_p} %{buildroot}/usr/
%{__cp} -r usr/* -t %{buildroot}/usr/


%clean
%{__rm} -rf %{buildroot}


%postun
#during an upgrade, the value of the argument passed in is 1
#during an uninstall, the value of the argument passed in is 0
if [ "$1" = "0" ] ; then
    %{__rm} -rf /etc/httpd/conf.d/bes-webdav*
    service httpd condrestart
fi


%files
%defattr(-,root,root,-)
/etc/cron.d/*
/etc/logrotate.d/*
/etc/security/limits.d/*
/usr/sbin/*

%attr(640,root,root) /etc/storm-bes/

%doc README INSTALL ChangeLog

%changelog ChangeLog
