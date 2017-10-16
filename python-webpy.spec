%if 0%{?fedora}
%global with_python3 1
%endif

%global pkgname webpy
%global srcname web.py

%global commit b725a4f7dda3114c626ccdf7a7004c21efb8ba8b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           python-%{pkgname}
Version:        0.40.dev0
Release:        20170809git%{shortcommit}%{?dist}
Summary:        A simple web framework for Python
Group:          Development/Libraries

# The entire source code is Public Domain save for the following exceptions:
#   web/debugerror.py (Modified BSD)
#     This is from django
#     See http://code.djangoproject.com/browser/django/trunk/LICENSE
#   web/httpserver.py (Modified BSD)
#     This is from WSGIUtils/lib/wsgiutils/wsgiServer.py
#     See http://www.xfree86.org/3.3.6/COPYRIGHT2.html#5
License:        Public Domain and BSD

URL:            http://webpy.org/
Source0:        https://github.com/%{pkgname}/%{pkgname}/archive/%{commit}/%{pkgname}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch

%global _description\
web.py is a web framework for python that is as simple as it is\
powerful. web.py is in the public domain; you can use it for whatever\
purpose with absolutely no restrictions.

%description %_description

%package -n python2-%{pkgname}
Summary: %summary
Requires:       python-cherrypy
BuildRequires:  python2-devel
%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname} %_description


%if 0%{?with_python3}
%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       python3-cherrypy
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
%_description

%endif

%prep
%autosetup -n %{pkgname}-%{commit}


%build
%{__python} setup.py build
%if 0%{?with_python3}
%py3_build
%endif


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm %{buildroot}%{python2_sitelib}/web/wsgiserver/wsgiserver3.py*

%if 0%{?with_python3}
%py3_install
rm %{buildroot}%{python3_sitelib}/web/wsgiserver/wsgiserver2.py*
%endif


%files -n python2-%{pkgname}
%doc README.md
%license LICENSE.txt
%{python2_sitelib}/web
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info

%if 0%{?with_python3}
%files -n python3-%{pkgname}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/web
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%endif


%changelog
* Mon Oct 16 2017 Jan Beran <jberan@redhat.com> - 0.40.dev0-20170809gitb725a4f
- new version from the latest commit 0.40.dev0-20170809gitb725a4f
- modernized specfile with Python 3 subpackage

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.37-11
- Python 2 binary package renamed to python2-webpy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.37-1
- update to 0.37
- minor spec cleanup

* Wed Mar 14 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.36-2
- unbundle cherrypy-code

* Wed Jan 25 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.36-1
- rebase to 0.36

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 0.32-3
- Strip shebang from non-scripts
- Update license information
- Enable unit tests

* Thu Jul 02 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 0.32-2
- Added python-devel BuildRequires
- Updated with multiple licensing annotations

* Wed Jul 01 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 0.32-1
- Rebase to 0.32

* Mon Jun 01 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 0.31-1
- Initial package
