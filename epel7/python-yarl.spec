AutoReq: no

%global srcname yarl

Name:           rh-python35-%{srcname}
Version:        0.12.0
Release:        3%{?dist}
Summary:        Python module to handle URLs

License:        ASL 2.0
URL:            https://pythonhosted.org/yarl/
Source0:        https://github.com/aio-libs/yarl/archive/v%{version}/%{srcname}-%{version}.tar.gz

Requires:       rh-python35-multidict

Requires: rh-python35
BuildRequires: rh-python35

%global __python scl enable rh-python35 -- python
%global __python3 scl enable rh-python35 -- python

%description
The module provides handy URL class for url parsing and changing.

%prep
%setup -q -n %{srcname}-%{version}

%build
CFLAGS="%{optflags}" %{__python3} setup.py build
sleep 1

%install
CFLAGS="%{optflags}" %{__python3} setup.py install -O1 --skip-build --root %{buildroot}
rm -vf %{buildroot}/opt/rh/rh-python35/root/usr/lib64/python3.5/site-packages/%{srcname}/_quoting.c

%files
%doc CHANGES.rst README.rst
%license LICENSE
/opt/rh/rh-python35/root/usr/lib64/python3.5/site-packages/%{srcname}-*.egg-info
/opt/rh/rh-python35/root/usr/lib64/python3.5/site-packages/%{srcname}

%changelog
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Update to latest upstream release 0.12.0 (rhbz#1471102)

* Wed Jun 28 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-1
- Update to latest upstream release 0.11.0 (rhbz#1465202)

* Wed Jun 14 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.3-1
- Update to 0.10.3 (rhbz#1461225)

* Tue May 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Wed Mar 15 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.0-1
- Update to latest upstream release 0.10.0 (rhbz#1432279)

* Mon Feb 20 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.8-1
- Update to latest upstream release 0.9.8 (rhbz#1423061)

* Thu Feb 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.6-1
- Update to 0.9.6

* Thu Feb 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-1
- Update to 0.9.2

* Wed Feb 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.8.1-4
- Fix BRs

* Tue Feb 07 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-3
- Update BR

* Fri Jan 27 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-2
- Don't remove _quoting.c

* Sat Jan 21 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-1
- Update to latest upstream release 0.8.1
- Remove _quoting.c

* Mon Nov 21 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-2
- Update Source0, summary

* Fri Nov 18 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Initial package
