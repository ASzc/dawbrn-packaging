%global srcname async-timeout

Name:           rh-python35-%{srcname}
Version:        1.2.1
Release:        2%{?dist}
Summary:        asyncio-compatible timeout context manager

License:        ASL 2.0
URL:            https://github.com/aio-libs/async-timeout
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires: rh-python35
BuildRequires: rh-python35

%global __python scl enable rh-python35 -- python
%global __python3 scl enable rh-python35 -- python

%description
asyncio-compatible timeout context manager
The context manager is useful in cases when you want to apply timeout
logic around block of code or in cases when asyncio.wait_for() is not
suitable. Also it's much faster than asyncio.wait_for() because timeout
doesn't create a new task.

%prep
%setup -q -n async-timeout-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%license LICENSE
%doc README.rst CHANGES.rst
/opt/rh/rh-python35/root/usr/lib/python3.5/site-packages/%{srcname}-*.egg-info
/opt/rh/rh-python35/root/usr/lib/python3.5/site-packages/%{srcname}

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sun Mar 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuild for Python 3.6

* Thu Nov 17 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-3
- Add missing BR
- Rename the pkg

* Sun Nov 13 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-2
- Update files section and the description

* Fri Nov 11 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-1
- Initial spec

