%global modname multidict

#global rctag b4

Name:           rh-python35-%{modname}
Version:        3.1.3
Release:        3%{?dist}
Summary:        MultiDict implementation

License:        ASL 2.0
URL:            https://github.com/aio-libs/multidict
Source0:        %{url}/archive/v%{version}%{?rctag:%{rctag}}/%{modname}-%{version}%{?rctag:%{rctag}}.tar.gz

Requires: rh-python35
BuildRequires: rh-python35

%global __python scl enable rh-python35 -- python
%global __python3 scl enable rh-python35 -- python

%description
Multidicts are useful for working with HTTP headers, URL query args etc.
The code was extracted from aiohttp library.

%prep
%setup -q -n %{modname}-%{version}%{?rctag:%{rctag}}
rm -f %{modname}/*.c

%build
CFLAGS="%{optflags}" %{__python3} setup.py build
sleep 1

%install
CFLAGS="%{optflags}" %{__python3} setup.py install -O1 --skip-build --root %{buildroot}
rm -f %{buildroot}/opt/rh/rh-python35/root/usr/lib64/python3.5/site-packages/%{modname}/*.{c,pyx}

%files
%license LICENSE
%doc README.rst CHANGES.rst
/opt/rh/rh-python35/root/usr/lib64/python3.5/site-packages/%{modname}-*.egg-info
/opt/rh/rh-python35/root/usr/lib64/python3.5/site-packages/%{modname}

%changelog
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Mon Jul 03 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- Ignore tests until imports are fixed

* Thu Jun 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-1.1
- Rebuild for Python 3.6

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.4-1
- Update to 2.1.4

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.3-1
- Update to 2.1.3

* Mon Nov 07 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Fri Sep 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-1.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.0-1
- Update to 1.1.0
- Trivial fixes

* Thu Jun 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.0-0.1b4
- Initial package
