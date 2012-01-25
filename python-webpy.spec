%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname webpy
%define srcname web.py

Name:           python-%{pkgname}
Version:        0.36
Release:        1%{?dist}
Summary:        A simple web framework for Python
Group:          Development/Libraries

# The entire source code is Public Domain save for the following exceptions:
#   web/wsgiserver (CherryPy/BSD)
#     See LICENSE.wsgiserver.txt
#     See http://fedoraproject.org/wiki/Licensing:BSD#New_BSD_.28no_advertising.2C_3_clause.29
#   web/debugerror.py (Modified BSD)
#     This is from django
#     See http://code.djangoproject.com/browser/django/trunk/LICENSE
#   web/httpserver.py (Modified BSD)
#     This is from WSGIUtils/lib/wsgiutils/wsgiServer.py
#     See http://www.xfree86.org/3.3.6/COPYRIGHT2.html#5
License:        Public Domain and BSD

URL:            http://webpy.org/
Source0:        http://webpy.org/static/%{srcname}-%{version}.tar.gz
BuildRequires:  python-devel
BuildArch:      noarch

%description
web.py is a web framework for python that is as simple as it is
powerful. web.py is in the public domain; you can use it for whatever
purpose with absolutely no restrictions. 

%prep
%setup -q -n web.py-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%doc PKG-INFO
%{python_sitelib}/*

%changelog
* Wed Jan 25 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.36-1
- rebase to 0.36

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-7

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
