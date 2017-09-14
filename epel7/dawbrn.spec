Name: dawbrn
Version: 1.0.2
Release: 1%{?dist}
Summary: Documentation Autobuilds Would Be Really Nice
License: ASL 2.0
BuildArch: noarch
Url: https://github.com/ASzc/dawbrn
Source0: https://github.com/ASzc/dawbrn/archive/dawbrn-%{version}.tar.gz
Requires: rh-git29, rh-python35, rh-python35-aiohttp, docker
BuildRequires: rh-python35

%global __python scl enable rh-python35 -- python

%description
Daemon for automatic documentation build and deployment

%prep
%setup -q -n dawbrn-%{version}

%build

%install
mkdir -p %{buildroot}%{_usr}/lib/dawbrn/
cp -r dawbrn %{buildroot}%{_usr}/lib/dawbrn/
cd install
install -Dm644 usr/lib/systemd/system/dawbrn.service %{buildroot}%{_usr}/lib/systemd/system/dawbrn.service
install -Dm440 etc/sudoers.d/10-dawbrn %{buildroot}%{_sysconfdir}/sudoers.d/10-dawbrn
install -Dm600 etc/sysconfig/dawbrn %{buildroot}%{_sysconfdir}/sysconfig/dawbrn
install -Dm755 usr/bin/dawbrn_dockerbuild %{buildroot}%{_bindir}/dawbrn_dockerbuild
install -Dm755 etc/dawbrn/dockerbuild.d/10-maven.sh %{buildroot}%{_sysconfdir}/dawbrn/dockerbuild.d/10-maven.sh
install -dm700 %{buildroot}%{_localstatedir}/lib/dawbrn
install -Dm664 var/lib/dawbrn/gitconfig %{buildroot}%{_localstatedir}/lib/dawbrn/.gitconfig
# cache
install -Dm644 etc/nginx/conf.d/10-dawbrn-cache.conf %{buildroot}%{_sysconfdir}/nginx/conf.d/10-dawbrn-cache.conf
install -Dm755 usr/bin/dawbrn_cache-posttrans %{buildroot}%{_bindir}/dawbrn_cache-posttrans
install -dm755 %{buildroot}%{_sysconfdir}/dawbrn/maven-cache
install -dm700 %{buildroot}%{_localstatedir}/lib/nginx/dawbrn_cache
# cache-mavencentral
install -Dm644 etc/nginx/default.d/10-dawbrn-cache-mavencentral.conf %{buildroot}%{_sysconfdir}/nginx/default.d/10-dawbrn-cache-mavencentral.conf
install -Dm644 etc/dawbrn/maven-cache.d/10-mavencentral.xml %{buildroot}%{_sysconfdir}/dawbrn/maven-cache.d/10-mavencentral.xml

%clean
rm -rf $RPM_BUILD_ROOT

%pre
getent group dawbrn > /dev/null || /usr/sbin/groupadd -r dawbrn
getent passwd dawbrn > /dev/null || /usr/sbin/useradd -r -g dawbrn \
       -d %{_localstatedir}/lib/dawbrn -s /sbin/nologin dawbrn
:

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_usr}/lib/dawbrn/*
%{_usr}/lib/systemd/system/dawbrn.service
%{_sysconfdir}/sudoers.d/10-dawbrn
%config(noreplace) %{_sysconfdir}/sysconfig/dawbrn
%{_bindir}/dawbrn_dockerbuild
%{_sysconfdir}/dawbrn/dockerbuild.d/10-maven.sh
%defattr(-,dawbrn,dawbrn)
%dir %{_localstatedir}/lib/dawbrn
%{_localstatedir}/lib/dawbrn/.gitconfig

%changelog
* Wed Aug 02 2017 Alex Szczuczko <aszczucz@redhat.com> - 1.0.0-1
- Initial package



%package cache
Version: 1.0.2
Release: 1%{?dist}
Summary: nginx-based caches for dawbrn
Requires: nginx

%description cache
Configuration file for nginx to cache for dawbrn

%postun cache
rm -f %{_sysconfdir}/dawbrn/maven-cache/settings.xml

%files cache
%defattr(-,root,root)
%{_sysconfdir}/nginx/conf.d/10-dawbrn-cache.conf
%{_bindir}/dawbrn_cache-posttrans
%dir %{_sysconfdir}/dawbrn/maven-cache.d
%dir %{_sysconfdir}/dawbrn/maven-cache
%ghost %{_sysconfdir}/dawbrn/maven-cache/settings.xml
%dir %attr(-,nginx,nginx) %{_localstatedir}/lib/nginx/dawbrn_cache



%package cache-mavencentral
Version: 1.0.2
Release: 1%{?dist}
Summary: nginx-based cache of Maven Central for dawbrn
Requires: dawbrn-cache

%description cache-mavencentral
Configuration file for nginx to cache maven central

%post cache-mavencentral
%{_bindir}/dawbrn_cache-posttrans

%postun cache-mavencentral
%{_bindir}/dawbrn_cache-posttrans

%files cache-mavencentral
%defattr(-,root,root)
%{_sysconfdir}/dawbrn/maven-cache.d/10-mavencentral.xml
%{_sysconfdir}/nginx/default.d/10-dawbrn-cache-mavencentral.conf
